# ### SEM POO - Programação Orientada a Objetos

# cor = "preto"
# modelo = "civic"

# def acelerar():
#     print("O carro acelerou")

# print(cor)
# print(modelo)
# acelerar()

## Com Progrmamação Orientada a Objetos
# class Carro:
#     def __init__(self, cor, modelo):
#         self.cor = cor
#         self.modelo = modelo

#     def acelerar(self):
#         print("O carro acelerou")

# carro1 = Carro("preto", "civic")
# carro2 = Carro("vermelho", "gol")
# print(carro1.cor)
# print(carro1.modelo)
# print(carro2.cor)   
# print(carro2.modelo)


# carro1.acelerar()
# carro2.acelerar()

##Atividade

# class conta:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo

#     def depositar(self, valor):
#         self.saldo += valor 
#         print("Deposito realizado")
#     def sacar(self, valor):
#         self.saldo -= valor
#         print("Saque realizado")

#     def mostrar_saldo(self):
#         print(f"Saldo atual: {self.saldo}")

# conta1 = conta("fulano", 1000)
# print(conta1.titular)
# conta1.depositar(500) 
# conta1.sacar(200)
# conta1.mostrar_saldo() 

#Atividade 2
# class Produto:
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self.preco = preco 

#     def exibiir_dados(self):
#         print(f"Produto: {self.nome}")
#         print(f"Valor: R${self.preco}")

# produto1 = Produto("Camiseta", 50)
# produto1.exibiir_dados()

##Atividaede 3
def verificar_situcao(self):
   media = calcular_media(self.notas)
   
   if media >= 7:
         return "Aprovado"
   elif media >= 5:
         return "Recuperação"   
   else:
         return "Reprovado"
   