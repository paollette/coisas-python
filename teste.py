# Variáveis - se autocompletam sem precisar serem declaradas

media = 0
n1 = n2 = n3 = n4 = 0.0
nome, idade = 'Alexandre', 5
estado = True

# Função Type() - retorna com o tipo de variável

print(type(n2))
print(type(media))
print(type(nome))
print(type(estado))
print(type(1+2j)) # Suporta matemática avançada

# Função isinstance() - retorna verdadeiro ou falso em uma consulta de variável

a = 10
b = 'Gio'
print(isinstance(b, int))
print(isinstance(b, (int, float)))
print(isinstance(b, int))

# Operações matemáticas nas variáveis

a = 40
b = 3
c = a * b
print(c)
