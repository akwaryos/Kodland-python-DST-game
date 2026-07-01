import random
from pgzero.actor import Actor
from pgzero.clock import clock
from ui.settings import WIDTH, HEIGHT


class Robot(Actor):

    def __init__(self, image, pos):
        super().__init__(image, pos)
        
        self.speed = 1
        self.dx = 0
        self.dy = 0

        self.timer = 0
        self.frame = 0
        self.direction = "right"
        self.walk_frames = {
            
            "right" : [
            "robot/walk_right_1",
            "robot/walk_right_2",
            "robot/walk_right_3",
            "robot/walk_right_4",
            ],

            "left": [
            "robot/walk_left_1",
            "robot/walk_left_2",
            "robot/walk_left_3",
            "robot/walk_left_4",
            ]
        }
        clock.schedule_interval(self.next_step, 0.12)
        self.change_direction()

    def change_direction(self):

        directions = [
            (1, 0),    
            (-1, 0),   
            (0, 1),    
            (0, -1) ,
            (0,0),
            (1,1),
            (-1,-1)
        ]

        direction = random.choice(directions)

        self.dx, self.dy = direction

        if self.dx > 0:
            self.direction = "right"
        elif self.dx < 0:
            self.direction = "left"

    def next_step(self):

        if  self.frame <= len(self.walk_frames):
            self.frame+=1
        else:
            self.frame = 0
        
    def update(self,score):
        
        self.image = self.walk_frames[self.direction][self.frame]
            
        self.timer -= 1

        if self.timer <= 0:
            self.change_direction()
            self.timer = random.randint(0, 200)

        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        if self.left <= 0:
            self.left = 0
            self.change_direction()

        if self.right >= WIDTH:
            self.right = WIDTH
            self.change_direction()

        if self.top <= 0:
            self.top = 0
            self.change_direction()

        if self.bottom >= HEIGHT:
            self.bottom = HEIGHT
            self.change_direction()



        
        self.speed = 1 + score * 0.8

