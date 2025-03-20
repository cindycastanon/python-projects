
import sys
import pygame
from part2pccexercises.settings12p1 import Settings

class Blue:
  def __init__(self):
    pygame.init()
    self.settings=Settings()
    self.screen=pygame.display.setmode(self.settings.screen_width, self.settings.screen_height)
    pygame.display.setcaption('Alien Invasion')

  def run_game(self):
    while True:
      for event in pygame.event.get():
        if pygame.type==pygame.QUIT:
          sys.exit()

      self.screen.fill(self.settings.bg_color)
      pygame.display.flip()


if __name__=='__main__':
  ai_game=Blue()
  ai_game.run_game()