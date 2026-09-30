from PIL import Image

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

janela = Tk ()
janela.withdraw()

caminho_imagem = askopenfilename(title= "Selecione uma imagem:")
caminho = askdirectory(title = "Escolha onde as imagens serão salvas:")

imagem = Image.open(caminho_imagem)

numero = 1

print("Você deseja que sua folha esteja em modo 'paisagem' ou 'retrato'?")

print("1 - Paisagem\n2- Retrato")

formato = int(input(""))

nome = input("Digite o nome das imagem que serão salvas: ")

if formato == 1:
    imagem_rodar = imagem.rotate(90)
    largura, altura = imagem_rodar.size

    folha_altura = int(input("Quantas folhas deseja de altura?: "))
    folha_largura = int(input("Quantas folhas deseja de largura?: "))

    largura_do_pedaco = largura / folha_largura
    altura_do_pedaco =  altura / folha_altura

    for y in range(folha_altura):
        for x in range(folha_largura):
            esquerda = x*largura_do_pedaco
            cima = y*altura_do_pedaco
            baixo = cima+altura_do_pedaco
            direita = esquerda+largura_do_pedaco

            cortado = imagem_rodar.crop((esquerda, cima, direita, baixo))

            cortado.save(f"{caminho}/{nome}_{numero}.png")

            numero+=1
elif formato == 2:
    largura, altura = imagem.size

    folha_altura = int(input("Quantas folhas deseja de altura?: "))
    folha_largura = int(input("Quantas folhas deseja de largura?: "))

    largura_do_pedaco = largura / folha_largura
    altura_do_pedaco = altura / folha_altura

    for y in range(folha_altura):
        for x in range(folha_largura):
            esquerda = x*largura_do_pedaco
            cima = y*altura_do_pedaco
            baixo = cima+altura_do_pedaco
            direita = esquerda+largura_do_pedaco

            cortado = imagem.crop((esquerda, cima, direita, baixo))

            cortado.save(f"{caminho}/{nome}_{numero}.png")

            numero+=1
else:
    print("O número selecionado pelo usuário não está nas opções")