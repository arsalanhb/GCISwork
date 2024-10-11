'''The purpose of this program is to use turtle in order to draw figures by simply extracting color-coded numbers
from a given text file.'''


import turtle as t
turta=t.Turtle()

#t.setup(width=1000, height=1000)  Just wanted to draw YODA...
PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'

def initialization(turta):
    '''This function sets the speed, pencolor, canvas size, and the starting point of the turtle to start drawing'''

    t.tracer(False)
    t.setup(width=640, height=640) # Making the canvas only as big as needed
    turta.speed(0)
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * (ROWS / 2))  # starting position for turtle
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)

def draw_square(turta):
    '''This function is responsible for drawing each individual square pixel'''

    turta.begin_fill()
    for i in range(4):
        turta.forward(PIXEL_SIZE)
        turta.right(90)
    turta.end_fill()

def drawstart(turta):
    '''This function draws a grid by multiplying the columns and rows'''
    for row in range(ROWS):
        for col in range(COLUMNS):
            draw_square(turta)
            turta.penup()
            turta.forward(PIXEL_SIZE)
            turta.pendown()

        turta.penup()
        turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * (ROWS / 2 - (row + 1)))
        turta.pendown()

def get_color(digit):
    '''This function gives each color a numeric code 
    and skips when a digit that is not available is inputted.'''

    if digit == '0':
        return 'black'
    elif digit == '1':
        return 'white'
    elif digit == '2':
        return 'red'
    elif digit == '3':
        return 'yellow'
    elif digit == '4':
        return 'orange'
    elif digit == '5':
        return 'green'
    elif digit == '6':
        return 'yellowgreen'
    elif digit == '7':
        return 'sienna'
    elif digit == '8':
        return 'tan'
    elif digit == '9':
        return 'gray'
    elif digit == 'A':
        return 'darkgray'
    else:
        return None

def draw_color_pixel(digit, turta):
    '''This function is responsible for drawing each individual pixel with a specified color
    according to the digit inputted by the user.'''
    
    color = get_color(digit)
    
    if color:
        turta.fillcolor(color)
        turta.begin_fill()
        for i in range(4):
            turta.forward(PIXEL_SIZE)
            turta.right(90)
        turta.end_fill()
        turta.forward(PIXEL_SIZE)

def draw_line_from_string(digit, turta):
    '''This function draws a line of pixels based on the string input from the user.'''
    
    for char in digit:
        color = get_color(char)
        if color == None:  # Simplest check for None
            print("Invalid color code:", char)
            return False
        draw_color_pixel(char, turta)
    return True

def draw_shape_from_string(turta):
    '''This function prompts the user for color strings and draws shapes accordingly.'''
    
    for row in range(ROWS):
        color_string = input(f"Enter a color string for row {row + 1} (or press Enter to finish): ")
        if color_string == "":
            break
    
        turta.penup()
        turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * (ROWS / 2 - row))    
        turta.pendown()
        
        draw_line_from_string(color_string, turta)


def draw_shape_from_file(turta):
    '''This function opens a file, reads every line and draws rows accordingly'''

    filepath = input("Enter Filepath for the drawing file:  ")
    
    with open(filepath, 'r') as file:
        row = 0
        for line in file:
        
            color_string = line.strip() # Strip any extra whitespace (like newline characters), Now 'color_string' contains each line in the file, one at a time
            #print(line)
    
            turta.penup()
            turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * (ROWS / 2 - row))  # Move to the row position
            turta.pendown()
        
            draw_line_from_string(color_string, turta)
            row = row + 1


def draw_grid(turta):
    '''This function creates a checkered red and black grid'''
    row = 0
    while row < 19:
        color_string = '02' * 10
    
        turta.penup()
        turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * (ROWS / 2 - row))  # Move to the row position
        turta.pendown()
        row = row + 1
        draw_line_from_string(color_string, turta)

        color_string = '20' * 10

        turta.penup()
        turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * (ROWS / 2 - row))  # Move to the row position
        turta.pendown()
        row = row + 1
        draw_line_from_string(color_string, turta)