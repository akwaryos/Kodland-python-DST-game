from pgzero.actor import Actor
from pgzero.clock import clock
from pgzero.keyboard import keyboard
class Player(Actor):
    def __init__(self,image, position):
        super().__init__(image, position)

        self.speed = 3

        self.walk_frames = {
            
            "right" : [
            "player/walk_right_1",
            "player/walk_right_2",
            "player/walk_right_3",
            "player/walk_right_4",
            ],

            "left": [
            "player/walk_left_1",
            "player/walk_left_2",
            "player/walk_left_3",
            "player/walk_left_4",
            ]
        }

        self.frame = 0
        self.in_motion = False
        self.direction = "right"

        clock.schedule_interval(self.next_step, 0.12)

    def update(self):
        self.in_motion = self.handle_input()
        self.animate()

    def handle_input(self):
        in_motion = False

        if keyboard.left:
            self.x -= self.speed
            in_motion = True
            self.direction = "left"

        if keyboard.right:
            self.x += self.speed
            in_motion = True
            self.direction = "right"

        if keyboard.up:
            self.y -= self.speed
            in_motion = True

        if keyboard.down:
            self.y += self.speed
            in_motion = True

        return in_motion

    def next_step(self):

        if self.in_motion and self.frame < 3:
            self.frame+=1
        else:
            self.frame = 0
        

    def animate(self):
        if self.in_motion:
            self.image = self.walk_frames[self.direction][self.frame]
            print(self.image)
        else:
            self.image = "player/idle"
            self.frame = 0