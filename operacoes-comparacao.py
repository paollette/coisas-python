x = y = z = False
n1 = n2 = 0

print("Digite um número: ")
n1 = int(input())
n2 = int(input('Digite outro número: '))

x = n1 == n2
print('Os valores são iguais? ', x,) # /n - quebra de linha

z = n1 > n2
print(n1, ' é maior que ', n2, "? ", z)

y = n1 != n2
print ('São diferentes?' + str(y))