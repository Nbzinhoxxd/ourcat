import os

def renomear_arquivos():
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    arquivos = sorted(os.listdir(pasta_atual))
    
    contador = 1

    for arquivo in arquivos:
        if arquivo.lower().endswith(".jpeg"):
            novo_nome = f"gatinha_{contador}.jpg"
            caminho_antigo = os.path.join(pasta_atual, arquivo)
            caminho_novo = os.path.join(pasta_atual, novo_nome)

            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado: {arquivo} -> {novo_nome}")
            contador += 1

if __name__ == "__main__":
    renomear_arquivos()
