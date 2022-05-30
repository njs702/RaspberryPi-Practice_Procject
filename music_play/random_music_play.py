import pygame
import os
import random

os.system("python /home/pi/webapps/music_play/stop_music.py")

path = "/home/pi/music_list/"
music_list = os.listdir(path)
numbers = [i for i in range(len(music_list))]
random.shuffle(numbers)
# init
pygame.mixer.init()

for i in range(len(music_list)):
    file_path = "/home/pi/id_saver.txt"

    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.load(path + music_list[numbers[i]])
    pygame.mixer.music.play()

    f = open(file_path, "w")
    f.write(str(os.getpid()))
    f.close()

    while pygame.mixer.music.get_busy() == True:
        continue
