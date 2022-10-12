"""/*******************************************************************
Autor: Sival Leão de Jesus
Concluído em: xx/xx/xxxx
Declaro que este código foi elaborado por mim de forma individual e não contém
nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
**********************************************************************/"""

#codigo fonte do "import os": https://github.com/python/cpython/tree/3.10/Lib/os.py
import os
from random import randint

def pausar():
    pausa = input("\n\n\nPress Enter para continuar ")

def faxineira():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def iniciar(dic, endereco_py):
    with open("Campeao.txt", "w", encoding="utf-8") as save:
        save.write(str(dic))

def adicionar_save(dic, endereco_py):
    #funcao usada para criar e abrir os arquivos txt para funcionamento do software, assim que o programa inicia
    #verificando se o arquivo existe
    if os.path.isfile("Campeao.txt"):
        #se existir, abre o arquivo
        with open("Campeao.txt", "r",encoding="utf-8") as abrir:
            dic = abrir.read()
            dic = eval(dic)
        return dic
    else:
        #se nao existir, cria um arquivo
        with open("Campeao.txt", "w",encoding="utf-8") as save:
            save.write(str(dic))

def verificar_termo(dic,termo):
    #verifica se o termo existe em algum documento
    tem = ""
    for i in dic:
        if termo in dic[i]:
            tem = "sim"
    if tem == "sim":
        return True
    else:
        False

def add_classe(Herois,todos, assassinos, lutadores, magos, atiradores, suportes, tanques):
    for Camps, valor in Herois.items():
        todos.append(Camps)
        for classe in Herois[Camps]:
            if classe == "assassinos":
                assassinos.append(Camps)
            elif classe == "lutadores":
                lutadores.append(Camps)
            elif classe == "magos":
                magos.append(Camps)
            elif classe == "atiradores":
                atiradores.append(Camps)
            elif classe == "suportes":
                suportes.append(Camps)
            elif classe == "tanques":
                tanques.append(Camps)

def atualizar_lista(dic):
    with open("Campeao.txt", "w",encoding="utf-8") as save:
            save.write(str(dic))     
    add_classe(Herois,todos, assassinos, lutadores, magos, atiradores, suportes, tanques)

def sorteio(lista , quant):
    faxineira()
    repeti = []
    tamanho = len(lista)
    print("O(s) campeão(ões) soerteado(s) é:\n")
    for i in range(quant):
        aleatorio = randint(0 ,tamanho - 1)
        if aleatorio in repeti:
            i = i-1
        else:
            repeti.append(aleatorio)
            print(lista[aleatorio])

    pausar()

def exibir(lista):
    cont = 1
    for i in (lista):
        print(f"{cont} -> {i}")
        cont += 1

    pausar()

def quant_sorteio():
    faxineira()
    ativo = 0
    while ativo ==0:
        faxineira()
        print("Quantos campeões deseja sortear")
        x = input("(1) Normal\n(2) Duo\n(3) Trio\n(4) Squad\n(5) Full\n")

        if x == "1":
            
            ativo = 1
            return 1
        elif x == "2":
            return 2
            ativo = 1

        elif x == "3":
            return 3
            ativo = 1

        elif x == "4":
            return 4
            ativo = 1

        elif x == "5":
            return 5
            ativo = 1

        else:
            ativo =0
                 

#=================================PRINCIPAL======================#

faxineira()
#buscar endereco onde o codigo esta localizado
endereco_py = os.getcwd()
#dicionario save
"""catalogaram os personagens
Sival & Gustavo"""

Herois = {
"ahri":["magos", "assassinos"], 
"akali":["assassinos"], 
"akshan":["atiradores", "assassinos"],
"alistar":["tanques","suportes"],
"amumu":["tanques"],
"annie":["magos", "suportes"],
"ashe":["atiradores", "suportes"],
"aurelion sol":["magos"],
"blitzcrank":["tanques", "suportes"],
"brand":["magos"],
"braum":["suportes", "tanques"],
"caitlyn":["atiradores"],
"camille":["lutadores"],
"corki":["atiradores"],
"darius":["lutadores"],
"diana":["lutadores", "magos"],
"dr. mundo":["lutadores", "tanques"],
"draven":["atiradores"],
"ekko":["assassinos", "magos"],
"evelynn":["assassinos"],
"ezreal":["atiradores", "magos"],
"fiora":["lutadores","assassinos"],
"fizz":["assassinos","magos"],
"galio":["tanques","magos"],
"garen":["lutadores","tanques"],
"gragas":["tanques","magos"], 
"graves":["atiradores","lutadores"],
"irelia":["lutadores","assassinos"],
"janna":["suportes","magos"],
"jarvan iv":["tanques","lutadores"],
"jax":["lutadores"],
"jayce":["lutadores","atiradores"],
"jhin":["atiradores", "magos"],
"jinx":["atiradores"],
"kai´sa":["atiradores", "assassinos"],
"karma":["magos","suportes"],
"Kassadin":["assassinos", "magos"],
"katarina":["assassinos","magos"],
"kayle":["lutadores", "suportes"],
"kennen":["magos", "atiradores"],
"kha´zix":["assassinos", "lutadores"],
"lee sin":["lutadores", "assassinos"],
"leona":["tanques", "suportes"],
"lucian":["atiradores"],
"lulu":["suportes", "magos"],
"lux":["magos", "suportes"],
"malphite":["tanques"],
"master yi":["assassinos", "lutadores"],
"miss fortune":["atiradores", "magos"],
"morgana":["magos", "suportes"],
"nami":["suportes", "magos"],
"nasus":["lutadores", "tanques"],
"nautilus":["tanques","suportes"],
"nunu e willump":["tanques", "magos"],
"olaf":["lutadores"],
"orianna":["magos", "suportes"],
"pantheon":["lutadores", "assassinos"],
"pyke":["assassinos", "suportes"],
"rakan":["suportes", "tanques"],
"rammus":["tanques"],
"renekton":["lutadores"],
"rengar":["assassinos"],
"riven":["lutadores", "assassinos"],
"senna":["atiradores", "suportes"],
"seraphine":["magos","suportes"],
"sett":["lutadores"],
"shen":["tanques", "suportes"],
"shyvana":["lutadores", "tanques"],
"singed":["tanques", "magos"],
"sona":["suportes", "magos"],
"soraka":["suportes", "magos"],
"teemo":["atiradores", "magos"],
"thresh":["tanques"],
"tristana":["atiradores"],
"tryndamere":["lutadores"],
"twisted fate":["magos", "atiradores"],
"varus":["atiradores", "magos"],
"vayne":["atiradores", "assassinos"],
"veigar":["magos"],
"vi":["lutadores"],
"wukong":["lutadores", "tanques"],
"xayah":["atiradores", "magos"],
"xin zhao":["lutadores", "tanques"],
"yasuo":["lutadores","assassinos"],
"yuumi":["suportes", "magos"],
"zed":["assassinos"],
"ziggs":["magos"], 

"Shion":["tanques","lutadores"], 
"samira": ["atiradores", "assassinos"], 
"yone": ["assassinos"],
"gwen": ["lutadores"]
}

#classes
todos = []
assassinos = []
lutadores = []
magos = []
atiradores = []
suportes = []
tanques = []
#
clases = ["assassinos", "lutadores", "magos", "atiradores", "suportes", "tanques"]
ADD = []

#atualizando dicionario
if adicionar_save(Herois,endereco_py) != None:
    Herois = adicionar_save(Herois,endereco_py)
    iniciar(Herois,endereco_py)
add_classe(Herois, todos, assassinos, lutadores, magos, atiradores, suportes, tanques)


#Iniciando codigo
#MENU

on = 1
while on == 1:
    faxineira()
    print("=-" * 5 + "MENU" + "-=" * 5 + "\n")
    menu = input("(1) Sortear campeão\n(2) Adicionar novo campeão\n(3) Mostra campeões salvos\n(4) Sair\n>>> ")

    if menu == "1":
        faxineira()
        sort = 1
        while sort == 1:
            faxineira()
            print("=-" * 5 + "SORTEAR" + "-=" * 5 + "\n")
            escolha = input("(1) Todos\n(2) Assassinos\n(3) lutadores\n(4) Magos\n(5) Atiradores\n(6) suportes\n(7) Tanques\n(8) Voltar ao menu\n>>> ")
            faxineira()
            quantidade = quant_sorteio()
            if escolha == "1":
                
                sorteio(todos, quantidade)
                sort += 1
            elif escolha == "2":
                
                sorteio(assassinos, quantidade)
                sort += 1
            elif escolha == "3":
                
                sorteio(lutadores, quantidade)
                sort += 1
            elif escolha == "4":
                sorteio(magos,quantidade)
                
                sort += 1
            elif escolha == "5":
                
                sorteio(atiradores,quantidade)
                sort += 1
            elif escolha == "6":
                
                sorteio(suportes,quantidade)
                sort += 1
            elif escolha == "7":
                
                sorteio(tanques,quantidade)
                sort += 1
            elif escolha == "8":
                
                sort += 1
            else:
                sort = 1
    
    elif menu == "2":
        faxineira()
        add_novo = 1
        while add_novo == 1:
            escolha_add = input("(1) Adicionar\n(2) Sair\n>>> ")
            if escolha_add == "1":
                faxineira()
                novoCamp = input("Escreva coretamente o nome do campeão: ").lower()
                
                
                if novoCamp in todos:
                    faxineira()
                    print("Este campeãos ja existe na lista")
                    pausar()
                    faxineira()

                else:
                    
                    for i in clases:
                        sim = 1
                        while sim == 1:
                            faxineira()
                            SN = input(f"O campeão {novoCamp} pertece a classe: {i}\n\n(1) Sim\n(2) Não\n>>> ")

                            if SN == "1":
                                ADD.append(i)
                                sim = 0

                            elif SN == "2":
                                sim = 0 
                            
                            else:
                                faxineira()
                                print("Resposta invalida")
                                sim = 1
                                pausar()
                                faxineira()
                    
                        add_novo += 1
        
                Herois[novoCamp] = ADD
                atualizar_lista(Herois)
                ADD = []
            
            elif escolha_add == "2":
                add_novo += 1
            
            else:
                faxineira()
                print("Resposta invalida")
                add_novo = 1
                pausar()
                faxineira()


    elif menu == "3":

        faxineira()
        mostra = 1
        while mostra == 1:
            faxineira()
            print("=-" * 5 + "SORTEAR" + "-=" * 5 + "\n")
            escolha = input("(1) Todos\n(2) Assassinos\n(3) lutadores\n(4) Magos\n(5) Atiradores\n(6) suportes\n(7) Tanques\n(8) Voltar ao menu\n>>> ")
            faxineira()

            if escolha == "1":
                exibir(todos)
                mostra += 1
            elif escolha == "2":
                exibir(assassinos)
                mostra += 1
            elif escolha == "3":
                exibir(lutadores)
                mostra += 1
            elif escolha == "4":
                exibir(magos)
                mostra += 1
            elif escolha == "5":
                exibir(atiradores)
                mostra += 1
            elif escolha == "6":
                exibir(suportes)
                mostra += 1
            elif escolha == "7":
                exibir(tanques)
                mostra += 1
            elif escolha == "8":
                mostra += 1
            else:
                mostra = 1
    


    elif menu == "4":
        on += 1


                    
print("Oi")
#vamos ver

#@hdfkh
