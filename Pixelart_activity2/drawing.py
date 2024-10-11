import turtle as t
from pixart import initialization, drawstart, draw_grid, draw_shape_from_string, draw_shape_from_file


def main():
    turta = t.Turtle()
    initialization(turta) #Runs the Initialization Function to setup everything
    
    drawstart(turta) #Draws and Empty 20x20 Grid
    #draw_shape_from_string(turta) #Drawing from user input string
    draw_shape_from_file(turta) #Drawing from a file
    #draw_grid(turta) #drawing red and black chekered grid
    
    input("Press enter to close turtle window...")

if __name__ == "__main__":
    main()


# BEST GROUP EVER!