import requests
from config import API_KEY, API_SECRET

def obter_token(API_KEY, API_SECRET):
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        dados = response.json()
        print(f'{dados}')
        return dados["access_token"]
    else:
        print(f"Erro ao obter token: {response.status_code}")
        return None

token = obter_token(API_KEY, API_SECRET)
print(f"Token: {token}") 

