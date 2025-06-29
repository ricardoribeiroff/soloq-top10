import os
from sqlalchemy import create_engine
from services.get_data import coletar_top_n_players, data_hora_atual
from services.normalize_data import transformar_top_n_players

# Garante que a pasta 'data' exista
os.makedirs("data", exist_ok=True)

# Execução
def exibir_tabela_top(endpoint_name: str, titulo: str, salvar_csv=False, salvar_db=True):
    lista = coletar_top_n_players(endpoint_name)
    tabela = transformar_top_n_players(lista)
    
    print(f"\n{titulo}\n", tabela)

    if salvar_csv:
        tabela.to_csv(f"data/{titulo.replace(' ', '_').lower()}.csv", index=False, encoding='utf-8-sig')

    if salvar_db:
        engine = create_engine(f"sqlite:///data/riot_data_{data_hora_atual}.db")
        tabela.to_sql(titulo.replace(" ", "_").lower(), con=engine, if_exists='replace', index=False)
