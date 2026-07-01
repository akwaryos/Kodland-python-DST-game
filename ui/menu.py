from pygame import Rect
from .settings import WIDTH,HEIGHT
class Menu():
    def __init__(self):
        self.title = "The Man, The Robot, and The Zombie"
        self.start = Rect(100,0,200,100)
        self.music = Rect(100,20,200,100)
      
    def on_key_down(self,key):
        if key == key.SPACE:
            state = "Game"
        
            return state
        
        return None

    def draw(self,screen):
        screen.draw.text(
            self.title,
            midtop =(WIDTH/2,HEIGHT/4),
            fontsize=72,
            color = "gray",
            background = "gray",
            owidth=1,
            gcolor = "green"
            )
        screen.draw.text(
            "press space to start",
            center = (WIDTH/2,HEIGHT/2),
            fontsize=48,
            color = "gray",
            # background = "gray",
            owidth=1,
            gcolor = "green"
            )
        
        screen.draw.text(
            "press esc to quit",
            center = (WIDTH/2,HEIGHT/1.3),
            fontsize=48,
            color = "gray",
            # background = "gray",
            owidth=1,
            gcolor = "green"
            )
        
        screen.draw.text(
            "press CTRL to mute/unmute",
            center = (WIDTH/2,HEIGHT/1.6),
            fontsize=48,
            color = "gray",
            # background = "gray",
            owidth=1,
            gcolor = "green"
            )
        
        