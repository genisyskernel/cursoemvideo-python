from pygame import mixer

caminho_mp3 = "../resources/a_to_the_o.mp3"

mixer.init()
mixer.music.load(caminho_mp3)
mixer.music.play()
sair = str(input("\033[4;31mDigite qualquer coisa para sair...\033[m"))


