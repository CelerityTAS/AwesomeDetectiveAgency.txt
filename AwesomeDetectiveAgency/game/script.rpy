# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define M = Character("Sir Howards")
define L = Character("Lady Bennington")
define O = Character("Poor Grandma")
define D = Character("Detective Richard Dichson")
define B = Character("Butler")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Butler happy

    # These display lines of dialogue.

    B "Hey your Grandma has been accused of murder  "
    B "Hey there"

    # This ends the game.

    return
