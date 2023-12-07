import pygame as pg

_ = False
mini_map = [
    [1,1,1,1,1,1,1,1,1],
    [1,_,1,_,_,_,_,_,1],
    [1,_,1,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,1,_,1],
    [1,_,_,_,_,_,1,_,1],
    [1,1,1,1,1,1,1,1,1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, val in enumerate(row):
                if val:
                    self.world_map[(i,j)] = val

    def draw(self):
        x = []
        for pos in self.world_map:
            x.append(
                pg.draw.rect(
                    self.game.screen,
                    'darkgray',
                    (pos[0]*100, pos[1]*100, 100, 100),
                    2
                )
            )