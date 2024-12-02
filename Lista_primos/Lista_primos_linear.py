# @author Arthurcapa

#Primeiro pegamos o input do usuário e validamos.
while True:
    print('Digite um número:')
    try:
        num = int(input())
    except:
        print('Erro, por favor use um número') #Exceção caso um caractere que não seja um número seja utilizado
        continue
    if num < 2:
        print('Erro, por favor use um número maior que 1') #Exceção caso um número menor que 2 seja utilizado
        continue
    break

#função para determinar se (numero) é primo
def is_primo(numero):
    for x in range(2, numero):
        if numero % x == 0:
            return False
        else:
            continue
    return True

#função para listar todos os números primos até (numero)
def lista_primos(numero):
    for x in range(2, numero+1):
        if is_primo(x) == True:
            print(x)
        else:
            continue

#invocação do método para listar todos os primos até (num)
print("Segue a lista de números primos:")
lista_primos(num)
