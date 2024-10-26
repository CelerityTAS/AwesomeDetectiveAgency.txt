# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define M = Character("Sir Gold")
define L = Character("Lady Gold")
define O = Character("Dishi Solver")
define D = Character("Detective Pinkerton")
define B = Character("Michael Dacoity")
define P = Character("Caze Solver")
define C = Character("Crow")


default foundcalendar = False
default talkedtobutler = False
default has_police_station=False
default has_sirs_office=False
default butler_accusation_score = 0

default player_inventory = {'Business Card': "My Business Card"}

default knows_affair = False
default talked_to_sir = False
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
    jump talking_to_sir_gold
    #jump butler_accusation
    # show detective smug
    P "You have indeed, how may I be of assistance?"  

    "I am Michael Dacoity"
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
        
        #change scale
    C "Hello, who might you be?"
    show detective normal at left with easeinleft: 
        zoom 0.5
        yalign 0.64

    #P "I am searching for someone that might have murdered the Lady of the local Mansion"
    #if (talkedtobutler == true) and (foundcalendar == true) : 
    #   C "Oh my, you have talked to the butler, haven't you?"
    #   P "Yes indeed, how could you tell?"
    #   C "I saw you leave the mansion, and you should know crows"

### Talking to Sir Gold

label murderer_room:
    if (not talking_to_sir_gold):
        jump talking_to_sir_gold
    B "This is the crime Scene"
    return


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

### Sir Accusation
label sir_accusation:
    show detective normal at left
    show sirgold shocked at right
    M "You think I murdered my wife?"
    M "Are you insane?"
    M "I know I shouldn't have let some loosey doosey detective snoop around the place"
    M "What could you have possibly taken as evidence for your claim?"
    menu:
        "You clearly..."
        "wanted to get my grandmother fired":
            jump sir_accusation_grandma_fired
        "Weren't home on the 27.th":
            jump sir_accusation_not_home
        "had an affair and wanted your wife dead":
            jump sir_accusation_affair

label sir_accusation_affair:
    if (knows_affair):
        M "But if I wasn't here, I could not have murdered my wife you idiot"
        show detective wrong at left
        P "Guess I missed that"
        show detective normal at left
        jump sir_accusation_evidence
    else: 
        jump sir_not_home

label sir_accusation_grandma_fired:
    M "If I wanted your grandmother fired, I would have just fired her"
    P "You were scared of her, since she could easily beat you up"
    M "Nonsense"
    jump sir_accusation_evidence

label sir_accusation_not_home:
    M "But if I wasn't home, then I could not have murdered my wife?"
    M "You seem to be confused"
    show Player wrong at left
    if (knows_affair):
        jump sir_accusation_evidence
    else:
        jump sir_not_home





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
    show butler shocked at right
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
    show butler normal at right
    call screen pickevidence
    B "Sorry, but that is not at all evidence he was sleeping!"
label witness_evidence:
    show butler normal at right
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
    if (correct and (res=="Diary" or res=="Calendar")):
        show butler shocked at right
        B "Oh I guess he couldn't have done it then"
        $ butler_accusation_score = butler_accusation_score + 2
        jump butler_accusation_outsider
    else:
        show butler normal at right
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
    show detective wrong at left
    P "Oh yeah, I forgot"
    jump butler_accusation_grandma

label butler_accusation_grandma:
    show detective normal at left
    B "I guess then it must have been your Grandma I truely am sorry."
    show detective shocked at left
    P "How dare you"
    show detective normal at left
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
    show detective wrong at left
    P "I guess I missed that"
    show detective normal at left
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
                jump butler_accusation_handprint_grandma
            "...your footprint":
                jump butler_accusation_final_missing

label butler_accusation_handprint_grandma:
    B "What about grandmas handprint?"
    P "These are clearly too big for grandmas small hands, they must be yours!!"
    $ butler_accusation_score = butler_accusation_score + 5
    jump butler_accusation_conclusion

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
        return


label LooseScreen:
    show bg loose
    pause
    return
    B "Sir Gold is innocent?"
    return