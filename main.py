import os
from tkinter.filedialog import askdirectory

# Abre um Pop-Up solicitando ao usuário o diretório onde quer a execução do algoritmo para organizar os arquivos
caminho = askdirectory(title="Selecione uma pasta")

# Guarda todos os arquivos dentro do diretório que passamos
lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

locais = {
    #nomeDaPasta : Extensões
    "Imagens" : [".png", ".jpg"],
    "Planilhas" : [".csv", ".xlsx"],
    "Videos" : [".mp3", ".mp4", ".mov"],
    "PDFs" : [".pdf"]
}

# Para cada arquivos dentro de lista de arquivos
for arquivo in lista_arquivos:
    # Usando o método splithtext, irá separar o nome do arquivo e sua extensão
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")

    for pasta in locais:
        if extensao in locais[pasta]:
            
            # se o caminho não existir
            if not os.path.exists(f"{caminho}/{pasta}"):
                # Cria o caminho
                os.mkdir(f"{caminho}/{pasta}")
            
            # Com a pasta existindo, iremos mudar o caminho. Antes downloads/arquivos  ==> downloads/pasta/arquivos
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
