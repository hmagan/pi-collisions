from time import sleep
from Constants import WIDTH, TIME_STEPS
from Root import Root
from Block import Block
from playsound import playsound

global selected
selected = 1

global in_menu 
in_menu = True

def handle_left(e):
    global selected
    selected -= 1
    if selected <= 0:
        selected = 6

def handle_right(e):
    global selected
    selected += 1
    if selected >= 7:
        selected = 1

def hande_enter(e):
    global in_menu
    in_menu = False

def reset_blocks(block1, block2):
    block1.config(WIDTH / 2 * 0.75 - 200, 1, 0)
    block2.config(WIDTH / 2 - 200, 1, -7 / TIME_STEPS)

def main():
    global in_menu

    root = Root() # contains logic for drawing to screen and the main application loop

    block1 = Block(WIDTH / 2 * 0.75 - 200, 1, 0)
    block2 = Block(WIDTH / 2 - 200, 1, -7 / TIME_STEPS)
    
    root.bind("<Left>", handle_left)
    root.bind("a", handle_left)
    root.bind("<Right>", handle_right)
    root.bind("d", handle_right)
    root.bind("<Return>", hande_enter)

    while(True): # main loop
        if in_menu: 
            root.draw_menu(selected)
        else: 
            if block2.m == 1: # means we just exited the menu and should update mass according to selection
                block2.update_mass(100 ** (selected - 1))

            collision = False # set a boolean to play the noise once at most per tick
            for i in range(TIME_STEPS): # Euler integration 
                if block1.is_colliding(block2):
                    block1.collide(block2)
                    block1.incr_coll()
                    collision = True

                if block1.hit_wall():
                    collision = True

                block1.update()
                block2.update()

            if collision: 
                playsound("clack.mp3", False)

            root.draw_blocks([block1, block2], block1.collisions) # func to render newly-updated blocks

            if block2.x >= WIDTH + (300 if selected != 3 else 900): # if block2 exits the screen, reset to menu; 3 digits takes especially long to get the last hit
                in_menu = True
                reset_blocks(block1, block2)

        root.update() # implicit to tkinter Root class; necessary for main application loop
        sleep(0.0025) # add small delay between iterations to slow down the sim

if __name__ == "__main__":
    main()