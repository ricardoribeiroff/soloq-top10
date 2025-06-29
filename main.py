from services.load_data import exibir_tabela_top

def main():
    # Executa o pipeline para as 3 ligas
    exibir_tabela_top('challengerleagues', "Top 10 Desafiante")
    exibir_tabela_top('grandmasterleagues', "Top 10 Grão-Mestre")
    exibir_tabela_top('masterleagues', "Top 10 Mestre")

if __name__ == "__main__":
    main()
