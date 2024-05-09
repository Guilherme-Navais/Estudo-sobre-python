segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos//86400
segundos_restantes1 = segundos%86400
horas = segundos_restantes1//3600
segundos_restantes2 = segundos_restantes1%3600
minutos = segundos_restantes2//60
segundos_restantes_final = segundos_restantes2%60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos_restantes_final,"segundos.")

