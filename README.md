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

## 🖥️ Agendamento de Tarefa no Windows (com `run_script.bat`)

Você pode automatizar a coleta de dados criando uma tarefa agendada no Windows usando o arquivo `run_script.bat`:

### 📄 Exemplo de conteúdo do `run_script.bat`

```bat
@echo off
REM --------------------------------------------------------
REM Script para ativar o ambiente virtual e executar o script Python
REM --------------------------------------------------------

REM === PASSO 1: Ativar o ambiente virtual ===
REM Substitua pelo caminho real do seu ambiente virtual
call C:\CAMINHO\PARA\SUA\venv\Scripts\activate.bat

REM === PASSO 2: Ir até a pasta do projeto ===
cd /d C:\CAMINHO\PARA\SEU\PROJETO

REM === PASSO 3: Executar o script desejado ===
python main.py

REM === PASSO 4: (Opcional) Manter a janela aberta após execução
pause
```

### 🛠️ Como agendar no Windows

1. Abra o **Agendador de Tarefas** (`taskschd.msc`)
2. Clique em **Criar Tarefa...**
3. Na aba **Geral**:
   - Dê um nome como: `Atualizar TOP 10 Solo Queue`
   - Marque "Executar com privilégios mais altos"
4. Na aba **Disparadores** (_Triggers_):
   - Adicione um novo disparador: diariamente, ou no horário que preferir
5. Na aba **Ações**:
   - Ação: Iniciar um programa
   - Programa/script: `run_script.bat` (coloque o caminho completo)
6. Na aba **Condições** e **Configurações**, ajuste conforme necessário

> ✅ Certifique-se de que o caminho no `.bat` esteja correto com seu ambiente e pastas locais.

Pronto! Agora sua coleta será executada automaticamente nos horários definidos.

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
