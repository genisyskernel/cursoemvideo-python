n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1 // n2
e = n1 ** n2

print("A soma e {0}, o produto e {1} e a divisao e {2}!".format(s, m, d), end="\n")
print("Divisao inteira {0} e potencia {1}!".format(di, e))
