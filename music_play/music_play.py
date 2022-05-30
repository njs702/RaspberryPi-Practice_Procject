import pygame
import os

os.system("python /home/pi/webapps/music_play/stop_music.py")

path = "/home/pi/music_list/"
music_list = os.listdir(path)
# init
pygame.mixer.init()
# os.system("d")
for music in music_list:
    file_path = "/home/pi/id_saver.txt"

    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.load(path + music)
    pygame.mixer.music.play()

    f = open(file_path, "w")
    f.write(str(os.getpid()))
    f.close()

    while pygame.mixer.music.get_busy() == True:
        continue

