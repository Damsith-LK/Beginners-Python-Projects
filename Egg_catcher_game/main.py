"""Steps of the programme
1. Setup screen
2. Setup the catcher
3. Setup egg falling
4. Keep score
5. Display the 4 chances of dropping the egg
6. If egg dropped 1 chance gone (No chances = game over)
"""

import turtle

# Setting up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title('Egg Catcher Game')


screen.exitonclick()
