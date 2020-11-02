num = int(input("\033[1;31mDigite um numero: \033[m"))

print("\033[7;30mDobro: {}\033[m".format(num*2))
print("\033[1;34mTriplo: {}\033[m".format(num*3))
print("\033[1;32mRaiz quadrada: {:.2f}\033[m".format(num**(1/2)))
