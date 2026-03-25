"""
story.py — Narrative for The Time Traveler's Primer (history skill pack).
"""

INTRO_STORY = """
[bold cyan]A New Page Appears in the Primer...[/bold cyan]

Puck floats over to a page that seems to shimmer with age.

[bold yellow]"Oh!"[/bold yellow] Puck breathes. [bold yellow]"This one is special."[/bold yellow]

The page is covered in tiny illustrations: pyramids, tall ships, airplanes,
people marching arm in arm, a boy with a telescope looking at the stars.

[bold yellow]"This is the history chapter,"[/bold yellow] Puck says softly.
[bold yellow]"It's about all the people who came before you. The things they built.
The journeys they took. The mistakes they made — and what they learned."[/bold yellow]

You touch the page, and suddenly the illustrations start moving.

[bold yellow]"History isn't just facts and dates,"[/bold yellow] Puck says.
[bold yellow]"It's people. Real people — who were brave, and scared, and curious,
and sometimes wrong, and sometimes remarkable.
Just like you."[/bold yellow]

[bold white]The page glows. Time begins to move.[/bold white]

[italic]"Those who cannot remember the past are condemned to repeat it." — George Santayana[/italic]
"""

ZONE_INTROS = {
    "ancient_civilizations": (
        "[bold cyan]THE ANCIENT WORLD[/bold cyan]\n\n"
        "Puck flutters around images of pyramids and marble temples.\n"
        "[bold yellow]'Before phones, before cars, before even books — people built incredible things. "
        "Cities! Writing! Democracy! Let's visit the very first great civilizations.'[/bold yellow]"
    ),
    "explorers_and_discoveries": (
        "[bold cyan]THE AGE OF EXPLORATION[/bold cyan]\n\n"
        "A tiny ship appears on the page, setting sail into unknown waters.\n"
        "[bold yellow]'Imagine getting on a boat and sailing toward the horizon, "
        "not knowing what you'd find. These explorers did exactly that. "
        "And what they found changed the world forever.'[/bold yellow]"
    ),
    "inventions_and_inventors": (
        "[bold cyan]THE INVENTION WORKSHOP[/bold cyan]\n\n"
        "Light bulbs and blueprints float across the page.\n"
        "[bold yellow]'Every invention started with someone saying: what if this was possible? "
        "The printing press. The telephone. The airplane. The internet. "
        "One idea — and nothing was ever the same.'[/bold yellow]"
    ),
    "world_wars": (
        "[bold cyan]THE GREAT CONFLICTS[/bold cyan]\n\n"
        "Puck's glow dims slightly. [bold yellow]'This chapter is about something hard. "
        "Two wars that changed everything — and cost millions of lives. "
        "We study them not to celebrate war, but to understand it. "
        "And to make sure we do better.'[/bold yellow]"
    ),
    "american_history": (
        "[bold cyan]THE AMERICAN STORY[/bold cyan]\n\n"
        "An eagle soars across the page. [bold yellow]'America is a country built on a promise: "
        "that all people are created equal. "
        "Sometimes that promise was broken. But people kept fighting to keep it. "
        "That fight is still happening today.'[/bold yellow]"
    ),
    "world_leaders_and_change": (
        "[bold cyan]THE COURAGE CHAPTER[/bold cyan]\n\n"
        "Puck glows warmly. [bold yellow]'These are the people who looked at something unfair "
        "and said: I will not accept this. They were not born powerful. "
        "They became powerful through courage. "
        "And because of them, the world is better.'[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "ancient_civilizations": (
        "[bold green]ZONE COMPLETE — THE ANCIENT WORLD![/bold green]\n\n"
        "You've visited Egypt, Greece, Rome, and Mesopotamia. "
        "[bold yellow]Puck claps. 'Those civilizations built the foundation for almost everything!'[/bold yellow]"
    ),
    "explorers_and_discoveries": (
        "[bold green]ZONE COMPLETE — AGE OF EXPLORATION![/bold green]\n\n"
        "The brave explorers are honored. "
        "[bold yellow]'They didn't know what they'd find,' Puck says. 'But they went anyway. That takes courage.'[/bold yellow]"
    ),
    "inventions_and_inventors": (
        "[bold green]ZONE COMPLETE — THE INVENTION WORKSHOP![/bold green]\n\n"
        "Every invention remembered. "
        "[bold yellow]'You know what's amazing?' Puck says. 'Every one of those inventors was told it was impossible first.'[/bold yellow]"
    ),
    "world_wars": (
        "[bold green]ZONE COMPLETE — THE GREAT CONFLICTS[/bold green]\n\n"
        "A heavy chapter, completed with care. "
        "[bold yellow]Puck is quiet for a moment. 'Thank you for taking this seriously. That's what history deserves.'[/bold yellow]"
    ),
    "american_history": (
        "[bold green]ZONE COMPLETE — THE AMERICAN STORY![/bold green]\n\n"
        "The Declaration, the Constitution, the Civil War, civil rights, and suffrage. "
        "[bold yellow]'America is still becoming what it promised to be,' Puck says. 'And that work belongs to you too.'[/bold yellow]"
    ),
    "world_leaders_and_change": (
        "[bold green]ZONE COMPLETE — THE COURAGE CHAPTER![/bold green]\n\n"
        "The great leaders remembered and celebrated. "
        "[bold yellow]Puck glows gold. 'One day, someone will be learning about the change YOU made. I believe that.'[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "ancient_civilizations": (
        "[bold red]BOSS CHALLENGE — ANCIENT CIVILIZATIONS QUIZ[/bold red]\n\n"
        "[bold yellow]'Puck shuffles the civilizations! Can you match each to its greatest achievement? No hints this time — you know this!'[/bold yellow]"
    ),
    "explorers_and_discoveries": (
        "[bold red]BOSS CHALLENGE — THE GREATEST JOURNEY[/bold red]\n\n"
        "[bold yellow]'Who did what? The explorers are all mixed up. Show Puck you can tell them apart!'[/bold yellow]"
    ),
    "inventions_and_inventors": (
        "[bold red]BOSS CHALLENGE — INVENTION TIMELINE[/bold red]\n\n"
        "[bold yellow]'Can you figure out which invention came FIRST in history? Think carefully!'[/bold yellow]"
    ),
    "world_wars": (
        "[bold red]BOSS CHALLENGE — PEACE AND JUSTICE[/bold red]\n\n"
        "[bold yellow]'This is the most important question in the whole chapter. Think about WHY we study these wars.'[/bold yellow]"
    ),
    "american_history": (
        "[bold red]BOSS CHALLENGE — THE AMERICAN PROMISE[/bold red]\n\n"
        "[bold yellow]'The Constitution has been amended many times to expand freedom. Which amendment was most important for ending slavery?'[/bold yellow]"
    ),
    "world_leaders_and_change": (
        "[bold red]BOSS CHALLENGE — THE COMMON THREAD[/bold red]\n\n"
        "[bold yellow]'Puck asks the deepest question: what connects Gandhi, Mandela, Malala, Roosevelt, and King?'[/bold yellow]"
    ),
}
