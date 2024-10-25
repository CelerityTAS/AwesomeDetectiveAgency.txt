# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define M = Character("Sir Howards")
define L = Character("Lady Bennington")
define O = Character("Nana (Lily Colómes)")
define D = Character("Detective Richard Dichson")
define B = Character("Butler (Rick Raymond)")
define P = Character("Isaac Colómes")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show anon default
    
    # These display lines of dialogue.

    # Anruf des Butlers
    "Hello, is this the Colomes Detective Agency?"

    show detective smug
    P "You have indeed, how may I be of assistance?"

    show anon default
    "I am Rick, Rick Raymond"
    B "Your Grandma and I have been working at the Howards Estate for a few months now."
    show anon scared
    B "Yesterday Lady Bennington, Sir Howards wife was murdered!"
    B "The Police seems to believe your grandma was the murderer"
    B "I cannot fathom sweet poor old Lily being a cold blooded murderer"
    show anon default
    B "Please visit me at the Estate, Please hurry, before your grandma is behind bars."

    menu placeselect:
        "Where should I go"
        "Estate":
            jump Estate1
        "My Archives":
            "They are empty"
            jump Archives

label Estate1:
    show bg estate
    show Butler excited

    menu Estate1B1:
        "Welcome to the Estate Sir"
        "Where is my Grandma?":
            B "She is at the police station, in custody"
            B "I asked you to come here so you could look at the crime scene and prove her innocence!"
        "Show me to the Crime Scene":
            B "Of course!"
            jump Crime1
        "Leave":
            jump DetectiveAgency1
    