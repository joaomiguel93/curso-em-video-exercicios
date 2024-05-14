# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.music.load('cidadaocomum.mp3')
pygame.mixer.music.play()
input() # necessário colocar um input para tocar o áudio
pygame.event.wait()
