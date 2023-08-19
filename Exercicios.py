####  ####  ####  ##   #### #     #
   #  #__   #__   / #  #__   #   #
#  #  #     #    /  #  #      # #
 ##   ####  #    ###   ####    #


print("Seja bem vindo! esse é um exercício para aplicação do estudo em andamento")
nome = input(f"\nQuem fala?")
# print(nome)
profissao = input(f"\nSabe me dizer {nome} qual a sua Profissão?")
print(profissao)
print(f"\nQue legal, sabia que um {profissao} ganha bem?")
print(f"\nVamos ver quanto você ganha hoje e o imposto que paga sobre seu salário")
salario = float(input("Valor Salário:"))
imposto = float (input("Imposto:"))

if not imposto:
    imposto = float (27.5)
else: 
    imposto = float(imposto)
sal = salario - (salario*(imposto*0.01)) #observe que foi criada uma nova variavel para poder efetuar o calculo, chamada "sal"

print(sal)
#######
print("Vamos calcular novamente!")
def CalculoSalario():
    imposto = float (27.5)
    while imposto > 0.:
        imposto = input("Imposto ou (s) sair:")
        if not imposto:
            imposto = float (27.5)
        elif imposto == 's':
            break
        else:
            imposto = float(imposto)
        print("Valor Final: {0}".format(salario - (salario*imposto*0.01)))
salario = float(input("Valor Salario: "))
CalculoSalario()
print(f"\n Obrigado por utilizar o cálculo de imposto por este exercício")