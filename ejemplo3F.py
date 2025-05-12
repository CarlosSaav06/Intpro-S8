#ahora que imprima el cubo de cada uno de esos numeros, y que llegue hasta la linea 10

for i in range(1, 11):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)
        print("El cubo de", i, "es", i ** 3)
        print("El cubo de", j, "es", j ** 3)