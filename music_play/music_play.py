import pygame
import os

os.system("python /home/pi/webapps/music_play/test.py")

path = "/home/pi/music_list/"
music_list = os.listdir(path)
# init
pygame.mixer.init()
# os.system("d")
for music in music_list:
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.load(path + music)
    pygame.mixer.music.play()

    f = open("id_saver.txt", "w")
    f.write(str(os.getpid()))
    f.close()

    while pygame.mixer.music.get_busy() == True:
        continue

