label prologue:
    call prologue_00 from _prologue_00
    call prologue_01 from _prologue_01

    # present route choice and jump to route's main global label

    return

# ----------------------------
# --- PROLOGUE MAIN LABELS ---
# ----------------------------
label prologue_00:
    scene bg game 3
    with fade

    """
    The invitation told me to go here, but...

    I don't see anyone yet

    ...
    """

    show payne picrew 2 at halfsize, rightcenter
    with fade

    "There's someone standing in the corner!" with hpunch

    """
    I almost didn't see him... Did he not see me yet?

    I walk closer curiously.
    """

    show payne picrew 2 at truecenter
    with fade

    "When I was close enough to him and could observe his face, I saw that he was looking at me."

    menu:
        mc "..!!"

        "Who are you?":
            call .choice_0
            return

        "H-Hi, are you here for the game testing too?":
            jump .choice_1
            return

    return

label .choice_0:
    payne "Oh hi, didn't notice I was staring in your direction, m'sorry!"
    payne "The name's Payne, are you also here for testing the new escape room?"

    """
    He doesn't seem too bad, actually

    He sounds a lot less scary than he looks
    """

    mc "Yeah, I am! And nice to meet you, I'm [mcname]"
    return

label .choice_1:
    payne "Ah, sorry, I must've been staring in your direction"
    payne "Yes, I'm here for the escape room as well!"
    payne "A friend recommended it to me, even though I'm not that into these types of things, they seem pretty interesting"

    """
    He doesn't seem so scary after all, but is he a first timer?
    
    I thought they would only invite people that know their way around
    """

    mc "They are interesting for sure! I like them a lot and am a bit of an expert on them, so I can help out when needed!"
    payne "*laughs nervously* Hahaha yeah, thanks, we'll count on you then"
    return
# ----------------------------

# ----------------------------
label prologue_01:

    payne "Seems like we're the only ones here at the moment"
    payne "Let's wait for the other participants, shall we?"
    payne "We can introduce ourselves to the others too when they're all here"

    hide payne picrew 2
    show zak picrew 2 at leftcenter
    show rye picrew 2 at rightcenter

    zak "What the hell... didn't think the company would send me here to play a stupid game with *kids*"
    rye "Hey, old man, I'm not a kid!" with hpunch
    zak "*sigh*"

    hide zak picrew 2
    hide rye picrew 2
    show keath picrew 2 at truecenter

    keath "HI BITCHES"

    return