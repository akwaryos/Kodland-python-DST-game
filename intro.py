import pgzrun
from sprites.player import Player
from sprites.zombie import Zombie

WIDTH: 1280
HEIGHT: 720

class Game:
    def __init__(self):
        self.player = Player("player/idle", (50, 50))
        self.zombie = Zombie("zombie/idle",(200,200))
        self.score = 0

    def update(self):
        self.player.update()

    def draw(self):
        screen.clear()
        screen.fill((100, 100, 200))

        self.player.draw()
        self.zombie.draw()

        screen.draw.text(
            f"Score: {self.score}",
            (20, 10),
            color="black",
            fontsize=42,
        )


game = Game()


def update():
    game.update()


def draw():
    game.draw()


pgzrun.go()