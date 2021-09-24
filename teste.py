total_casos = int(input())
while total_casos > 0:
    i = 0
    numero = []
    troca = 0
    n = 0
    while i < total_casos:
        sms = int(input())
        numero.append(sms)
        i+=1

    while n < len(numero)-1:
         if numero[n] < numero[n + 1]:
            troca+=1
         n+=1
    print(troca)
    total = 0
    print(total)