import os
import csv  

class Data_Handler:
    def __init__(self, data):
        self.items = data
        script_path = os.path.dirname(__file__)
        self.folder_path = os.path.dirname(script_path)

    def max_min(self):
        todos_os_precos = [float(produto["price"].split()[1]) for produto in self.items]

        maximum = max(todos_os_precos)
        minimum = min(todos_os_precos)
        return maximum, minimum
    
    def save_to_csv(self, filename):
        with open(os.path.join(self.folder_path, filename), 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "price", "id", "href"])
            writer.writeheader()
            writer.writerows(self.items) 