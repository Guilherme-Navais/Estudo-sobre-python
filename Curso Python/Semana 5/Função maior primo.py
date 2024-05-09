def numero_primo(num):
    contador = num
    divide = num
    primo = True

    while divide != 2:
        divide = contador - 1
        contador = contador - 1
        if num % divide == 0:
            divide = 2
            primo = False
    return primo



def maior_primo(p):
    eh_numero_primo = []

    if p < 2:
        return "Digite um número válido"
    else:
       num = 2
       while num <= p:
            if numero_primo(num) == False:
               num = num +1
            else:
               eh_numero_primo = num
               num = num + 1
    
    return eh_numero_primo
               
        
           