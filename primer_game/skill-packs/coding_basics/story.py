"""
story.py — Narrative for The Code Garden (Coding Basics) skill pack.
"""

INTRO_STORY = """
[bold cyan]Welcome to The Code Garden![/bold cyan]

Puck flutters down onto a workbench covered in gears, buttons, and blinking lights.

[bold yellow]"Oh! Oh! You came just in time!"[/bold yellow] Puck squeaks.
[bold yellow]"The Garden is full of wonderful machines — but nobody taught them what to DO!"[/bold yellow]

You look around. A little robot stands frozen in the middle of a path.
A sorting machine has stopped halfway through a pile of colorful shapes.

[bold yellow]"Machines need INSTRUCTIONS. Without them, they just... sit there."[/bold yellow]

Puck spins happily. [bold yellow]"And that's what coding is! Giving machines clear, step-by-step instructions so they can do amazing things!"[/bold yellow]

[bold white]"So I'm going to be a programmer?"[/bold white]

[bold yellow]"YOU'RE going to be a CODE GARDENER! You'll learn how programs think, how they remember things, how they make choices... and how to grow ideas into instructions!"[/bold yellow]

The frozen robot blinks, waiting.
Let's wake it up.
"""

ZONE_INTROS = {
    "what_is_coding": (
        "[bold cyan]THE CODE WORKSHOP[/bold cyan]\n\n"
        "Puck points to the frozen robot. [bold yellow]'Before we can fix anything, "
        "we need to understand: what IS a program? What IS coding? "
        "Let's start from the very beginning!'[/bold yellow]"
    ),
    "sequences_loops": (
        "[bold cyan]THE LOOP BRIDGE[/bold cyan]\n\n"
        "[bold yellow]'Sometimes we need to do the same thing over and over again. "
        "Like brushing every tooth, or watering every plant in a row. "
        "That's called a LOOP! Loops save time — and make programs much shorter!'[/bold yellow]"
    ),
    "conditionals": (
        "[bold cyan]THE CHOICE CROSSROADS[/bold cyan]\n\n"
        "[bold yellow]'Puck lands at a fork in the path. "
        "'Programs have to make DECISIONS. If it's raining, take an umbrella. "
        "If not, leave it home. An IF statement lets a program choose what to do!'[/bold yellow]"
    ),
    "variables": (
        "[bold cyan]THE MEMORY MEADOW[/bold cyan]\n\n"
        "[bold yellow]'Computers need to remember things while they work. "
        "A variable is like a little box with a label on it — "
        "you put a value inside, give it a name, and you can use it later!'[/bold yellow]"
    ),
    "functions": (
        "[bold cyan]THE FUNCTION FACTORY[/bold cyan]\n\n"
        "[bold yellow]'What if you need to do the same set of steps in lots of different places? "
        "You could write them out every time... OR you could put them in a FUNCTION! "
        "Name it once, use it anywhere!'[/bold yellow]"
    ),
    "creative_computing": (
        "[bold cyan]THE INVENTION GARDEN[/bold cyan]\n\n"
        "[bold yellow]'You've learned how programs think. Now it's time to put it all together! "
        "Real coders combine sequences, loops, conditionals, variables, and functions "
        "to build things that have never existed before. Let's invent!'[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "what_is_coding": (
        "[bold green]ZONE COMPLETE — THE CODE WORKSHOP![/bold green]\n\n"
        "You understand what a program is and how computers follow instructions. "
        "The frozen robot gives a happy beep. [bold yellow]'Great start! '[/bold yellow]"
    ),
    "sequences_loops": (
        "[bold green]ZONE COMPLETE — THE LOOP BRIDGE![/bold green]\n\n"
        "Loops make sense now! Instead of writing the same thing 100 times, "
        "one loop does it all. Puck does a little dance. [bold yellow]'So efficient!'[/bold yellow]"
    ),
    "conditionals": (
        "[bold green]ZONE COMPLETE — THE CHOICE CROSSROADS![/bold green]\n\n"
        "Programs can now think for themselves — choosing the right path "
        "based on what's true. [bold yellow]'Now THAT is a smart program!'[/bold yellow]"
    ),
    "variables": (
        "[bold green]ZONE COMPLETE — THE MEMORY MEADOW![/bold green]\n\n"
        "Variables stored and retrieved perfectly. The program's memory is sharp. "
        "[bold yellow]'Nothing forgotten!'[/bold yellow]"
    ),
    "functions": (
        "[bold green]ZONE COMPLETE — THE FUNCTION FACTORY![/bold green]\n\n"
        "Functions built and ready to use anywhere. No repeated code, no wasted effort. "
        "[bold yellow]'You're thinking like a real coder!'[/bold yellow]"
    ),
    "creative_computing": (
        "[bold green]ZONE COMPLETE — THE INVENTION GARDEN![/bold green]\n\n"
        "Every concept connected, every idea transformed into logic. "
        "The Code Garden is fully awake! "
        "[bold yellow]'You did it! You're a CODE GARDENER!'[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "what_is_coding": (
        "[bold red]BOSS CHALLENGE — THE PROGRAM PUZZLE[/bold red]\n\n"
        "[bold yellow]'Time to show you really understand what a program is. "
        "No hints — just you and what you've learned!'[/bold yellow]"
    ),
    "sequences_loops": (
        "[bold red]BOSS CHALLENGE — THE INFINITE LOOP BEAST[/bold red]\n\n"
        "[bold yellow]'A loop gone wrong can run forever! "
        "Show me you know how loops START, how they RUN, and how they STOP.'[/bold yellow]"
    ),
    "conditionals": (
        "[bold red]BOSS CHALLENGE — THE BIG DECISION[/bold red]\n\n"
        "[bold yellow]'A complex IF... ELSE IF... ELSE chain. "
        "Think it through one step at a time. What happens in each case?'[/bold yellow]"
    ),
    "variables": (
        "[bold red]BOSS CHALLENGE — THE VARIABLE VAULT[/bold red]\n\n"
        "[bold yellow]'Multiple variables, changing values, and a tricky question at the end. "
        "Track every change carefully!'[/bold yellow]"
    ),
    "functions": (
        "[bold red]BOSS CHALLENGE — THE MASTER FUNCTION[/bold red]\n\n"
        "[bold yellow]'Design the perfect function. What does it take in? "
        "What does it give back? Show me you understand inputs and outputs!'[/bold yellow]"
    ),
    "creative_computing": (
        "[bold red]BOSS CHALLENGE — THE GARDEN GUARDIAN[/bold red]\n\n"
        "[bold yellow]'The final challenge combines EVERYTHING. "
        "A loop, a conditional, variables, and a function all working together. "
        "Think it through — you CAN do this!'[/bold yellow]"
    ),
}
