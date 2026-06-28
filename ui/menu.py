from pygame import Rect
class Menu():
    def __init__(self):
        self.title = "Man VS Zombie and Robot"
        self.start = Rect(100,0,200,100)
        self.music = Rect(100,20,200,100)

    def draw(self,screen):
        screen.draw.text(self.title,(100,200))