import pgzrun
from ui.menu import Menu
from sprites.player import Player
from sprites.zombie import Zombie
from ui.settings import WIDTH, HEIGHT,BACKGROUND_COLOR


class Game:
    def __init__(self):
        self.states  = ("UI", "Game", "Score")
        self.current_state = self.states[0]
        self.menu = Menu()
        self.player = Player("player/idle", (50, 50))
        self.zombie = Zombie("zombie/idle",(200,200))
        
        self.score = 0

    def update(self):
         if self.current_state == "Game":
            self.player.update()

    def set_state(self,state):
         if state in self.states:
            self.current_state = state
    
    def get_state(self):
        return self.current_state

    def on_key_down(self, key):

        if self.current_state == "UI":

            state = self.menu.on_key_down(key)

            if state:
                self.set_state(state)

    def draw(self):
        screen.clear()
        screen.fill(BACKGROUND_COLOR)

        if self.get_state() == "UI":
            self.menu.draw(screen)
            
        else:

            self.player.draw()
            self.zombie.draw()
            print(self.get_state())

            screen.draw.text(
                f"Score: {self.score}",
                (20, 10),
                color="black",
                fontsize=42,
            )




game = Game()

def on_key_down(key):
    game.on_key_down(key)
    
def update():
    game.update()


def draw():
    game.draw()


pgzrun.go()