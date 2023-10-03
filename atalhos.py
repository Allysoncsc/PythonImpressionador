



#comentar várias linhas = ctrl+;





cpf = 11233344
faturamento = 100000

print(f"Faturamento: {faturamento:.2f}")

print(f"Faturamento: R${faturamento:,.2f} ")

#completa os 11 diggitos com 0
print(f"CPF: {cpf:011}")

#procentagem
print(f"Top 5 representa {totaal_top5/sum(vendas):0.1%}")








#pegando os maiores e menores valores de uma lista
import heapq
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
aux = heapq.nlargest(5,vendas)
menores = heapq.nsmallest(3,vendas)
print(aux)





