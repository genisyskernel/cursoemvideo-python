c = float(input("\033[7;31;40mInforme a temperatura em celsios: \033[m"))

f = c * 9 / 5 + 32 # 0°C × 9/5 + 32 = 32°F

print("\033[7;37;44mA temperatura\033[m \033[7;35;43m{0:.2f}\033[m \033[7;37;44mgraus celsios corresponde a\033[m \033[7;35;43m{1:.2f}\033[m \033[7;37;44mgraus fahrenheit.\033[m".format(c, f))
