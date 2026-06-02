import os
import csv

class FlightDataManager:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        self.csv_path = os.path.join(data_dir, "flights_data.csv")
        self._initialize_csv()
    
    def _initialize_csv(self):
        if not os.path.exists(self.csv_path):
            with open(self.csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Type", "Flight Number", "Flight Code", "Departure City", "Arrival City", "Time Remaining"])
    
    def save_flight_data(self, aircraft_type: str, fly_number: list, fly_code: list, 
                         departure_city: list, arrival_city: list, time_remaining: str):
        data = [
            aircraft_type,
            fly_number[0] if fly_number else "",
            fly_code[0] if fly_code else "",
            departure_city[0] if departure_city else "",
            arrival_city[0] if arrival_city else "",
            time_remaining
        ]
        with open(self.csv_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data)