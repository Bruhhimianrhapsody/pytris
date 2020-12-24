import pygame
import sys
import display, pieces

class Game:

    def __init__(self):
        self.maindisp = display.Display()
        self.test_piece = pieces.Long(self.maindisp.get_size())
    
    def event_handler(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
    
    def main_loop(self):
        while True:
            self.maindisp.clear()
            self.event_handler()
            self.test_piece.update()
            self.test_piece.show(self.maindisp.get_surface())
            self.maindisp.update()

if __name__ == "__main__":
    Game().main_loop()