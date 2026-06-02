import os

selectors = {
    "URL": "https://www.flightradar24.com/",
    "CLOSE_POPUP": "button[class='rounded-md bg-white p-2 text-blue-500']",
    "AGREE_COOKIES": "button[id='gravitoTCFCMP-layer1-accept-all']",
    "LOGIN": "button[data-testid='auth-toggle']",
    "email_input": "input[type='email'][data-testid='email']",
    "password_input": "input[type='password'][data-testid='password']",
    "SETTINGS": "button[data-testid='panel-selector__settings']",
    "B_AND_W": "button[data-testid='image-toggle-black_white__button']",
    "CLOSE_SETTINGS": "button[data-testid='settings__close']",
    "fly_number": "span[data-testid='aircraft-panel__header__flight-number']",
    "fly_code": "span[data-testid='aircraft-panel__header__model']",
    "departure_city": "span[data-testid='aircraft-panel__airport-departure-city']",
    "arrival_city": "span[data-testid='aircraft-panel__airport-arrival-city']",
    "time_remaining": "span[data-testid='aircraft-panel__flight-time-remaining']",
    "close_flight_info": "#app > div > div > div.flex.min-h-full.w-0.flex-1.flex-col.overflow-hidden.bg-white > main > div > div > div > div.absolute.flex.top-12.rounded-xl.mt-4.ml-4.z-40.lg\:top-0.w-84.overflow-hidden.shadow-default > div > header > div.flex.items-start.justify-between > button"

}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

images_path = {
    "aviao": os.path.join(BASE_DIR, "asset_aviao_transparent.png"),
    "helicoptero": os.path.join(BASE_DIR, "asset_helicopter_transparent.png")
}