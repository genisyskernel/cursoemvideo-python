from math import trunc
num = float(input("\033[1;35mDigite um número:\033[m "))

num_inteiro = trunc(num)

print("\033[1;31mO número\033[m \033[1;30m{0}\033[m \033[1;31mtem a parte inteira\033[m \033[1;30m{1}.\033[m".format(num, num_inteiro))
