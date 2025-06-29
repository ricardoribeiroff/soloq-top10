# TOP 10 - Solo Queue Ranking (League of Legends)

ETL que coleta o top 10 da Solo Queue de League of Legends brasileira e retorna os valores em um arquivo .db (sqlite).

A coleta é feita nos elos Desafiante, Grão-Mestre e Mestre.

## Tecnologias utilizadas
- Pandas
- SQLAlchemy

## Como utilizar

Crie um ambiente virtual
```bash
python -m venv venv
```

Ative o venv
```bash
> .\venv\Scripts\activate
```

Instale as dependencias
```bash
pip install -r requirements.txt
```

Execute o script main.py
```bash
python main.py
```

Os dados serão salvos em um arquivo .db com o nome riot_data_YYYYMMDD_HHMMSS no diretório ".\data".

