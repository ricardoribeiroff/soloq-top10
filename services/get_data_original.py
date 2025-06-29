import requests
import pandas as pd
import time
import os
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

# Lógica da transformação de dados

# Cria uma tabela e adiciona os valores requisitados enquanto trata alguns dados como winrate e posição. O usuario com a tagline foi tratado na saida da função buscar_nome_invocador
def transformar_top_n_players(lista_jogadores: list) -> pd.DataFrame:
    tabela = []

    for i, player in enumerate(lista_jogadores):
        puuid = player.get('puuid')
        nome = buscar_nome_invocador(puuid)
        time.sleep(1.2)  # Para evitar limite de requisições

        wins = player.get('wins', 0)
        losses = player.get('losses', 0)
        total = wins + losses
        winrate = f"{round((wins / total) * 100)}%" if total > 0 else "0%"

        tabela.append({
            "Posição": i + 1,
            "Invocador": nome,
            "Pontos (LP)": player.get("leaguePoints", 0),
            "Vitórias": wins,
            "Derrotas": losses,
            "Win Rate": winrate,
            "Hot Streak": "Sim" if player.get('hotStreak') else "Não"
        })
        
    return pd.DataFrame(tabela)

# Verifica se o arquivo SQLite já existe e cria um nome sequencial
def gerar_nome_banco(base_nome="riot_data.db"):
    if not os.path.exists(base_nome):
        return base_nome

    i = 2
    while os.path.exists(f"riot_data_{i}.db"):
        i += 1
    return f"riot_data_{i}.db"

# Execução
def exibir_tabela_top(endpoint_name: str, titulo: str, salvar_csv=False, salvar_db=True):
    lista = coletar_top_n_players(endpoint_name)
    tabela = transformar_top_n_players(lista)
    
    print(f"\n{titulo}\n", tabela)

    if salvar_csv:
        tabela.to_csv(f"{titulo.replace(' ', '_').lower()}.csv", index=False, encoding='utf-8-sig')

    if salvar_db:
        from sqlalchemy import create_engine
        engine = create_engine(f"sqlite:///riot_data_{data_hora_atual}.db")
        tabela.to_sql(titulo.replace(" ", "_").lower(), con=engine, if_exists='replace', index=False)




# Mostrar os Top 10
exibir_tabela_top('challengerleagues', "Top 10 Desafiante")
exibir_tabela_top('grandmasterleagues', "Top 10 Grão-Mestre")
exibir_tabela_top('masterleagues', "Top 10 Mestre")