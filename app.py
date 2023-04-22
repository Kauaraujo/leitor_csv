from csv import reader
import math
from time import sleep
from Models.pessoa import Pessoa
from typing import List


#/home/kaue/PraticaPython/dados.csv


registros = []  # cria uma lista vazia para armazenar os registros
feminino = 0 #Lista para guardar quantidade so sexo feminino
masculino = 0 #lista para guardar quantidade de masculino
idades = [] #lista para guardar as idades
alturas = [] #lista para guardar as alturas

pessoas: List[Pessoa] = []

caminho_arquivo = input('Informe o caminho do arquivo que deseja ler os dados:')

with open(caminho_arquivo) as arquivo:
    leitor = reader(arquivo)
    cabecalho = next(leitor)  # Lê e guarda o cabeçalho
    
    for linha in leitor:
            nome = linha[0]
            sexo = linha[1]
            idade = int(linha[2])
            altura = int(linha[3])
            pessoa = Pessoa(nome, sexo, idade, altura)
            pessoas.append(pessoa)
        
for dado in pessoas:
    idades.append(dado.idade)
    alturas.append(dado.altura)
    if dado.sexo == 'Feminino':
        feminino += 1
    else:
        masculino += 1



def main() -> None:
    menu_iniciar()

def menu_iniciar() -> None:
    print('=====================================')
    print('========= LEITOR DE .CSV ============')
    print('========= Projeto Pessoal ===========')
    print('=====================================')

    print('Selecione uma opção no menu: ')
    print('1 - Listar Pessoas')
    print('2 - Média dos dados')
    print('3 - Mediana dos dados')
    print('4 - Moda dos dados')
    print('5 - Desvio padrão dos dados')
    print('6 - Sair do sistema')
    sleep(1)

    opcao: int = int(input())

    if opcao == 1:
        listar_pessoas()
    elif opcao == 2:
        menu_media()
    elif opcao == 3:
        menu_mediana()
    elif opcao == 4:
        menu_moda()
    elif opcao == 5:
        desvio_dados()
    elif opcao == 6:
        print('Saindo do programa..')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(2)
        menu_iniciar()

def listar_pessoas():
    if len(pessoas) > 0:
        print('Listagem de Pessoas')

        for pessoa in pessoas:
            print(pessoa)
            print('--------------------')
            sleep(1)
    else:
        print('Não existem dados cadastrados.')
    sleep(2)
    menu_iniciar()

def menu_media():
    print('=====================================')
    print('========= LEITOR DE .CSV ============')
    print('========= Projeto Pessoal ===========')
    print('=====================================')

    print('Selecione uma opção no menu: ')
    print('1 - Média de Idades')
    print('2 - Média de Altura')

    opcao: int = int(input())

    if opcao == 1:
        media(idades)
    elif opcao == 2:
        media(alturas)
    else:
        print('Opção inválida')
        sleep(2)
        menu_iniciar()

def media(dados):
    med = sum(dados) / len(dados)
    if dado.idade in dados:
        print(f"A média de idades da lista é: {med:.2f}")
    else:
        print(f"A média de altura em CM da lista é: {med:.2f}")
    sleep(2)
    menu_iniciar()

def menu_mediana():
    print('=====================================')
    print('========= LEITOR DE .CSV ============')
    print('========= Projeto Pessoal ===========')
    print('=====================================')

    print('Selecione uma opção no menu: ')
    print('1 - Mediana de Idades')
    print('2 - Mediana de Altura')

    opcao: int = int(input())

    if opcao == 1:
        mediana(idades)
    elif opcao == 2:
        mediana(alturas)
    else:
        print('Opção inválida')
        sleep(2)
        menu_iniciar()

def mediana(dados):
    lista_ordenada = sorted(dados)
    tamanho_lista = len(lista_ordenada)
    indice_central = tamanho_lista // 2

    if tamanho_lista % 2 == 0:
        median = ((lista_ordenada[indice_central - 1]) + lista_ordenada[indice_central]) / 2
        print(f"A média de idades da lista é: {median:.2f}")
    else:
        median = lista_ordenada[indice_central]
        print(f"A média de idades da lista é: {median:.2f}")

def menu_moda():
    print('=====================================')
    print('========= LEITOR DE .CSV ============')
    print('========= Projeto Pessoal ===========')
    print('=====================================')

    print('Selecione uma opção no menu: ')
    print('1 - Moda da Idade')
    print('2 - Moda da Altura')

    opcao: int = int(input())

    if opcao == 1:
        moda(idades)
    elif opcao == 2:
        moda(alturas)
    else:
        print('Opção inválida')
        sleep(2)
        menu_iniciar()

def moda(dados):
    frequencias = {}

    for item in dados:
        if item in frequencias:
            frequencias[item] += 1
        else:
            frequencias[item] = 1
    
    moda = None
    frequencias_max = 0

    for item, frequencia in frequencias.items():
        if frequencia > frequencias_max:
            moda = item
            frequencias_max = frequencia
    if dado.idade in dados:
        print(f'A moda das idades é: {moda} anos')
    else:
        print(f'A moda das alturas é: {moda}cm')

def desvio_dados(lista):
    desvio_medio = []
    media = sum(lista) / len(lista)
    
    for num in lista:
        dado = num - media
        desvio_medio.append(dado)
    
    quadrado = [num ** 2 for num in desvio_medio]

    soma_desvios = (sum(quadrado) / len(lista)) - 1

    raiz_quadrada = math.sqrt(soma_desvios)

    return raiz_quadrada


if __name__ == '__main__':
    main()
