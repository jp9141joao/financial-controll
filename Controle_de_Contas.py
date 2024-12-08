import os
import time

def Adicionar_Gasto(Saldo,Extrato,Gastos,Nome_Gasto,Valor_Gasto,Tipo_Gasto):

    if Tipo_Gasto == 1: 
        Extrato.append([Nome_Gasto,Valor_Gasto,'Essencial','Gasto'])
        Gastos.append([Nome_Gasto,Valor_Gasto,'Essencial','Gasto'])
    else:
        Extrato.append([Nome_Gasto,Valor_Gasto,'Superfluo','Gasto'])
        Gastos.append([Nome_Gasto,Valor_Gasto,'Superfluo','Gasto'])


def Adicionar_Ganho(Saldo,Extrato,Ganhos,Nome_Ganho,Valor_Ganho,Tipo_Ganho):

    if Tipo_Ganho == 1: 
        Extrato.append([Nome_Ganho,Valor_Ganho,'Constante','Ganho'])
        Ganhos.append([Nome_Ganho,Valor_Ganho,'Constante'])
    else:
        Extrato.append([Nome_Ganho,Valor_Ganho,'Inconstante','Ganho'])
        Ganhos.append([Nome_Ganho,Valor_Ganho,'Inconstante'])


def Mostrar_Gastos(Saldo,Extrato,Gastos):
    Tam = len(Gastos)
    Total = 0

    if Tam <= 0:
        print('Adicione pelo menos um gasto para poder ve-lo!')
        time.sleep(3)
        return
    
    print('* Tabela de Gastos *')

    for i in range(Tam):
        print(f'\n-----------------------------------\n\nNome: {Gastos[i][0]}\nNumero: {i+1}\nTipo de gasto: {Gastos[i][2]}\nValor: R${Gastos[i][1]}')
        Total += Gastos[i][1]

    print(f'\n-----------------------------------\n\nTotal de gastos: R${Total}')


def Mostrar_Ganhos(Saldo,Extrato,Ganhos):
    Tam = len(Ganhos)
    Total = 0
    
    if Tam <= 0:
        print('Adicione pelo menos um ganho para poder ve-lo!')
        time.sleep(3)
        return
    
    print('* Tabela de Ganhos *')

    for i in range(Tam):
        print(f'\n-----------------------------------\n\n\nNome: {Ganhos[i][0]}\nNumero: {i+1}\nTipo de gasto: {Ganhos[i][2]}\nValor: R${Ganhos[i][1]}')
        Total += Ganhos[i][1]

    print(f'\n-----------------------------------\n\nTotal de ganhos: R${Total}')

        
def Excluir_Gasto(Numero,Extrato,Gastos):
    Find = Extrato.index(Gastos[Numero-1])
    Extrato.pop(Find)
    Gastos.pop(Numero-1)


def Excluir_Ganho(Numero,Extrato,Ganhos):
    Find = Extrato.index(Ganhos[Numero-1])
    Extrato.pop(Find)
    Ganhos.pop(Numero-1)


def Mostrar_Extrato(Saldo,Extrato):
    Tam = len(Extrato)
    Total = 0

    print('* Extrato *')
    if Tam <= 0:
        print(f'\n-----------------------------------\n\nVazio\n\nSaldo: R${Saldo}\n-----------------------------------')
    else:
        for i in range(Tam):
            if Extrato[i][3] == 'Gasto':
                print(f'\n-----------------------------------\n\nGASTO\n\nNome: {Extrato[i][0]}\nTipo: {Extrato[i][2]}\nValor: -R${Extrato[i][1]}')
                Total -= Extrato[i][1]
            else:
                print(f'\n-----------------------------------\n\nGANHO\n\nNome: {Extrato[i][0]}\nTipo: {Extrato[i][2]}\nValor: +R${Extrato[i][1]}')
                Total += Extrato[i][1]

    print('\n-----------------------------------')

    print(f'Total do extrato: R${Total}\n\nSaldo: R${Saldo}')
        
    Voltar = int(input('\nDigite "1" voltar\nR: '))
    while Voltar != 1:
        Voltar = int(input('\nValor invalido! Digite "1" voltar\nR: '))


def Main():
    
    while True:
        
        os.system('cls')
        Verificador = input('\nDigite o saldo da sua conta\nR: ')
        Saldo = None
        
        Verificador = Verificador.replace(',','.')
            
        if (Verificador.isdigit()) or (Verificador.replace('.','').isdigit()) or (Verificador[0] == '-' and Verificador[1:].replace('.','').isdigit()): 
            Saldo = float(Verificador)          

        if Saldo is not None:
            break
        

    while True:
        os.system('cls')
        Verificador = input('\nSua conta possui credito\n1- Sim\n2- Não\nR: ')
        Confirmacao = None
        
        if Verificador.isdigit():
            Confirmacao = int(Verificador)

        if Confirmacao is not None:
            if Confirmacao == 1:
                while True:
                    os.system('cls')
                    Verificador = input('\nDigite o limite da sua conta\nR: ')
                    Credito = None
                    
                    Verificador = Verificador.replace(',','.')
                    
                    if (Verificador.isdigit()) or (Verificador.replace('.','').isdigit()) or (Verificador[0] == '-' and Verificador[1:].replace('.','').isdigit()): 
                        Credito = float(Verificador)
                        
                    if Credito is not None:
                        break
                
                Saldo += Credito
                Layout = f'\nSaldo + Credito: '
                break
            
            elif Confirmacao == 2:
                Layout = f'\nSaldo: '
                break
                        
    
    Extrato = []
    Gastos = []
    Ganhos = []

    while True:
        os.system('cls')
        Tam = len(Extrato)
        Menu = int(input(f'{Layout} R${Saldo}\n\n* Menu *\n1- Adicionar gastos\n2- Adicionar ganhos\n3- Mostrar gastos\n4- Mostrar ganhos\n5- Mostrar extrato\n6- Sair\nR: '))
        
        if Menu == 6:
            print('Programa Encerrado!')
            break
        
        elif Menu == 1:
            os.system('cls')
            Nome_Gasto = str(input('\nDigite o nome do gasto\nR: '))
            Valor_Gasto = float(input('\nDigite o valor do gasto\nR: '))
            while Valor_Gasto <= 0:
                Valor_Gasto = float(input('\nValor Invalido! Digite novamente o valor do gasto\nR: '))
            
            Tipo_Gasto = int(input('\nDefina se o gasto é \n1- Essencial (Aluguel, Combustivel, Plano de Saude,Comida, etc)\n2- Superfluos (Serviço de streaming, Delivery, Academia, Eventos sociais, etc)\nR: '))
            while Tipo_Gasto != 1 and Tipo_Gasto != 2:
                Tipo_Gasto = int(input('\nDefina se o gasto é \n1- Essencial (Aluguel, Combustivel, Plano de Saude,Comida, etc)\n2- Superfluo (Serviço de streaming, Delivery, Academia, Eventos sociais, etc)\nR: '))

            Saldo -= Valor_Gasto
            Adicionar_Gasto(Saldo,Extrato,Gastos,Nome_Gasto,Valor_Gasto,Tipo_Gasto)

            print('\nGasto adicionado!')
            Voltar = int(input('\nDigite "1" voltar\nR: '))
            while Voltar != 1:
                Voltar = int(input('\nValor invalido! Digite "1" voltar\nR: '))            

        elif Menu == 2:
            os.system('cls')
            Nome_Ganho = str(input('\nDigite o nome do ganho\nR: '))
            Valor_Ganho = float(input('\nDigite o valor do ganho\nR: '))
            while Valor_Ganho <= 0:
                Valor_Ganho = float(input('\nValor Invalido! Digite novamente o valor do ganho\nR: '))

            Tipo_Ganho = int(input('\nDefina se o ganho é \n1- Constante (Salario, Renda Passiva, etc)\n2- Inconstante (Investimentos, Horas extra, etc)\nR: '))
            while Tipo_Ganho != 1 and Tipo_Ganho != 2:
                Tipo_Ganho = int(input('\nDefina se o ganho é \n1- Constante (Salario, Renda Passiva, etc)\n2- Inconstante (Investimentos, Horas extra, etc)\nR: '))
            
            Saldo += Valor_Ganho
            Adicionar_Ganho(Saldo,Extrato,Ganhos,Nome_Ganho,Valor_Ganho,Tipo_Ganho)
            print('\nGanho adicionado!')

            Voltar = int(input('\nDigite "1" voltar\nR: '))
            while Voltar != 1:
                Voltar = int(input('\nValor invalido! Digite "1" voltar\nR: '))

        elif Menu == 3:
            os.system('cls')
            Mostrar_Gastos(Saldo,Extrato,Gastos)
            Excluir = int(input('\nDeseja excluir algum gasto\n1- Sim\n2- Não\nR: '))
            while Excluir != 1 and Excluir != 2:
                Excluir = int(input('\nValor invalido! Digite novamente se deseja excluir algum gasto\nR: '))

            if Excluir == 1:
                Numero = int(input('\nDigite o numero do gasto que deseja excluir\nR: '))
                while Numero > Tam or Numero <= 0:
                    Numero = int(input('\nNumero invalido! Digite novamente o numero do gasto que deseja excluir\nR: '))

                Saldo += Gastos[Numero-1][1]
                Excluir_Gasto(Numero,Extrato,Gastos)

                print('\nGasto excluido com sucesso!')
            
            Voltar = int(input('\nDigite "1" voltar\nR: '))
            while Voltar != 1:
                Voltar = int(input('\nValor invalido! Digite "1" voltar\nR: '))

        elif Menu == 4:
            os.system('cls')
            Mostrar_Ganhos(Saldo,Extrato,Ganhos)
            Excluir = int(input('\nDeseja excluir algum ganho\n1- Sim\n2- Não\nR: '))
            while Excluir != 1 and Excluir != 2:
                Excluir = int(input('\nValor invalido! Digite novamente se deseja excluir algum ganho\nR: '))

            if Excluir == 1:
                Numero = int(input('\nDigite o numero do ganho que deseja excluir\nR: '))
                while Numero > Tam or Numero <= 0:
                    Numero = int(input('\nNumero invalido! Digite novamente o numero do ganho que deseja excluir\nR: '))

                Saldo -= Ganhos[Numero-1][1]
                Excluir_Ganho(Numero,Extrato,Gastos)

                print('Ganho excluido com sucesso!')
            
            Voltar = int(input('\nDigite "1" voltar\nR: '))
            while Voltar != 1:
                Voltar = int(input('\nValor invalido! Digite "1" voltar\nR: '))

        elif Menu == 5:
            os.system('cls')
            Mostrar_Extrato(Saldo,Extrato)
        
        else:
            os.system('cls')
            print('\nOpção Invalida!')
            Continuar = int(input('\nDeseja continuar\n1- Sim\n2- Não\nR: '))
            while Continuar != 1 and Continuar != 2:
                Continuar = int(input('\nOpção Invalida!\nDeseja continuar\n1- Sim\n2- Não\nR: '))

            if Continuar == 2:
                print('Programa Encerrado!')
                break


Main()