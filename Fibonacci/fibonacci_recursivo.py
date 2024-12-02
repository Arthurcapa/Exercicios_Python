# @author Arthurcapa

#Primeiro pegamos o input do usuário e validamos.
while True:
    print('Digite um número:')
    try:
        num = int(input())
    except:
        print('Erro, por favor use um número') #Exceção caso um caractere que não seja um número seja utilizado
        continue
    if num < 0:
        print('Erro, por favor use um número positivo') #Exceção caso um número negativo seja utilizado
        continue
    break

#função que pega um número x e retorna o valor da sequencia fibonacci na
#posição x
def fib(numero_fib):
    if numero_fib == 0: #se for 0 retorna-se 0
        return 0

    if numero_fib == 1: #se for 1 retorna-se 1
        return 1

    return fib(numero_fib-2)+fib(numero_fib-1)

print(fib(num))