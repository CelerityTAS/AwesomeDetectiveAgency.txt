# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define M = Character("Sir Gold")
define L = Character("Lady Gold")
define O = Character("Dishi Solver")
define D = Character("Detective Pinkerton")
define B = Character("Michael Dacoity")
define P = Character("Caze Solver")
define C = Character("Crow",color="#222222")

default player_inventory = {
    'Business Card': "My Business Card",
    'Diary': "The Diary of Sir Gold, it has info on a date he had on the 27.10 at 19:00",
    'Calender': "A few days are marked. The 27. with a heart. Uh their cars insurance is expiring"
    }

screen pickevidence():
    vbox:
        align (0.5, 0.5)
        for item in player_inventory:
            textbutton "[item]" action Return(item)
# Evidence
default correct = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg skyday

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    show anon default
    

    play music "audio/intro.mp3" volume 0.5
    # Anruf des Butlers
    "Hello, is this the Caze Solver's Detective Agency?"
    
    # TODO: remove this
    jump butler_accusation

    show detective smug
    P "You have indeed, how may I be of assistance?"

    show anon default
    "I am "
    B "Your Grandma and I have been working at the Howards Estate for a few months now."
    show anon scared
    B "Yesterday Lady Bennington, Sir Howards wife was murdered!"
    B "The Police seems to believe your grandma was the murderer"
    B "I cannot fathom sweet poor old Lily being a cold blooded murderer"
    show anon default
    B "Please visit me at the Estate, Please hurry, before your grandma is behind bars."
    jump place_select

label place_select:
    show bg room
    menu:
        "Move to"
        "Estate":
            jump Estate1
        "Police Station":
            jump Estate1
        "Back Alley":
            jump Estate1


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
    
default butler_accusation_score = 0

label butler_accusation:
    show Butler suprised
    B "Wait, you think I murdered Lady Gold?"
    show Butler default
    B "I seriously hope you are in your right mind, Detective"
    menu:
        B "I invited you to this place so you could defend your grandma, why would I have done that if I murdered her"
        "You were trying to protect my Grandma":
            jump butler_accusation_sir_gold
        "You were framing Sir Gold instead!":
            jump butler_accusation_sir_gold
        "You were trying to bring me down too!":
            $ butler_accusation_score = butler_accusation_score-2
            jump butler_accusation
    
    return
        
label butler_accusation_sir_gold:
    show Butler wow
    $ butler_accusation_score = butler_accusation_score+1
    menu:
        B "Sir Gold is innocent?"
        "He was not home":
            jump nothome
        "He was sleeping":
            jump sleeping_evidence
        "He witnessed the murder":
            jump witness_evidence
    return

label sleeping_evidence:
    call screen pickevidence
    B "Sorry, but that is not at all evidence he was sleeping!"
label witness_evidence:
    call screen pickevidence
    B "Sorry, but that doesn't prove anything"

label nothome:
    menu :
        B "I guess he wasn't home, but what was he doing at that time?"
        "He was at a Hostess club":
            $ correct=True
            jump not_home_evidence 
        "He was golfing":
            $ correct=False
            jump not_home_evidence
        "He was working":
            $ correct=False
            jump not_home_evidence


label not_home_evidence:
    call screen pickevidence
    $ res = _return
    if (res=="Diary" or res=="Calendar"):
        B "Oh I guess he was innocent"
        $ butler_accusation_score = butler_accusation_score + 2
    else:
        B "What does that prove?"
        $ butler_accusation_score = butler_accusation_score-3
            

label butler2:
    B "How did you know"
    return

label failure:
    B "Okok you are dumb"
    return

label after:
    return