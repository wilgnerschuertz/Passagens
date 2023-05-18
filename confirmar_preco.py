import requests

def confirmar_preco():
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers/pricing"
    headers = {
        "Authorization": "Bearer nfG3BEny0AiTwXGaH7PyGv0ijKlZ",  # Substitua pelo seu token de acesso
        "Content-Type": "application/json"
    }

    payload = {
        "data": {
            "type": "flight-offers-pricing",
            "flightOffers": [
                {
                    "type": "flight-offer",
                    "id": "1",
                    "source": "GDS",
                    "instantTicketingRequired": False,
                    "nonHomogeneous": False,
                    "oneWay": False,
                    "lastTicketingDate": "2020-08-04",
                    "numberOfBookableSeats": 9,
                    "itineraries": [
                        {
                            "duration": "PT32H15M",
                            "segments": [
                                {
                                    "departure": {"iataCode": "SYD", "terminal": "1", "at": "2021-02-01T19:15:00"},
                                    "arrival": {"iataCode": "SIN", "terminal": "1", "at": "2021-02-02T00:30:00"},
                                    "carrierCode": "TR",
                                    "number": "13",
                                    "aircraft": {"code": "789"},
                                    "operating": {"carrierCode": "TR"},
                                    "duration": "PT8H15M",
                                    "id": "1",
                                    "numberOfStops": 0,
                                    "blacklistedInEU": False
                                },
                                {
                                    "departure": {"iataCode": "SIN", "terminal": "1", "at": "2021-02-02T22:05:00"},
                                    "arrival": {"iataCode": "DMK", "terminal": "1", "at": "2021-02-02T23:30:00"},
                                    "carrierCode": "TR",
                                    "number": "868",
                                    "aircraft": {"code": "788"},
                                    "operating": {"carrierCode": "TR"},
                                    "duration": "PT2H25M",
                                    "id": "2",
                                    "numberOfStops": 0,
                                    "blacklistedInEU": False
                                }
                            ]
                        },
                        {
                            "duration": "PT15H",
                            "segments": [
                                {
                                    "departure": {"iataCode": "DMK", "terminal": "1", "at": "2021-02-05T23:15:00"},
                                    "arrival": {"iataCode": "SIN", "terminal": "1", "at": "2021-02-06T02:50:00"},
                                    "carrierCode": "TR",
                                    "number": "867",
                                    "aircraft": {"code": "788"},
                                    "operating": {"carrierCode": "TR"},
                                    "duration": "PT2H35M",
                                    "id": "5",
                                    "numberOfStops": 0,
                                    "blacklistedInEU": False
                                },
                                {
                                    "departure": {"iataCode": "SIN", "terminal": "1", "at": "2021-02-06T06:55:00"},
                                    "arrival": {"iataCode": "SYD", "terminal": "1", "at": "2021-02-06T18:15:00"},
                                    "carrierCode": "TR",
                                    "number": "12",
                                    "aircraft": {"code": "789"},
                                    "operating": {"carrierCode": "TR"},
                                    "duration": "PT8H20M",
                                    "id": "6",
                                    "numberOfStops": 0,
                                    "blacklistedInEU": False
                                }
                            ]
                        }
                    ],
                    "price": {
                        "currency": "EUR",
                        "total": "546.70",
                        "base": "334.00",
                        "fees": [
                            {"amount": "0.00", "type": "SUPPLIER"},
                            {"amount": "0.00", "type": "TICKETING"}
                        ],
                        "grandTotal": "546.70"
                    },
                    "pricingOptions": {"fareType": ["PUBLISHED"], "includedCheckedBagsOnly": True},
                    "validatingAirlineCodes": ["HR"],
                    "travelerPricings": [
                        {
                            "travelerId": "1",
                            "fareOption": "STANDARD",
                            "travelerType": "ADULT",
                            "price": {"currency": "EUR", "total": "546.70", "base": "334.00"},
                            "fareDetailsBySegment": [
                                {
                                    "segmentId": "1",
                                    "cabin": "ECONOMY",
                                    "fareBasis": "O2TR24",
                                    "class": "O",
                                    "includedCheckedBags": {"weight": 20, "weightUnit": "KG"}
                                },
                                {
                                    "segmentId": "2",
                                    "cabin": "ECONOMY",
                                    "fareBasis": "O2TR24",
                                    "class": "O",
                                    "includedCheckedBags": {"weight": 20, "weightUnit": "KG"}
                                },
                                {
                                    "segmentId": "5",
                                    "cabin": "ECONOMY",
                                    "fareBasis": "X2TR24",
                                    "class": "X",
                                    "includedCheckedBags": {"weight": 20, "weightUnit": "KG"}
                                },
                                {
                                    "segmentId": "6",
                                    "cabin": "ECONOMY",
                                    "fareBasis": "H2TR24",
                                    "class": "H",
                                    "includedCheckedBags": {"weight": 20, "weightUnit": "KG"}
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        dados_resposta = response.json()
        # Processar os dados de resposta conforme necessário
        return dados_resposta
    else:
        print(f"Erro ao confirmar o preço: {response.status_code}")
        return None

# Exemplo de uso

dados_resposta = confirmar_preco()
if dados_resposta:
    # Processar os dados de resposta conforme necessário
    print(dados_resposta)
