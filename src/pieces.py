import pygame 

class Piece():

    def __init__(self, screen_size):
        self.BLOCK_SIZE = 20         
        self.x = (screen_size // 2) - (self.BLOCK_SIZE // 2)
        self.y = 0

class Long(Piece):

    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.blocks = [pygame.Rect(self.x, y, self.BLOCK_SIZE, self.BLOCK_SIZE,) for y in range(0, 40, 10)]
        self.color = (64, 224, 208)
        self.can_flip = True

    def show(self, screen):
        for i in self.blocks:
            pygame.draw.rect(screen, self.color, i)

    def update(self):
        for i in self.blocks:
            i.y += self.BLOCK_SIZE  

    def flip(self):
        if self.can_flip == True:
            diff = -20
            for i in self.blocks:
                i.x += diff
                diff += self.BLOCK_SIZE
            for i in self.blocks:
                i.y = self.blocks[-1].y
            self.can_flip = False
        else:
            diff = -20
            for i in self.blocks:
                i.x = self.blocks[-1].x
                i.y += diff 
                diff += self.BLOCK_SIZE
            self.can_flip = True
