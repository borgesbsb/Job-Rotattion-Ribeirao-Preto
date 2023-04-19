opcao = input("Deseja informar uma string? (s/n)")

if opcao.lower() == 's':
    string = input("Informe a string: ")
else:
    string = "desafio" 


lista_chars = list(string)


for i in range(len(lista_chars)//2):
    temp = lista_chars[i]
    lista_chars[i] = lista_chars[len(lista_chars)-1-i]
    lista_chars[len(lista_chars)-1-i] = temp


string_invertida = ''.join(lista_chars)

print(string_invertida)