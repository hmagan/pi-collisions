from Constants import HEIGHT

class Block():
    x = y = w = v = m = 0
    collisions = 0

    len_dict = { # dictionary for getting side length from mass
        100 ** 0: 20, 
        100 ** 1: 40, 
        100 ** 2: 80, 
        100 ** 3: 120, 
        100 ** 4: 180, 
        100 ** 5: 240, 
    }

    def __init__(self, x, m, v):
        self.x = x # x coordinate
        self.w = self.len_dict[m] # side length
        self.y = 500 - self.w / 2 # y coordinate
        self.v = v # velocity
        self.m = m # mass

    def update(self): 
        if self.hit_wall(): 
            self.v *= -1
            self.incr_coll()
        self.x += self.v

    def is_colliding(self, other):
        return not (self.x + self.w / 2 < other.x - other.w / 2 or self.x - self.w / 2 > other.x + other.w / 2)

    def bounce(self, other):
        # formula for perfectly elastic, head-on collisions
        self_curr_v = self.v
        self.v = (self.m - other.m) / (self.m + other.m) * self_curr_v
        self.v += ((2 * other.m) / (self.m + other.m) * other.v)

        other_curr_v = other.v
        other.v = (2 * self.m) / (self.m + other.m) * self_curr_v
        other.v += ((other.m - self.m) / (self.m + other.m) * other_curr_v)

    def hit_wall(self):
        return self.x <= 0
    
    def incr_coll(self): 
        self.collisions += 1

    def reset_coll(self):
        self.collisions = 0

    def update_mass(self, m): 
        self.m = m
        self.w = self.len_dict[m]
        self.y = 500 - self.w / 2

    def config(self, x, m, v): 
        self.x = x # x coordinate
        self.w = self.len_dict[m] # side length
        self.y = 500 - self.w / 2 # y coordinate
        self.v = v # velocity
        self.m = m # mass
        self.collisions = 0
