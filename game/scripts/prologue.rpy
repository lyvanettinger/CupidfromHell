label prologue:
    # can these calls be automated somehow? just need the amount of labels in a chapter and loop over them
    call prologue_scene_01 from _prologue_scene_01
    call prologue_scene_02 from _prologue_scene_02
    call prologue_scene_03 from _prologue_scene_03
    call prologue_scene_04 from _prologue_scene_04

    # present route choice and jump to route's main global label
    "End game."

    return

# ----------------------------
# --- PROLOGUE MAIN LABELS ---
# ----------------------------
label prologue_scene_01:
    # scene 1: (show hand holding letter OR just the letter on a table/the envelope it came inside of)
    # narrator briefs the letter MC got for the escape room testing
    # something along the lines of: MC, <insert well known company name> has recognized your exceptional puzzle solving skills and would like to formally invite you
    # to a test run of our new escape room establishment. as it's currently in development, please do not disclose any information regarding this test and letter
    # to anyone

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

    return
# ----------------------------

# ----------------------------
label prologue_scene_02:
    # scene 2: (shows receptionist desk inside love hotel)
    # MC is on her way to the escape room location. she gets to the address and it's.... a love hotel?!?!?!?
    # what the hell, of all places, this is where they're holding the escape room testing?? MC hesitantly goes inside and talks to the receptionist, showing them the letter
    # the receptionist tells MC to take the elevator down to the -2 floor

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
# ----------------------------

# ----------------------------
label prologue_scene_03:
    # scene 3: (shows waiting room for escape room; chairs and escape room entrance doors closed/open depending)
    # MC steps out of the elevator and enters the waiting room. She's the third to arrive there. A grumpy businessman was already sitting in one of the chairs in the waiting room,
    # scrolling his phone. another man, more casually dressed, stood across from him, taking in a spot where he had view over the entire room and the elevator doors.
    # there was an ominous atmosphere in the air, the two men didn't seem particularly sociable. MC awkwardly takes place in the waiting room
    # (timeskip)
    # the elevator moves again and opens with a ding, revealing a man around MC's age. He loudly announces himself to the room and MC can feel her nerves calming, happily greeting him
    # the man standing also greets him with a short "good day" and kurt nod, while the businessman only looks up from his phone briefly.
    # MC gets up and makes small talk with the new guy, he seems excited for the escape room testing.
    # (very small timeskip)
    # the escaperoom doors open and a cute little creature blob (Keath's familiar) shows up, welcoming all the contestants, introducing itself as Lili.
    # it wishes everyone good luck and, before everyone goes inside, tells them the girl among them (MC) should enter first. everyone looks at MC.
    # the cute creature leaves and MC enters the escape room first alone

    """
    (Insert long waiting room scene)
    """

    return
# ----------------------------

# ----------------------------
label prologue_scene_04:
    # scene 4: (shows dark background with choice menu of 3 buttons/levers)
    # MC enters the escape room first alone, the doors close briefly. the cute creature's voice can be heard telling her to choose one out of three buttons/levers. this will
    # determine the character route, as Keath will fire an arrow into that person's heart to aid in falling in love with MC.
    # symbols on buttons/underneath levers:
    # blue Stats/stonks? energy drink can with 6? Zak
    # yellow graceful lady hat? double mask? Rye
    # green crosshair? paper with knife through? Payne

    """
    [mcname] enters the escape room and the doors closed behind me with a bang.

    It's pitch black inside..

    After a while, 3 buttons light up in front of [mcname].
    """

    mc "Is this the first puzzle?"
    mc "..."

    """
    [mcname] feels around her to see if there's anything else worth of note in the room.
    """

    mc "There seems to be nothing else around."
    mc "I guess I'll have to push one of them."

    menu: # implement slightly differently organized choice menu, listing them horizontally instead of vertical, with image buttons
        mc "..which button should I push?"

        "Blue":
            jump .choice_1
            return

        "Yellow" if False: # not yet implemented
            jump .choice_2
            return

        "Green" if False: # not yet implemented
            jump .choice_3
            return

    return

label .choice_1:
    "Go on Zak's route"
    jump zak_route
    return

label .choice_2:
    "Go on Rye's route"
    return

label .choice_3:
    "Go on Payne's route"
    return
# ----------------------------