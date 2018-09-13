
import datetime as dt

mes = int(input("Digite o mês de seu nascimento: "))
ano = int(input("Digite o ano de seu nascimento: "))

today = dt.datetime.now()
#print(today.year)
idade_anos = today.year - ano
print("Sua idade é:", idade_anos)