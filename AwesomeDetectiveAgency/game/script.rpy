﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define M = Character("Sir Gold")
define L = Character("Lady Gold")
define O = Character("Dishi Solver")
define D = Character("Detective Pinkerton")
define B = Character("Michael Dacoity")
define P = Character("Caze Solver")
define C = Character("Crow")

default talkedtocrow == False
default foundcalendar = False
default talkedtobutler = False
default has_police_station=False
default has_sirs_office=False
default butler_accusation_score = 0

default player_inventory = {'Business Card': "My Business Card"}

# Evidence

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg agency
    play music "audio/intro.mp3" volume 0.5
  
    show anon at right
    #show detective normal at left
    # Anruf des Butlers
    "Hello, is this the Caze Solver's Detective Agency?"
    
    # TODO: remove this
    #jump butler_accusation
    # show detective smug
    P "You have indeed, how may I be of assistance?"  

    # show anon default
    "I am "
    B "Your Grandma and I have been working at the Howards Estate for a few months now."
    # show anon scared
    B "Yesterday Lady Bennington, Sir Howards wife was murdered!"
    B "The Police seems to believe your grandma was the murderer"
    B "I cannot fathom sweet poor old Lily being a cold blooded murderer"
    show anon normal
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
            jump BackAlley


label Estate1:
    show bg estate
    show butler

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
    


label BackAlley:
    scene bg alley
    show crow normal at right with easeinright:
        zoom 0.5
        yalign 0.64
    C "Hello, who might you be?"
    show detective normal at left with easeinleft: 
        zoom 0.5
        yalign 0.64
    #placeholer calendar aufgehoben
    #default player_inventory = {'Calendar'}
    #$ foundcalendar == true
    #talkedtocrow == true
    P "I am searching for someone that might have murdered the Lady of the local Mansion"
    if (talkedtobutler == true) and (foundcalendar == true) : 
    C "Oh my, you have talked to the butler, haven't you?"
    P "Yes indeed, how could you tell?"
    C "I saw you leave the mansion, you should know crows are everywhere here"
    C "I can assure you that the murderer is somewhere within the mansion, as I have not seen any person leave after the incident"
    show detective wrong at left with easeinleft: 
        zoom 0.5
        yalign 0.64
    menu:
        "Why should I trust you?":
            C "Why shouldn't you? You seem to be in distress, because you havent found the murderer and time is running out"
            C "Now hush hush, go back and find the culprit, so that the poor soul may rest in peace"

        "Why would a crow bother with humans?":
            C "Because it is amusing, watching humans fight against one another"
            C "Now hush hush, go back and find the culprit, so that the poor soul may rest in peace"
    else:
        C "I do not know anything about a murder, do you have any clues?"
        P "Looks like I've got all the pieces, just none of them fit. You got a fresh set of eyes on this?"


        label talking_to_sir_gold:
    show detective normal at left
    show sirgold normal at right
    $ talked_to_sir = True
    if (not talked_to_sir):
        M "Oh hello, you must be the Detective I heard is investigating the death of my poor wife."
        M "However I must warn you that the police has already found the murderer, so there is nothing for you to do here"
        P "I am very sure she is innocent!"
        P "That is what I am here to proof! I will find the real killer!"
        menu:
        "tell me about your affair" if knows_affair:
            jump sirs_affair
        "tell me about your butler":
            jump sir_gold_on_butler
        "leave":
            jump murderer_room


label sir_gold_on_butler:
    M "He is a good Butler, we have had him in our services for about 2 months now"
    P "Hmm ok"
    M "What he doesn't talk much!"
    jump talking_to_sir_gold

label sirs_affair:
    show detective normal at left
    show sirgold normal at right
    M "it hurts to say this, but I had secretly been meeting other women besides my wife"
    M "She definitely never found out though!"
    P "Yeah yeah"
    P "So where were you really, when your wife was killed"
    show sirgold shocked at right
    M "Ok waow, you knew that was a lie too."
    show sirgold normal at right
    M "I was really with my new miss in a fancy restaurant a few hours away from here"
    M "That means I cannot have murdered my wife, yes!"
    P "We will see about that"
    jump talking_to_sir_gold

### Sir about affair
label sir_not_home:
    return




label butler_accusation:
    #show Butler suprised
    B "Wait, you think I murdered Lady Gold?"
    #show Butler default
    B "I seriously hope you are in your right mind, Detective"
    menu:
        B "I invited you to this place so you could defend your grandma, why would I have done that if I murdered her"
        "You were trying to protect my Grandma":
            pass
        "You were framing Sir Gold instead!":
            jump butler_accusation_sir_gold
        "You were trying to bring me down too!":
            $ butler_accusation_score = butler_accusation_score-1
            jump butler_accusation
    
    return

label butler_accusation_sir_gold:
    B "Sir Gold is innocent?"
    return