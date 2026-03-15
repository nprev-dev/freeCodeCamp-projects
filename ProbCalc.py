import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, amount in kwargs.items():
            for _ in range(amount):             # amount = amount time loop runs
                self.contents.append(color)     # each time inner loop runs, adds color to self.contents
# after this runs, if red = 3 self.contents become ["red", "red", "red"]
    def draw(self, balls_draw):
        balls_drawn = []
        if balls_draw >= len(self.contents):  
            balls_drawn = self.contents.copy()    #creates seperate copy of self.contents
            self.contents = []
            return balls_drawn
        for _ in range(balls_draw):
            random_index = random.randrange(len(self.contents))# randomly selects an item from self.contents by position
            ball = self.contents.pop(random_index) # removes the item at position random_index from self.contents and stores it in ball
            balls_drawn.append(ball)
        return balls_drawn





def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_exp = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat) # creates full independant vers of hat
        balls_drawn = hat_copy.draw(num_balls_drawn)
        success = True
# post function checks if we drew the least required number of each expected color        
        for color, required_amount in expected_balls.items(): 
        # post function checks if we didnt draw least required, and returns sucess False and stops this experiment
            if balls_drawn.count(color) < required_amount:
                success = False
                break
        if success: # adds 1 to sucess_exp if exp was sucessful
            success_exp += 1
    return success_exp / num_experiments
