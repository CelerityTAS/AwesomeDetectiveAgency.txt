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

default talkedtocrow = False
default foundcalendar = False
default cantalk_to_crow = False
default talked_to_butler = False
default butler_accusation_score = 0

default player_inventory = {'Business Card': "My Business Card", "Phone": "I figured ot the murder was on the 27.10. at 4:00 PM"}
default player_inventory_remaining_slots = 6

default knows_affair = False
default talked_to_sir = False
# Evidence

default unlocked_back_alley = False
default unlocked_crime_scene = False
default has_recent_calender = False

screen pickevidence: 
    vbox:
        yalign 0.5
        xalign 0.5
        for item in player_inventory:
            textbutton "[item]" action Return(item)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene bg agency
    play music "audio/intro.mp3" volume 0.5
  
    show anon at right: 
            zoom 0.5
            yalign 0.64
    #show detective normal at left
    # Anruf des Butlers
    "Hello, is this the Caze Solver's Detective Agency?"
    
    P "Indeed it is, how may I be of assistance?"  
    "I am Michael Dacoity"
    B "Your grandma and I have been working at the Howards' Estate for a few months now."
    # show anon scared
    B "Yesterday, Lady Bennington, Sir Howard's wife was murdered!"
    B "The Police seems to believe your grandma was the murderer"
    B "I cannot fathom sweet poor old Lily being a cold blooded murderer"
    B "Please visit me at the Estate, lest your grandma finds herself behind bars."
    hide anon
    jump place_select

label place_select:
    hide anon
    hide sirgold
    hide butler
    menu:
        "Move to"
        "Estate":
            jump Estate
        "Back Alley" if (unlocked_back_alley):
            jump BackAlley
        "Crime Scene" if unlocked_crime_scene:
            jump murderer_room


label Estate:
    show bg estate
    show detective normal at left: 
            zoom 0.5
            yalign 0.64
    if (not talked_to_butler):
        jump talk_to_butler
    menu:
        "What should I do?"
        "Inspect":
            jump inspect_Estate
        "Talk to Butler":
            jump talk_to_butler
        "Move":
            jump place_select

label BackAlley:
    scene bg alley
    if (not talkedtocrow):
        jump talking_to_crow
    menu:
        "What should I do?"
        "Talk to crow":
            jump talking_to_crow
        "Inspect":
            jump inspect_back_alley
        "Move":
            jump place_select


label inspect_Estate:
    hide butler
    hide sirgold
    menu:
        "Where to inspect"
        "Piano":
            P "Just and old Piano"
            P "It is open"
            "Boop Boop Beep Beep PeeP"
            P "It is very out of tune. Must be just an art piece. Or someone is seriously tone deaf."
            if ("Note1" in player_inventory):
                P "This is where that Note used to be"
                menu:
                    P "Should I put it back?"
                    "Yes":
                        $ player_inventory.pop("Note1")
                    "No":
                        jump inspect_Estate
            else :
                P "Oh there is a note in the sheet music."
                if (player_inventory_remaining_slots > 0):
                    menu:
                        P "Should I take a look at it?"
                        "Yes":
                            $ player_inventory_remaining_slots -= 1
                            $ player_inventory["Note1"]="An old note left by someone, it just has the date of the murder."
                            P "Ok I got it"
                        "No":
                            jump inspect_Estate
                else:
                    P "Oh I can't keep track of this much stuff."
                    P "Gotta put back something"
        "Paintings":
            P "A few old Paintings are hung up here."
            show detective wrong at left: 
                zoom 0.5
                yalign 0.64
            P "WAIT IS THAT MY GRANDMA???"
            show detective normal at left: 
                zoom 0.5
                yalign 0.64
            P "I guess she was already extraordinarily strong!"
            P "The other one must be from Lady Gold"
            menu paintings:
                "What Painting to look at further"
                "Pie Thing":
                    P "I never understood abstract art"
                    P "Oh, this is just a pie chart of the company earnings"
                    P "Why would you hang that up in your home"
                    P "Wait does that say 'Money Laundering???'"
                    jump paintings
                "Sir":
                    P "A fine gentleman"
                    P "I wonder where he gets his suits"
                    if ("Note3" in player_inventory):
                        P "This is where that Note used to be"
                        menu:
                            P "Should I put it back?"
                            "Put it Back":
                                $ player_inventory.pop("Note3")
                            "Keep it":
                                jump paintings
                    else:
                        P "Oh there is a note hidden behind the painting"
                        if (player_inventory_remaining_slots > 0):
                            menu:
                                "Take it!":
                                    $ player_inventory_remaining_slots -= 1
                                    $ player_inventory["Note3"]="An Old note left by someone, it just has 3 PM on it."
                                "Leave it":
                                    jump paintings
                    jump paintings
                "Grandma":
                    P "She is buff!"
                    P "Almost makes me wanna believe she did it!"
                    P "She could probably beat up a few gangsters on her own if she wanted to!"
                    P "That reminds me, I never asked her, what she used to do before becoming a cleaning lady"
                    P "I guess it must have paid well, I mean she has her own little fortune"
                    P "She never really talkes about her past..."
                    jump paintings
                "Lady":
                    P "It seems like it is the dead lady."
                    P "A pity, she looks breathtaking"
                    P "I will find whoever killed you!"
                    jump paintings
                "Enough of the Paintings!":
                    jump inspect_Estate
        "Under the Carpet":
            P "I am very much not lifting this carpet!!"
        "Ok found everything":
            jump Estate
    jump inspect_Estate

label inspect_back_alley:
    menu:
        "Where to inspect"
        "'some girl' Poster":
            P "Oh it is a pop culture reference!"
            if (cantalk_to_crow):
                C "I love that game"
                P "same"
                P "'some girl' was my favourite character"
                C "I liked the conductor"
                P "all conductors are better than penguins"
            else:
                P "Damn I want someone to talk to about this game"
        "Wright does it right-Poster":
            P "Oh it is that damn Lawyer again"
            P "I hear he is never wrong"
            P "Probably could give me some competition!"
            jump inspect_back_alley
        "Trash Can":
            P "Who has this much trash?"
            P "I think I just saw a crow eating in here!"
            if ("Note4" in player_inventory):
                P "This is where I found that note"
                menu:
                    P "Should I put it back?"
                    "Put it Back":
                        $ player_inventory.pop("Note3")
                        jump paintings
                    "Keep it":
                        jump paintings
            else:   
                P "Oh there is a note here"
                if (player_inventory_remaining_slots > 0):
                    menu:
                        P "Should I take it?"
                        "Take it":
                            $ player_inventory_remaining_slots -= 1
                            $ player_inventory["Note4"]="A note someone left here, it just says 'Theo' and has a heart on it. It could be from the Sir's wife?"
                            jump inspect_back_alley
                        "Leave it":
                            jump inspect_back_alley
        "Mural":
            P "This reminds of a movie I watched as an adult"
            P "It was called murder on the solar express or something"
            P "I wonder if everyone is guilty."
            P "Or maybe just the victim is guilty!"
            P "Maybe she is still alive!"
            if (cantalk_to_crow):
                C "I don't think so"
                P "What do you know??"
                C "Crah!"
            jump inspect_back_alley
        "Ok found everything":
            jump BackAlley
    jump inspect_back_alley

    
label talk_to_butler:
    show butler normal at right: 
            zoom 0.5
            yalign 0.64
    if (accusation_mode):
        $ accusation_mode = False
        jump butler_accusation

    if (not talked_to_butler):
        $ talked_to_butler = True
        "Welcome to the Estate Sir"
    menu:
        "Where is my grandma?":
            B "She is at the police station, in custody"
            B "I asked you to come here so you could look at the crime scene and prove her innocence!"
        "Show me to the Crime Scene":
            B "Of course!"
            jump murderer_room
        "Leave":
            jump place_select
    jump talk_to_butler

label talking_to_crow:
    hide butler
    hide sirgold
    show crow normal at right: 
            zoom 0.5
            yalign 0.64

    if (accusation_mode):
        $ accusation_mode = False
        jump crow_accusation

    if (not talkedtocrow):
        $ talkedtocrow = True
        $ cantalk_to_crow = True
        show crow normal at right:
            zoom 0.5
            yalign 0.64
        C "Hello, who might you be?"
        show detective normal at left: 
            zoom 0.5
            yalign 0.64
        P "I am searching for someone that might have murdered the Lady of the local Mansion"
        C "Oh my, you have talked to the butler, haven't you?"
        P "Yes indeed, how could you tell?"
        C "I saw you enter the mansion, you should know crows are everywhere here"
        C "I can assure you that the murderer is somewhere within the mansion."
        C "haven't seen any person leave after that Lady was killed!"
        show detective wrong at left: 
            zoom 0.5
            yalign 0.64
    menu:
        "Why should I trust you?":
            C "Why shouldn't you? You seem to be in distress, because you havent found the murderer and time is running out"
            C "Now hush hush, go back and find the culprit, so that the poor soul may rest in peace"

        "Why would a crow bother with humans?":
            C "Because it is amusing, watching humans fight against one another"
            C "Now hush hush, go back and find the culprit, so that the poor soul may rest in peace"
        "Did you see anything?":
            C "I can assure you that the murderer is somewhere within the mansion, as I have not seen any person leave after the incident"
            C "Before the incident, there was someone that left however, Crah"
            C "The old man left"
            C "Only came back the next day, crah"
        "Ok, Thanks":
            jump BackAlley
    jump talking_to_crow


label murderer_room:
    $ unlocked_crime_scene = True
    show bg murderroom
    if (not talked_to_sir):
        B "This is the crime Scene"
        B "Oh and sir gold seems to want to talk to us"
        hide butler
        jump talking_to_sir_gold
    else:
        menu:
            "What should I do?"
            "Talk to Sir Gold":
                jump talking_to_sir_gold
            "Inspect":
                jump inspect_murderer_room
            "Leave":
                jump place_select
    
label inspect_murderer_room:

    show bg murderroom

    P "So this is where Lady Gold was murdered"
    menu: 
        "Vase":
            if("Vase" in player_inventory):
                P "The Vase seemed quite expensive, should I put it back? "
                menu: 
                    "Yes":
                        $ player_inventory.pop("Vase")
                    "No":
                        jump inspect_murderer_room
            else:
                P "It seems to be shattered, and there is a lot of blood on it, better take it as evidence"
                if (player_inventory_remaining_slots > 0):
                    menu:
                        P "Should I pick it up?"
                        "Yes":
                            $ player_inventory_remaining_slots -= 1
                            $ player_inventory["Vase"] = "The vase that was used as the murder weapon, blood seems to be the only thing on it"
                            P "With this, I'm sure I'll find the perpetrator!"
                        "No":
                            P "It is quite heavy, perhaps I can come back later"
                else:
                    P "Wow I can't keep track of all this stuff"

        "Vase fragments" if ( not "Vase fragments" in player_inventory):
            P "Hmmmm, the fragments. They might be useful later, might aswell pick them up"
            "Picked up the fragments"
            $ player_inventory_remaining_slots -= 1
            $ player_inventory ["Vase fragments"] = "Shattered remains of the once beautiful vase"

        "Calendar" if (not "Calendar" in player_inventory):
            P "Found the calendar!"
            $ foundcalendar = True
            menu:
                "Pick it up?"
                "Yes":
                    $ player_inventory_remaining_slots -= 1
                    $ player_inventory ["Calendar"] = "27.10 comes across as being a special day for Sir Gold, as it is marked with a heart"
                    P "The 27th is marked as a special date, maybe I can ask around"
                "No":
                    P "Why would a calendar even be useful? I'm just wasting my time here"
          
        "Chair" if (not "Note2" in player_inventory):
            P "Seems like I found some kind of letter, very intriguing"
            menu: 
                "Pick the letter up?"
                "Yes":
                    $ player_inventory_remaining_slots -= 1
                    $ player_inventory ["Note2"] = "Sir Gold wants to meet someone"
                    P "Perhaps this letter may be useful"
                "No":
                    P "I don't care about personal buisness"
                    P "Let's go somewhere with useful evidence"
        "Inspect windows":
            "These windows are very clean, huh"
            if (foundcalendar == True) or ("Calendar" in player_inventory):
                $ unlocked_back_alley = True
                jump BackAlley
            else:
                jump murderer_room

        "Leave":
            jump murderer_room

    #fenster inspecten 
    #calendar angeguckt oder aufgehoben
    #kann dann zum back alley
    jump inspect_murderer_room

label talking_to_sir_gold:
    hide crow
    hide butler
    show detective normal at left: 
            zoom 0.5
            yalign 0.64
    show sirgold normal at right: 
            zoom 0.5
            yalign 0.64

    if (accusation_mode):
        $ accusation_mode = False
        jump sir_accusation
    if (not talked_to_sir):
        $ talked_to_sir = True
        M "You must be the Detective Michael told me about."
        M "However I must warn you that the police has already found the murderer, so there is nothing for you to do here"
        P "I am quite sure she is innocent!"
        P "That is what I am here to proof! I will find the real killer!"
    menu sir_gold_menu:
        "Tell me about your affair" if knows_affair:
            jump sirs_affair
        "Tell me about your butler":
            jump sir_gold_on_butler
        "what happened?":
            if (not knows_affair):
                M "I was sleeping in my room peacefully"
            else:
                M "I was at the place of a hostess"
            M "The police told me your grandma brought tea to my wife"
            M "Then she killed my wife with a vase and took sleeping pills"
            M "The sleeping pills were later found in a trashcan in the kitchen"
            P "can I see that kitchen?"
            M "No, my servants are currently preparing my food"
            jump sir_gold_menu
        "Any strange occurances on that day?":
            M "Apart from the death of my wife?"
            M "I don't really remember anything"
            M "I did receive a few calls from mafiosos, that wanted to get my money. Hahaha"
            M "These mafiosos are really easy to spot however. They al have Earrings that are in the shape of Munition"
            M "The big fishes even have nukes, someone told me once"
            M "Truely crazy these people"
            P "Don't you fear for your life?"
            M "No!"
            jump sir_gold_menu
        "leave":
            jump murderer_room
            
label sir_gold_on_butler:
    M "He is a good butler, we have had him in our services for about 2 months now"
    P "Hmm ok"
    M "Shouldn't talking be your specialty as a detective?!?"
    jump talking_to_sir_gold

label sirs_affair:
    $ knows_affair = True
    show detective normal at left: 
            zoom 0.5
            yalign 0.64
    show sirgold normal at right: 
            zoom 0.5
            yalign 0.64
    M "It hurts to say this, but I have secretly been meeting other women besides my wife"
    M "She definitely never found out though!"
    P "Yeah yeah"
    P "So where were you really, when your wife was killed"
    show sirgold shocked at right: 
            zoom 0.5
            yalign 0.64
    M "Ok waow, you knew that was a lie too."
    show sirgold normal at right: 
            zoom 0.5
            yalign 0.64
    M "At that time I was meeting my new misstress in a fancy restaurant a few hours away from here"
    M "That means I cannot have murdered my wife, yes!"
    P "We will see about that"
    jump talking_to_sir_gold


### Sir Accusation
label sir_accusation:
    show detective normal at left: 
            zoom 0.5
            yalign 0.64
    show sirgold shocked at right: 
            zoom 0.5
            yalign 0.64
    M "You think I murdered my wife?"
    M "Are you insane?"
    M "I know I shouldn't have let some loosey doosey detective snoop around my place"
    M "What could you have possibly taken as evidence for your claim?"
    menu:
        "You clearly..."
        "wanted to get my grandmother fired":
            jump sir_accusation_grandma_fired
        "Weren't home on the 27th":
            jump sir_accusation_not_home
        "had an affair and wanted your wife dead":
            jump sir_accusation_affair

label sir_accusation_affair:
    if (knows_affair):
        M "But if I wasn't here, I could not have murdered my wife you idiot"
        show detective wrong at left: 
            zoom 0.5
            yalign 0.64
        P "Guess I missed that"
        show detective normal at left: 
            zoom 0.5
            yalign 0.64
        jump sir_accusation_evidence
    else: 
        jump sir_accusation_evidence

label sir_accusation_grandma_fired:
    M "If I wanted your grandmother fired, I would have just fired her"
    P "You were scared of her, since she could easily beat you up"
    M "Nonsense"    
    jump sir_accusation_evidence

label sir_accusation_not_home:
    M "But if I wasn't home, then I could not have murdered my wife?"
    M "You seem to be confused"
    show detective wrong at left: 
            zoom 0.5
            yalign 0.64
    if (knows_affair):
        jump sir_accusation_evidence
    else:
        jump sir_accusation_evidence

label sir_accusation_evidence:
    call screen pickevidence
    $ ret = _return
    if (ret=="Calendar"):
        jump sirs_affair

label butler_accusation:
    #show Butler suprised
    B "Wait, you think I murdered Lady Gold?"
    #show Butler default
    B "I seriously hope you are in your right mind, Detective"
    menu:
        B "I invited you to this place so you could defend your grandma, why would I have done that if I murdered her"
        "You were framing Sir Gold instead!":
            jump butler_accusation_sir_gold
        "You were trying to bring me down too!":
            $ butler_accusation_score = butler_accusation_score-1
            jump butler_accusation

label butler_accusation_sir_gold:
    show butler shocked at right: 
            zoom 0.5
            yalign 0.64
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
    show butler normal at right: 
            zoom 0.5
            yalign 0.64
    call screen pickevidence
    B "Sorry, but that is not at all evidence he was sleeping!"
label witness_evidence:
    show butler normal at right: 
            zoom 0.5
            yalign 0.64
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
        show butler shocked at right: 
            zoom 0.5
            yalign 0.64
        B "Oh I guess he couldn't have done it then"
        $ butler_accusation_score = butler_accusation_score + 2
        jump butler_accusation_outsider
    else:
        show butler normal at right: 
            zoom 0.5
            yalign 0.64
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
    show detective wrong at left: 
            zoom 0.5
            yalign 0.64
    P "Oh yeah, I forgot"
    jump butler_accusation_grandma

label butler_accusation_grandma:
    show detective normal at left: 
            zoom 0.5
            yalign 0.64
    B "I guess then it must have been your Grandma I truely am sorry."
    show detective wrong at left: 
            zoom 0.5
            yalign 0.64
    P "How dare you"
    show detective normal at left: 
            zoom 0.5
            yalign 0.64
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
    show detective wrong at left: 
            zoom 0.5
            yalign 0.64
    P "I guess I missed that"
    show detective normal at left: 
            zoom 0.5
            yalign 0.64
    $ butler_accusation_score = butler_accusation_score-3
    jump butler_accusation_conclusion

label butler_accusation_mafia:
    B "The Mafia?"
    P "The Mafia!"
    menu:
        P "And proof for that is"
        "the tattoo you have on your hand":
            jump butler_accusation_tatoo
        "the tattoo you have on your foot":
            jump butler_accusation_tatoo
        "your earrings":
            jump butler_accusation_final_proof

label butler_accusation_tatoo:
    B "I have no tatoos anywhere on my body, what are you talking about?"
    jump butler_accusation_final_proof

label butler_accusation_final_proof:
    B "Do you have any concrete evidence that I murdered her?"
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
    return