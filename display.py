import pygame 

class Display():
    
    def __init__(self):
        self.SIZE = 600 
        self.surface = pygame.display.set_mode((self.SIZE,self.SIZE))
        pygame.display.set_caption("Pytris")
        self.clock = pygame.time.Clock()
        self.fps = 5

    def clear(self):
        self.surface.fill((0,0,0))

    def update(self):
        pygame.display.update()
        self.clock.tick(self.fps)
    
    def get_size(self):
        return self.SIZE

    def get_surface(self):
        return self.surface