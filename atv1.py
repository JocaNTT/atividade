somatorio = 0
total_pares = 0

for contador in range(50,71):
  if contador % 2 == 0:
    somatorio += contador
    total_pares += 1

print(f'A soma dos pares é {somatorio}')
print(f'A média dos pares é {somatorio/total_pares}')
print(f'O total de valores pares é {total_pares}')