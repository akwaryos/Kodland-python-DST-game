import pgzrun
from ui.menu import Menu
from sprites.player import Player
from sprites.zombie import Zombie
from sprites.robot import Robot
from sprites.levels.compass import Compass
from ui.score import Score
from pygame import Rect
from ui.settings import WIDTH, HEIGHT,BACKGROUND_COLOR
import random


class Game:
    def __init__(self):
        music.play("background")
        self.audio_on = True
        self.states  = ("UI", "Game", "Score")
        self.current_state = self.states[0]
        self.menu = Menu()
        self.player = Player("player/idle", (WIDTH/2, HEIGHT-100))
        self.compass = Compass("levels/compass")
        self.zombies = []
        self.robots = []
        self.generate("zombie")
        self.generate("robot")            
        self.score = Score()




    def update(self):
         if self.current_state == "Game":
            self.player.update()
           
            if self.player.colliderect(self.compass):
                self.score.increment()
                if self.audio_on:
                    sounds.collect.play()
                self.compass.spawn()
                if self.score == 10:
                    self.set_state("Score")

        

            for zombie in self.zombies:
                zombie.update(self.score.get_score())
                if self.player.distance_to(zombie) < 45:
                    zombie.x = random.randint(50, WIDTH - 50)
                    zombie.y = random.randint(50, HEIGHT - 50)
                    self.player.image = "player/fall"
                    if self.audio_on:
                        sounds.hurt.play()
                    self.player.decrement()
                    self.score.decrement()



            for robot in self.robots:
                robot.update(self.score.get_score())
                if self.player.distance_to(robot) < 45:
                    robot.x = random.randint(50, WIDTH - 50)
                    robot.y = random.randint(50, HEIGHT - 50)
                    self.player.image = "player/fall"
                    if self.audio_on:
                        sounds.hurt.play()
                    
                    self.player.decrement()
                    self.score.decrement()

            if self.player.health == -1:
                self.set_state("Score")



    def toggle_audio(self):

        self.audio_on = not self.audio_on

        if self.audio_on:
            music.unpause()
        else:
            music.pause()

    def generate(self,item):
  



        if item =="zombie":
            for zombie in range(random.randint(6,12)):
                x = random.randint(100, WIDTH - 50)
                y = random.randint(100, HEIGHT - 50)
                zombie = Zombie("zombie/idle", (x, y))
                self.zombies.append(zombie)


        if item =="robot":
            for robot in range(random.randint(6,12)):
                x = random.randint(100, WIDTH - 50)
                y = random.randint(100, HEIGHT - 50)
                robot = Robot("zombie/idle", (x, y))
                self.robots.append(robot)
                
                


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

        if key == key.ESCAPE:
           quit()

        if key == key.LCTRL:
          self.toggle_audio()
           
        
    def draw(self):
        screen.clear()
        screen.fill(BACKGROUND_COLOR)

        if self.get_state() == "UI":
            self.menu.draw(screen)
            
        elif self.get_state() == "Game":
            screen.blit("background", (0, 0))
            screen.draw.text(
                f"Score: {self.score.get_score()} /10",
                (20, 10),
                color="black",
                fontsize=42,
            )

            screen.draw.text(
                f"Health: {self.player.get_health()} /3",
                (250, 10),
                color="black",
                fontsize=42,
            )

            self.player.draw()

     
            self.compass.draw()

        
            for zombie in self.zombies:

                zombie.draw()
            for robot in self.robots:
                robot.draw()

        elif self.get_state() == "Score": 
                if self.score.get_score() < 10:
                    sounds.lose.play()

                    screen.draw.text(
                    f"Game Over",
                    (WIDTH/2, HEIGHT/2),
                    color="black",
                    fontsize=100,
                    )
                    screen.draw.text(
                    f"Score: {self.score.get_score()}",
                    (WIDTH/2 + 200, HEIGHT/2 +200),
                    color="black",
                    fontsize=42,
                    )

                else:
                    sounds.win.play()
                    
                    screen.draw.text(
                    f"Congrats",
                    (WIDTH/2, HEIGHT/2),
                    color="black",
                    fontsize=100,
                    )
                    screen.draw.text(
                    f"Score: {self.score.get_score()} /10",
                    (WIDTH/2, HEIGHT/2 +200),
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