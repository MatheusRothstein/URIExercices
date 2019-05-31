nome_vend = str(input())
fixo = float(input())
vendas = float(input())
porcentagem = 15
total = porcentagem / 100*vendas
total_salario = total + fixo
print("TOTAL = R$ %.2f"% total_salario)