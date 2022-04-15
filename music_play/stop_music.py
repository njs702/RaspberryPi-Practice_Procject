import pygame
import os
# # init
# pygame.mixer.init()

# # load file
# pygame.mixer.music.load("./정준일_첫눈.mp3")

# pygame.mixer.stop()
file_path = "/home/pi/id_saver.txt"
f = open(file_path, "r")
s = f.readline()

os.system("fg")
os.system("kill " + s)

os.system("rm -rf " + file_path)