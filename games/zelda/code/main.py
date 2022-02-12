''' A Zelda-style RPG in Python that includes a lot of elements you need for a sophisticated game like graphics and animations, fake depth; upgrade mechanics, a level map and quite a bit more. 

Thanks for AI camp for sponsoring this video. You can find the link to their summer camp here: https://ai-camp.org/partner/clearcode 

If you want to support me: https://www.patreon.com/clearcode 
(You also get lots of perks)

Social stuff:
Twitter - https://twitter.com/clear_coder
Discord - https://discord.com/invite/a5C6pYw2w5  

https://www.youtube.com/watch?v=QU1pPzEGrqw&t=1s '''

import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
