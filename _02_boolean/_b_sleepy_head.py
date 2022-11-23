"""
Use boolean variables to control program logic between two different code
paths.
"""
import turtle

if __name__ == '__main__':
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    weekend = False
    if weekend:
        print("It's the weekend")
    else:
        print("It's not the weekend")
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    passed = True
    if passed:
        print("You passed")
    else:
        print("You didn't pass")
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    gameOver = False
    if gameOver:
        print("Game over")
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    shapeRed = False
    shapeSquare = False
    if shapeRed and shapeSquare:
        bob = turtle.Turtle()
        bob.color("red")
        bob.circle(100, 360, 4)
    pass
