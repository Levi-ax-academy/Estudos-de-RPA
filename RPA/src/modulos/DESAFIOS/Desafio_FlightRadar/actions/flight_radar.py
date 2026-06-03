from playwright.sync_api import Playwright
from src.modulos.DESAFIOS.Desafio_FlightRadar.data_assets.mock import images_path as ipath, selectors as sel
from src.modulos.DESAFIOS.Desafio_FlightRadar.actions.browser_manager import BrowserManager as BM
from src.modulos.DESAFIOS.Desafio_FlightRadar.actions.flight_data_manager import FlightDataManager as FDM
import pyautogui as pyag
import os
from time import sleep

class FlightRadar:
    def __init__(self, playwright: Playwright):
        self.bm = BM(playwright)
        self.page = self.bm.page
        self.data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data_assets")
        self.fdm = FDM(data_dir=self.data_dir)
        self.seen_ids = set()
    def _find_next_center(self, image, excluded_centers, region, confidence=0.5, proximity=40):
        matches = list(pyag.locateAllOnScreen(image=image, confidence=confidence, region=region))
        for m in matches:
            cx = m.left + m.width // 2
            cy = m.top + m.height // 2
            too_close = False
            for ex in excluded_centers:
                if abs(cx - ex[0]) <= proximity and abs(cy - ex[1]) <= proximity:
                    too_close = True
                    break
            if not too_close:
                return (cx, cy)
        return None

    def _count_valid_fields(self, info):
        valid_fields = 0
        if info.get("fly_number"):
            valid_fields += 1
        if info.get("fly_code"):
            valid_fields += 1
        if info.get("departure_city"):
            valid_fields += 1
        if info.get("arrival_city"):
            valid_fields += 1
        if info.get("time_remaining"):
            valid_fields += 1
        return valid_fields

    def _get_unique_id(self, info: dict):
        """Return the best unique id for a flight (prefer fly_code, fall back to fly_number)."""
        code = info.get("fly_code")
        if code:
            return code.strip()
        num = info.get("fly_number")
        if num:
            return num.strip()
        return None

    def _is_duplicate(self, info: dict) -> bool:
        uid = self._get_unique_id(info)
        return uid is not None and uid in self.seen_ids

    def _register_seen(self, info: dict):
        uid = self._get_unique_id(info)
        if uid:
            self.seen_ids.add(uid)

    def Apply_filters(self):
        self.page.locator(sel["SETTINGS"]).wait_for(state="visible")
        self.page.locator(sel["SETTINGS"]).click()
        self.page.locator(sel["B_AND_W"]).wait_for(state="visible", timeout=10000)
        self.page.locator(sel["B_AND_W"]).click()
        self.page.locator(sel["CLOSE_SETTINGS"]).click()
        self.page.wait_for_timeout(3000)

    def Check_Planes(self):
        # Aviões: coletar até 5 aviões verdadeiros; cliques falsos não incrementam o contador
        max_planes = 5
        found_planes = 0
        attempts = 0
        max_attempts = 60
        excluded = []
        region_plane = (25,120,1180,880)
        self.page.goto("https://www.flightradar24.com/39.67,-3.82/8")
        while found_planes < max_planes and attempts < max_attempts:
            try:
                planes_center = self._find_next_center(ipath["aviao"], excluded, region_plane, confidence=0.7)
            except Exception as e:
                print(f"Erro ao encontrar avião: {e}")
                if type(e).__name__ == "ImageNotFoundException":
                    pyag.scroll(500)  # Tentar rolar a tela para encontrar novos aviões
                    self.bm.navigate_on_screen(attempts=19)
                
            print(f"Avião candidato encontrado: {planes_center}")
            self.bm.navigate_on_screen(attempts)  # Tentar mover a tela para encontrar novos aviões a cada 10 tentativas
            
            if not planes_center:
                print("Nenhum novo candidato para avião encontrado no momento.")
                attempts += 1
                sleep(0.5)
                continue

            pyag.moveTo(planes_center[0], planes_center[1])
            pyag.click()
            sleep(5)
            if self.page.locator(sel["fly_number"]).is_visible() or self.page.locator(sel["fly_code"]).is_visible():
                print("Painel aberto: coletando informações do avião...")
                which_plane = f"aviao{found_planes}.png"
                flight_info = self.Scrap_Flight_Infos(airplane_type="aviao", which_airplane=which_plane, save=False)
                valid_fields = self._count_valid_fields(flight_info)
                print(f"Campos válidos: {valid_fields}/5")
                if valid_fields >= 3:
                    # checar duplicata antes de salvar
                    if self._is_duplicate(flight_info):
                        print(f"Avião duplicado detectado ({self._get_unique_id(flight_info)}). Ignorando.")
                        try:
                            self.page.locator(sel["close_flight_info"]).click()
                        except Exception:
                            pass
                        excluded.append(planes_center)
                    else:
                        print("Alvo válido: salvando e contando o avião.")
                        flight_info["which_airplane"] = which_plane
                        self._save_flight_data_if_valid(flight_info)
                        self._register_seen(flight_info)
                        pyag.screenshot(imageFilename=os.path.join(self.data_dir, which_plane))
                        sleep(1)
                        try:
                            self.page.locator(sel["close_flight_info"]).click()
                        except Exception:
                            pass
                        found_planes += 1
                else:
                    print("Avião inválido: faltam campos, continuando busca.")
                    try:
                        self.page.locator(sel["close_flight_info"]).click()
                    except Exception:
                        pass
                excluded.append(planes_center)
            else:
                print("Alvo falso: continuando busca sem incrementar contador.")
                excluded.append(planes_center)
            attempts += 1

    def Check_Helicopters(self):
        # Helicópteros: mesma lógica, coletar até 2 reais
        max_helis = 2
        found_helis = 0
        attempts = 0
        max_attempts = 60

        excluded = []
        region_heli = (30,130,1160,860)
        self.page.goto("https://www.flightradar24.com/-23.52,-46.61/12")

        sleep(10)
        while found_helis < max_helis and attempts < max_attempts:
            try:
                helicopter_center = self._find_next_center(ipath["helicoptero"], excluded, region_heli, confidence=0.45)
            except Exception as e:
                print(f"Erro ao encontrar helicóptero: {e}")
                if type(e).__name__ == "ImageNotFoundException":
                    pyag.scroll(500)  # Tentar rolar a tela para encontrar novos helicópteros
                    self.bm.navigate_on_screen(attempts=19)  # Tentar mover a tela para encontrar novos helicópteros a cada 10 tentativas
            print(f"Helicóptero candidato encontrado: {helicopter_center}")
            if attempts in [4,14,24,34,44,54]:  # A cada 5 tentativas, tentar mover a tela para encontrar novos helicópteros
                self.bm.navigate_on_screen(attempts+5)
            if attempts in [9,19,29,39,49,59]:  # A cada 10 tentativas, tentar mover a tela para encontrar novos helicópteros
                self.bm.navigate_on_screen(attempts)
            if not helicopter_center:
                print("Nenhum novo candidato para helicóptero encontrado no momento.")
                attempts += 1
                sleep(0.5)
                continue
            pyag.moveTo(helicopter_center[0], helicopter_center[1])
            pyag.click()
            sleep(5)
            if self.page.locator(sel["fly_number"]).is_visible() or self.page.locator(sel["fly_code"]).is_visible():
                print("Painel aberto: coletando informações do helicóptero...")
                which_heli = f"helicopteros{found_helis}.png"
                flight_info = self.Scrap_Flight_Infos(airplane_type="helicoptero", which_airplane=which_heli, save=False)
                valid_fields = self._count_valid_fields(flight_info)
                print(f"Campos válidos: {valid_fields}/5")
                if valid_fields >= 2:  # Para helicópteros, aceitar se tiver pelo menos 2 campos válidos, dada a dificuldade de obter dados completos
                    # checar duplicata antes de salvar
                    if self._is_duplicate(flight_info):
                        print(f"Helicóptero duplicado detectado ({self._get_unique_id(flight_info)}). Ignorando.")
                        try:
                            self.page.locator(sel["close_flight_info"]).click()
                        except Exception:
                            pass
                        excluded.append(helicopter_center)
                    else:
                        print("Alvo válido: salvando e contando o helicóptero.")
                        flight_info["which_airplane"] = which_heli
                        self._save_flight_data_if_valid(flight_info)
                        self._register_seen(flight_info)
                        pyag.screenshot(imageFilename=os.path.join(self.data_dir, which_heli))
                        sleep(1)
                        try:
                            self.page.locator(sel["close_flight_info"]).click()
                        except Exception:
                            pass
                        found_helis += 1
                else:
                    print("Helicóptero inválido: faltam campos, continuando busca.")
                    try:
                        self.page.locator(sel["close_flight_info"]).click()
                    except Exception:
                        pass
                excluded.append(helicopter_center)
            else:
                print("Alvo falso: continuando busca sem incrementar contador.")
                excluded.append(helicopter_center)
            attempts += 1
       
    def Scrap_Flight_Infos(self, airplane_type, which_airplane, save=True):
        sleep(5)
        self.fly_number = self.page.locator(sel["fly_number"]).all_inner_texts()
        self.fly_code = self.page.locator(sel["fly_code"]).all_inner_texts()
        self.departure_city = self.page.locator(sel["departure_city"]).all_inner_texts()
        self.arrival_city = self.page.locator(sel["arrival_city"]).all_inner_texts()
        self.time_remaining = self.page.locator(sel["time_remaining"]).all_inner_texts()
        self.time_remaining = self.time_remaining[0].split(' in ')[1].strip() if self.time_remaining and ' in ' in self.time_remaining[0] else ""
        self.print_path = os.path.join(self.data_dir, f"flight_info_{which_airplane}")
        pyag.screenshot(imageFilename=self.print_path, region=[40,205,425,776])
        flight_info = {
            "airplane_type": airplane_type,
            "fly_number": self.fly_number[0] if self.fly_number else "",
            "fly_code": self.fly_code[0] if self.fly_code else "",
            "departure_city": self.departure_city[0] if self.departure_city else "",
            "arrival_city": self.arrival_city[0] if self.arrival_city else "",
            "time_remaining": self.time_remaining,
        }
        if save:
            self.fdm.save_flight_data(airplane_type, self.fly_number, self.fly_code, self.departure_city, self.arrival_city, self.time_remaining)
        return flight_info

    def _save_flight_data_if_valid(self, info):
        self.fdm.save_flight_data(
            info["airplane_type"],
            [info["fly_number"]] if info["fly_number"] else [],
            [info["fly_code"]] if info["fly_code"] else [],
            [info["departure_city"]] if info["departure_city"] else [],
            [info["arrival_city"]] if info["arrival_city"] else [],
            info["time_remaining"],
        )