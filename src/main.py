
import datetime
import requests
import csv
from src.config import TOKEN


def buscar_voo(local_partida, local_chegada, data_inicial, data_final):
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {"Authorization": "Bearer {TOKEN}"} 

    data_inicial = datetime.datetime.strptime(data_inicial, "%Y-%m-%d")
    data_final = datetime.datetime.strptime(data_final, "%Y-%m-%d")

    with open('voos.csv', 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(["ID", "Source", "Price", "Currency", "Carrier", "Departure Date", "Return Date", "Stops", "Flight Numbers", "Stations", "Departure Times", "Arrival Times"])

        for i in range(4): 
            parametros = {
                "originLocationCode": local_partida,
                "destinationLocationCode": local_chegada,
                "departureDate": (data_inicial + datetime.timedelta(days=i)).strftime("%Y-%m-%d"),
                "returnDate": (data_final + datetime.timedelta(days=i)).strftime("%Y-%m-%d"),
                "adults": 1,
                "currencyCode": "BRL",
            }

            response = requests.get(url, headers=headers, params=parametros)
            print(f'{response}')

            if response.status_code == 200:
                dados = response.json()
                print(dados['data'][1])
                for oferta in dados['data']:
                    carrier_code = oferta['itineraries'][0]['segments'][0]['carrierCode']
                    carrier_name = dados['dictionaries']['carriers'].get(carrier_code, 'Unknown')

                    stops = len(oferta['itineraries'][0]['segments']) - 1 
                    flight_numbers = ", ".join(seg['number'] for seg in oferta['itineraries'][0]['segments'])  

                    stations = ", ".join([seg['departure']['iataCode'] for seg in oferta['itineraries'][0]['segments']])  
                    departure_times = ", ".join([seg['departure']['at'] for seg in oferta['itineraries'][0]['segments']]) 
                    arrival_times = ", ".join([seg['arrival']['at'] for seg in oferta['itineraries'][1]['segments']]) 

                    writer.writerow([oferta['id'], oferta['source'], oferta['price']['total'], oferta['price']['currency'], carrier_name, parametros['departureDate'], parametros['returnDate'], stops, flight_numbers, stations, departure_times, arrival_times])
            else:
                print(f"Erro ao buscar voos: {response.status_code}")


buscar_voo("BVB", "MGF", "2023-06-09", "2023-06-20") 
