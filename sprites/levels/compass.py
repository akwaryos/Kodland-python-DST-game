from pgzero.actor import Actor
import random
from ui.settings import WIDTH, HEIGHT

class Compass(Actor):
    def __init__(self,image):
        super().__init__(image)
        self.spawn()

    def spawn(self):
        self.pos = (
            random.randint(40, WIDTH - 40),
            random.randint(40, HEIGHT - 40)
        )
