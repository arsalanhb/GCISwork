import turtle as t

# Khaled

# Function to get table color
def get_table_color():
    """The purpose of this function is to allow the user to choose the color of the table."""

    return input("Enter the color of the table: ")

# Function to get table dimensions
def get_table_dimensions_wt():
    """The purpose of this function is to allow the user to choose the width of the table."""

    wt = int(input("Enter the width of the table (Recommended is 300-450): ")) 
    return wt

def get_table_dimensions_ht():
    """The purpose of this function is to allow the user to choose the height of the table."""

    ht = int(input("Enter the height of the table (Recommended is 10-20): ")) 
    return ht

# Function to draw the table
def draw_table(ct, wt, ht):
    """This functions draws the table with a specified color, width, and height 
    by utilizing the values inputted in the functions above it."""

    # Preparation Phase
    t.speed(5)
    "t.hideturtle()  Hiding the turtle cursor, so it doesn't appear at the end"
    t.penup() # Lifting the pen, so the turtle can navigate to starting position without drawing anything
    t.goto(-wt / 2, ht - 100)  # Table adjustment algorithm that allows for centering. REMEMBER TO EXPLAIN DURING CLASS
    t.color(ct) # Makes the outline of the shape the same color as the fill
    t.fillcolor(ct)
    t.pendown()
    t.begin_fill()

    # Drawing Phase 
    t.forward(wt)  
    t.right(90)
    t.forward(ht)  
    t.right(90)
    t.forward(wt)  
    t.right(90)
    t.forward(ht)  

    # Conclusion Phase
    t.end_fill()
    t.penup()

# Function to draw the legs of the table
def draw_table_legs(wt, ht):
    """
    This function makes four legs for the table after the turtle draws it. The four legs are all the same size and symmetrical to one another.
    The function takes the tables width and height in order to draw the legs correctly and symmetrically under the table.
    """

    # Table leg values are hard coded to ensure the table is proportionally wider than the legs.
    leg_length = 150  # Length of the legs
    leg_width = 5  # Width of the legs (thin)

    # First leg (left front)
    t.goto(-wt/2, -ht - 80)
    t.pendown()
    t.setheading(270)  # Point turtle downward
    t.begin_fill()
    t.forward(leg_length)
    t.left(90) # Draws to the left in order to stay proportionate
    t.forward(leg_width)
    t.left(90)
    t.forward(leg_length)
    t.left(90)
    t.forward(leg_width)
    t.end_fill()

    # Second leg (right front)
    t.penup()
    t.goto(wt/2, -ht - 80)
    t.pendown()
    t.setheading(270)
    t.begin_fill()
    t.forward(leg_length)
    t.right(90) # Draws to the right in order to stay proportionate
    t.forward(leg_width)
    t.right(90)
    t.forward(leg_length)
    t.right(90)
    t.forward(leg_width)
    t.end_fill()

    # Third leg (behind the front left leg)
    t.penup()
    t.goto(-wt/2 + 30, -ht - 80)  # Adjusted position slightly to the right to appear behind
    t.pendown()
    t.setheading(270)
    t.begin_fill()
    t.forward(leg_length)
    t.right(90)
    t.forward(leg_width)
    t.right(90)
    t.forward(leg_length)
    t.right(90)
    t.forward(leg_width)
    t.end_fill()

    # Fourth leg (behind the right front leg)
    t.penup()
    t.goto(wt/2 - 25, -ht - 80)  # Adjusted position slightly to the left to appear behind
    t.pendown()
    t.setheading(270)
    t.begin_fill()
    t.forward(leg_length)
    t.right(90)
    t.forward(leg_width)
    t.right(90)
    t.forward(leg_length)
    t.right(90)
    t.forward(leg_width)
    t.end_fill()
    t.penup()

# Shahid
def draw_layer(color, width, height, y_position):
    """This function draws the layers of the cake, where the color and height are both inputted by the user. 
    The variables width and y_position depend simply on the output of the table; this allows for the layers to be
    drawn exactly on top of the table. """
     
    t.goto(-width / 2, y_position)
    t.pendown()
    t.fillcolor(color)
    t.color(color)
    t.begin_fill()
    t.forward(width)
    t.right(-90)
    t.forward(height)
    t.right(-90)
    t.forward(width)
    t.right(-90)
    t.forward(height)
    t.right(-90)
    t.end_fill()

def get_height(layer_number):
    """This function allows the user to choose the height of each layer within the cake. This allows for variety
    with each layer, where some layers will appear larger or smaller than others."""

    height = int(input(f"Enter the height for layer {layer_number} (Recommended is 15-40): "))
    return height

def cake_values():
    """This function asks the user for the color of each layer, allowing optimal customization."""

    global color1
    color1 = input("Enter the color for layer 1: ")
    global height1
    height1 = get_height(1)

    global color2
    color2 = input("Enter the color for layer 2: ")
    global height2
    height2 = get_height(2)

    global color3
    color3 = input("Enter the color for layer 3: ")
    global height3
    height3 = get_height(3)

    global color4
    color4 = input("Enter the color for layer 4: ")
    global height4
    height4 = get_height(4)

    global color5
    color5 = input("Enter the color for layer 5: ")
    global height5
    height5 = get_height(5)

def cake_draw(ht):
    """This function takes the draw_layer() function's values and applies mathematical rules to ensure that each layer
    will appear exactly on top of the other. Each layer is associated with its own unique height, which is chosen by the user."""

    draw_layer(color1, 250, height1, ht - 100)                      # Bottom layer
    draw_layer(color2, 250, height2, height1 + ht - 100)                # Middle layer
    draw_layer(color3, 250, height3, height1 + height2 + ht - 100)     
    draw_layer(color4, 250, height4, height1 + height2 + height3 + ht - 100)
    draw_layer(color5, 250, height5, height1 + height2 + height3 + height4 + ht - 100) # Top layer
    t.penup()
    t.seth(90)
    #scary code dont uncomment please
    #t.forward(ht*2) #especially this one
    #t.seth(0)
    #t.forward(5)

# Mohammed
def candle():
    """This function draws the candles on top of the cake."""

    t.pendown()
    t.color('#f3e3c2')
    t.fillcolor('#f3e3c2')
    t.begin_fill()
    t.seth(180)
    t.forward(5)
    t.seth(90)
    t.forward(50)
    t.seth(0)
    t.forward(10)
    t.seth(270)
    t.forward(50)
    t.seth(180)
    t.forward(5)
    t.end_fill()
    t.penup()
    t.seth(90)
    t.forward(50)
    t.pendown()
    t.color('Black')
    t.pensize(2)
    t.forward(7)
    t.color('Orange')
    t.fillcolor('Orange')
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.color('black')
    t.pensize(1)
    t.penup()
    t.seth(270)
    t.forward(56)
    t.seth(0)

def draw_star(size, color):
    """This function is used to another decoration--the star. The function first draws a stick, which will hold the star. """
  
    t.penup()
    t.pendown()
    t.color('#f3e3c2')
    t.pensize(5)
    t.seth(90)
    t.forward(20)
    t.pensize(1)
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.seth(0)
    t.penup()
    t.forward(13)
    t.pendown()
    t.seth(90)
    t.left(54)
    t.forward(size)  
    t.right(144)
    t.forward(size)  
    t.right(144)
    t.forward(size)  
    t.right(144)
    t.forward(size)  
    t.right(144)
    t.forward(size)  
    t.right(144)
    t.end_fill()
    t.penup()
    t.home()

def icing():
    
    t.pensize(15)    ##THICKNESS OF ICING
    t.color('white') ##Color of ICING
    t.pendown()
    
    t.seth(270)
    t.circle(10, 180)
    t.seth(270)
    t.circle(10, 180)
    t.seth(270)
    t.circle(10, 180)
    t.seth(270)
    t.circle(10, 180)
    t.seth(270)
    t.circle(10, 180)
    t.seth(270)
    t.circle(10, 180)
    t.seth(270)
    t.circle(10, 180)
    t.seth(270)
    t.circle(10, 180)
    t.seth(270)
    t.circle(10, 180)
    t.seth(270)
    t.circle(10, 180)
    t.seth(270)
    t.circle(10, 180)
    t.seth(270)
    t.circle(10, 180)
    t.seth(270)
    t.circle(10, 180)

    t.pensize(1)
    t.penup()

# Main function
def main(): 
    """The main function collects everything together and ensures that all functions run properly and punctually. 
    You don't want your cake being drawn before your table, afterall!"""
    
    # Get all inputs first
    ct = get_table_color()  # Get the table color
    wt = get_table_dimensions_wt() # Get the table's width
    ht = get_table_dimensions_ht()  # Get the table's height
    cake_values()  # values for cake

    t.setup(width=500, height=500)  
    t.screensize(bg="light blue") 
    t.speed(10)

    print("Your caking is baking! Please wait...")


    # Drawing begins after inputs
    draw_table(ct, wt, ht)  # Draw the table
    draw_table_legs(wt, ht)  # Draw the legs
    cake_draw(ht) # Draw the cake
    
    
    t.forward(height5) #get height of last layer to position for decorations correctly
    
    icingpos = t.pos() #Get start position for icing from the top left of the cake

    t.seth(0)  #positioning for left candle
    t.forward(5)
    candle()
    t.forward(240) #positioning for right candle
    candle()
    t.seth(180) #positioning for star
    t.forward(125)
    draw_star(40, "DarkGoldenrod1") ##size and color of star

    t.goto(icingpos) ## GO to start position of icing

    t.seth(180) 
    t.forward(5) #Setup to make icing symmetrical
    icing()

    input("Press enter to close the window: ")

main()