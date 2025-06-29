import requests
import datetime
from sqlalchemy import create_engine

API_KEY = 'RGAPI-dd152143-a43f-4c44-ac75-96dfd6c5cc0f'
REGIAO = 'br1'
REGIAO_AMERICAS = 'americas'
QUEUE = 'RANKED_SOLO_5x5'
BASE_URL_LEAGUE = f'https://{REGIAO}.api.riotgames.com/lol/league/v4'
BASE_URL_ACCOUNT = f'https://{REGIAO_AMERICAS}.api.riotgames.com/riot/account/v1/accounts/by-puuid'

HEADERS = {'X-Riot-Token': API_KEY}

data_hora_atual = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

engine = create_engine('sqlite:///riot_data.db')

# Lógica da coleta de dados

# Coleta os dados dos jogadores com maior pontuação nos tiers Challenger, GrandMaster e Master
def coletar_top_n_players(endpoint_name: str, top_n: int = 10) -> list:
    url = f"{BASE_URL_LEAGUE}/{endpoint_name}/by-queue/{QUEUE}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    dados = resp.json()['entries']
    # Ordena por LP e retorna os top_n
    return sorted(dados, key=lambda x: x['leaguePoints'], reverse=True)[:top_n]

# Busca o nome e a tag line do jogador de acordo com o id coletado na função coletar_top_n_players
def buscar_nome_invocador(puuid: str) -> str:
    url = f"{BASE_URL_ACCOUNT}/{puuid}"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code == 200:
        data = resp.json()
        return f"{data.get('gameName', 'Desconhecido')} #{data.get('tagLine', '')}"
    else:
        return "Erro"