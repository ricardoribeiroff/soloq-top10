import pandas as pd
import time
from sqlalchemy import create_engine
from services.get_data import buscar_nome_invocador

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
