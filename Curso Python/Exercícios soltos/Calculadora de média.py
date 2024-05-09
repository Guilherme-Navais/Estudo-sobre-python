quantidade_num = int(input("Quantos números você deseja inserir? "))
contador = 1
num = 0

while quantidade_num <= 0:
    print("Digite um valor válido.")

while contador <= quantidade_num:
    num_escrito = str(contador)
    valor = float(input("Digite o "+num_escrito+"º número: "))
    contador = contador + 1
    num = num + valor 

media = num/quantidade_num

print("\nA média dos números inseridos é: ",media)