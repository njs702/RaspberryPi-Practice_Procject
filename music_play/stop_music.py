import pygame
import os
# # init
# pygame.mixer.init()

# # load file
# pygame.mixer.music.load("./정준일_첫눈.mp3")

# pygame.mixer.stop()

f = open("id_saver.txt", "r")
s = f.readline()

os.system("fg")
os.system("kill " + s)

os.system("rm -rf id_saver.txt")