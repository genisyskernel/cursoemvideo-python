# ANSI escape sequence - Code: \033[ STYLE_TEXT + TEXT_COLOR + BACKGROUND_COLOR m \033[m
# STYLE_TEXT CODES
# 0 = None
# 1 = Bold ( Negrito )
# 4 = Underline ( Sublinhado )
# 7 = Invert ( Inverte os estilos/cores )
##########################################################
# TEXT_COLOR CODES
# 30 = White ( Branco )
# 31 = Red ( Vermelho )
# 32 = Green ( Verde )
# 33 = Yellow ( Amarelo )
# 34 = Blue ( Azul )
# 35 = Purple ( Roxo )
# 36 = Cyan ( Ciano )
# 37 = Gray ( Cinza )
##########################################################
# BACKGROUND_COLOR CODES
# 40 = White ( Branco )
# 41 = Red ( Vermelho )
# 42 = Green ( Verde )
# 43 = Yellow ( Amarelo )
# 44 = Blue ( Azul )
# 45 = Purple ( Roxo )
# 46 = Cyan ( Ciano )
# 47 = Gray ( Cinza )

#print("\033[0;30;41mTeste\033[m")
#print("\033[4;33;44mTeste\033[m")
#print("\033[1;35;43mTeste\033[m")
#print("\033[30;42mTeste\033[m")
#print("\033[mTeste\033[m")
#print("\033[7;30mTeste\033[m")

#print("\033[7;31;42mHello, World!\033[m")

cores = {"clear":"\033[m", "red":"\033[31m", "blue":"\033[34m"}

nome = "Eduardo"
print("\033[1;30mPrazer em te conhecer,\033[m {0}{1}{2}!!!".format(cores["blue"], nome, cores["clear"]))
