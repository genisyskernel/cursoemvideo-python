from math import sqrt
import emoji
num = int(input("Digite um número: "))
raiz = sqrt(num)
print("A raiz do número {0} é {1:.2f}.".format(num, raiz))
print(emoji.emojize("Hello World! :earth_americas:", use_aliases=True))
