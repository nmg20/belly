import math as m

#Configuración general del juego
RES = WIDTH, HEIGHT = 1000, 700
FPS = 0

#Configuración del jugador
PLAYER_POS = 1.5, 2 #mini map
PLAYER_ANGLE = 180
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.1

#Configuración de RayCast
FOV = m.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20