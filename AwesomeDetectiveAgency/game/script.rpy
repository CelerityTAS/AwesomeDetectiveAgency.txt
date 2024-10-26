# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define M = Character("Sir Gold")
define L = Character("Lady Gold")
define O = Character("Dishi Solver")
define D = Character("Detective Pinkerton")
define B = Character("Michael Dacoity")
define P = Character("Caze Solver")



screen pickevidence():
    vbox:
        align (0.5, 0.5)
        for item in player_inventory:
            textbutton "[item]" action Return(item)

default player_inventory = {'Business Card': "My Business Card"}

# Evidence

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg skyday
    play music "audio/intro.mp3" volume 0.5
  
    show butler normal
    # Anruf des Butlers
    "Hello, is this the Caze Solver's Detective Agency?"
    
    # TODO: remove this
    jump butler_accusation
    hide crow
    # show detective smug
    P "You have indeed, how may I be of assistance?"  

    # show anon default
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
    
default butler_accusation_score = 0

label butler_accusation:
    show Butler shocked
    B "Wait, you think I murdered Lady Gold?"
    show Butler default
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
    show Butler shocked
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
        B "What was he doing then?"
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
        B "Oh I guess he couldn't have done it then"
        $ butler_accusation_score = butler_accusation_score + 2
        jump butler_accusation_outsider
    else:
        B "What does that prove?"
        $ butler_accusation_score = butler_accusation_score-3
        B "Anyway, even if it wasn't him, because he wasn't here"
        jump butler_accusation_outsider
            
label butler_accusation_outsider:
    menu:
        B "Why could it not have just been an outsider?"
        "A birdie told me":
            jump butler_accusation_grandma
        "Grandma was fighting them":
            jump GrandmaNinjaDefendingOutsiders
        
label GrandmaNinjaDefendingOutsiders:
    B "I thought your grandma was sleeping?"
    show Player wrong
    P "Oh yeah, I forgot"
    jump butler_accusation_grandma

label butler_accusation_grandma:
    B "I guess then it must have been your Grandma I truely am sorry."
    P "How dare you"
    B "You still have not presented me with proof!"
    jump butler_accusation_final

label butler_accusation_final:
    P "First things first, your motive was that you..."
    menu:
        "...wanted revenge for how she treated you":
            jump butler_accusation_revenge
        "...were hired by the mafia":
            jump butler_accusation_mafia
        "...really don't like Sir Gold":
            jump butler_accusation_revenge
        "... wanted to steal the vase for money":
            $ butler_accusation_score = butler_accusation_score+2
            jump butler_accusation_final_proof

label butler_accusation_revenge:
    B "I never disliked Lady Gold or Sir Gold, you cannot be serious!"
    P "I guess I missed that"
    $ butler_accusation_score = butler_accusation_score-3
    jump butler_accusation_conclusion

label butler_accusation_mafia:
    B "The Mafia?"
    P "The Mafia!"
    menu:
        P "And proof for that is"
        "the tatoo you have on your hand":
            jump butler_accusation_tatoo
        "the tatoo you have on your foot":
            jump butler_accusation_tatoo
        "your earrings":
            jump butler_accusation_final_proof

label butler_accusation_tatoo:
    B "I have no tatoos anywhere on my body, what are you talking about?"
    jump butler_accusation_final_proof

label butler_accusation_final_proof:
    B "Do you have any concrete evidence?"
    P "I do"
    call screen pickevidence
    $ res = _return
    if (res=="Vase"):
        $ butler_accusation_score = butler_accusation_score + 4
        B "what about it?"
        menu:
            P "There is very clearly..."
            "...something missing":
                jump butler_accusation_final_missing
            "...a giant handprint":
                $ butler_accusation_score = butler_accusation_score + 3
                jump butler_accusation_conclusion
            "...your footprint":
                jump butler_accusation_final_missing

label butler_accusation_final_missing:
    B "what exactly?"
    P "Well I don't know actually"
    $ butler_accusation_score = butler_accusation_score -3
    B "great"
    jump butler_accusation_conclusion   

label butler_accusation_conclusion:
    if butler_accusation_score > 10:
        B "Fine, it was me, I was the one who killed the old miss"
        B "But it was an accident I swear"
        B "She just woke up, when I was fleeing with the vase"