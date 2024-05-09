# Game script

# --- CHARACTERS ---
# MC
define mc = Character("[mcname]")
define you = Character("You")
# Love Interests
define zak = Character("Zak")
define payne = Character("Payne")
define rye = Character("Rye")
define keath = Character("Keath")

# --- CUSTOM TRANSFORMS ---
# Size
transform halfsize: 
    zoom 0.5
transform doublesize:
    zoom 2.0
# Placement
transform leftcenter:
    xalign 0.15
    yalign 0.5
transform rightcenter:
    xalign 0.85
    yalign 0.5

# --- GAME START ---
label start:
    stop music fadeout 1.0
    # player enters name
    python:
        mcname = renpy.input("Before you enter into hell, write down your name", length=32)
        mcname = mcname.strip()

        if not mcname:
            mcname = "You"

    # game start
    jump prologue

    #game ends
    return