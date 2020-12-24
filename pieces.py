import pygame 

class Piece():

    def __init__(self, screen_size):
        self.block_size = 20         
        self.x = (screen_size // 2) - (self.block_size // 2)
        self.y = 0

class Long(Piece):

    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.form = [pygame.Rect(self.x, y, self.block_size, self.block_size,) for y in range(0, 40, 10)]
        self.color = (64, 224, 208)

    def show(self, screen):
        for i in self.form:
            pygame.draw.rect(screen, self.color, i)

    def update(self):
        for i in self.form:
            i.y += self.block_size  

    def flip(self):
        diff = -20
        for i in self.form:
            i.x = 
            i.x += diff
            diff += 10 
