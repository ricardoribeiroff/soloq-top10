@echo off
REM Ativa o ambiente virtual
call D:\dev\riot_data\venv\Scripts\activate.bat

REM Vai para a pasta do projeto (por precaução)
cd /d D:\dev\riot_data

REM Executa o script Python
python main.py

REM Mantém a janela aberta após a execução
pause
