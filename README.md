# 🏆 **TOP 10 - Solo Queue Ranking (League of Legends Brasil)**

🎮 Projeto **ETL** que coleta os **Top 10 jogadores** da **Solo Queue brasileira** de *League of Legends* diretamente dos tiers:

> 🥇 Desafiante • 🥈 Grão-Mestre • 🥉 Mestre

Os dados são extraídos, transformados e armazenados automaticamente em um banco de dados SQLite (`.db`) com carimbo de data e hora. Ideal para análises, dashboards ou estudos sobre o cenário competitivo.

---

## 🚀 Tecnologias Utilizadas

- 🐼 [Pandas](https://pandas.pydata.org/) – manipulação e tratamento de dados  
- 🛠️ [SQLAlchemy](https://www.sqlalchemy.org/) – ORM para persistência no banco de dados SQLite  
- 🌐 [Riot Games API](https://developer.riotgames.com/) – dados em tempo real do LoL

---

## ⚙️ Como Utilizar

1. 🔹 **Clone o repositório**:
   ```bash
   git clone https://github.com/ricardoribeiroff/soloq-top10.git
   cd soloq-top10
   ```

2. 🔹 **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   ```

3. 🔹 **Ative o ambiente**:

   - No **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

   - No **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```

4. 🔹 **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. 🔹 **Execute o script**:
   ```bash
   python main.py
   ```

📦 Ao finalizar, um arquivo `.db` será gerado no diretório `./data` com o nome:  
```text
riot_data_YYYYMMDD_HHMMSS.db
```

---

## 📁 Estrutura do Projeto

```
📦 soloqueue-top10
 ┣ 📁 data                # Arquivos .db gerados automaticamente
 ┣ 📁 services            # Funções de coleta e transformação de dados
 ┣ 📜 main.py             # Script principal
 ┣ 📜 requirements.txt    # Dependências do projeto
 ┗ 📜 README.md
```

---

## 📌 To-Do & Melhorias Futuras

- [x] Exportar para `.csv` ou `.json`
- [x] Automatizar agendamentos com cron/task scheduler
- [ ] Visualizações com gráficos interativos
- [ ] Deploy com Streamlit ou FastAPI


Se curtir o projeto, deixe uma ⭐ e compartilhe!  
**GLHF! 🧙‍♂️**
