from src.modulos.SELENIUM.Desafio01_27_04_2026_MCeMB.SELENIUM.actions.navigation import Navigation as Nav 
from src.modulos.SELENIUM.Desafio01_27_04_2026_MCeMB.SELENIUM.actions.data_handler import Data_Handler as DH
from src.utils.constants.constants import URL   

def main():

    nav = Nav(URL)
    
    nav.get_products(URL)
    dh = DH(nav.items)
    dh.save_to_csv("products.csv")

    maior_preco, menor_preco = dh.max_min()
        
    print(f"Maior preço: R${maior_preco}")
    print(f"Menor preço: R${menor_preco}")
        
if __name__ == "__main__":
    main()