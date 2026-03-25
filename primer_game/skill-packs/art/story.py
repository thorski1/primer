"""
story.py — Narrative for The Art Studio skill pack.
"""

INTRO_STORY = """
[bold cyan]Puck fluttered to a doorway covered in colorful handprints.[/bold cyan]

[bold yellow]"Welcome,"[/bold yellow] Puck said, [bold yellow]"to the Art Studio."[/bold yellow]

Inside, every surface was covered with paintings, drawings, sculptures, and collages.
Colors everywhere. Brushes soaking in jars. Clay drying on wooden boards.

[bold yellow]"Art is the oldest language in the world,"[/bold yellow] Puck said quietly.
[bold yellow]"Before people had writing — before there were letters or numbers —
they drew pictures on cave walls to share what they'd seen, what they loved,
what they feared."[/bold yellow]

On one wall hung a copy of the Mona Lisa. On another, The Starry Night.
In the corner, a small clay figure looked like it was dancing.

[bold white]"Am I going to learn to paint like that?"[/bold white]

[bold yellow]"You're going to learn to SEE like that,"[/bold yellow] Puck said.
[bold yellow]"That's how all of it starts."[/bold yellow]

A blank canvas waited on an easel in the center of the room.

[bold white]The Studio is open. Let's explore![/bold white]
"""

ZONE_INTROS = {
    "colors_and_mixing": (
        "[bold cyan]THE COLOR GARDEN[/bold cyan]\n\n"
        "[bold yellow]'Every color in the world started as three,' Puck says, "
        "floating between jars of red, yellow, and blue paint. "
        "'Mix them. Blend them. Change them. "
        "From just three colors, the whole world is possible!'[/bold yellow]"
    ),
    "shapes_and_patterns": (
        "[bold cyan]THE PATTERN ROOM[/bold cyan]\n\n"
        "[bold yellow]'Look around you,' Puck says. 'Shapes everywhere. "
        "In tiles. In leaves. In windows. In fabric. "
        "Artists see the world as shapes — and patterns are shapes that dance together.'[/bold yellow]"
    ),
    "art_tools": (
        "[bold cyan]THE SUPPLY CLOSET[/bold cyan]\n\n"
        "[bold yellow]'A great artist knows their tools,' Puck says, opening a closet "
        "full of brushes, pencils, watercolors, and clay. "
        "'Let's find out what each one does — and what each one is best for.'[/bold yellow]"
    ),
    "famous_artwork": (
        "[bold cyan]THE GREAT GALLERY[/bold cyan]\n\n"
        "[bold yellow]'Come look,' Puck says. The walls of this room hold the most "
        "famous images in human history. "
        "'These pictures changed the world — or at least how people see it. "
        "Let's learn their names, their stories, and why they still matter.'[/bold yellow]"
    ),
    "art_elements": (
        "[bold cyan]THE ELEMENTS ROOM[/bold cyan]\n\n"
        "[bold yellow]'Every painting — every drawing — is built from the same things,' "
        "Puck says. 'Line. Shape. Color. Texture. Space. "
        "Once you can NAME them, you can use them on purpose. "
        "That is what separates art from accident.'[/bold yellow]"
    ),
    "famous_artists": (
        "[bold cyan]THE ARTISTS' HALL[/bold cyan]\n\n"
        "[bold yellow]'These are the people who changed what art could be,' Puck says. "
        "'A genius in Italy. A woman in Mexico. A boy from Brooklyn. "
        "They didn't just make pictures — they changed how the world saw itself.'[/bold yellow]"
    ),
}

ZONE_COMPLETIONS = {
    "colors_and_mixing": (
        "[bold green]ZONE COMPLETE — THE COLOR GARDEN![/bold green]\n\n"
        "Primary colors, secondary colors, warm and cool — you understand how color works. "
        "[bold yellow]'Every sunset, every painting, every rainbow — "
        "now you know the rules behind all of it!'[/bold yellow]"
    ),
    "shapes_and_patterns": (
        "[bold green]ZONE COMPLETE — THE PATTERN ROOM![/bold green]\n\n"
        "Shapes, symmetry, tessellations — you see the geometry in art now. "
        "[bold yellow]'Look at a tiled floor or a quilt and you'll never see it the same way again!'[/bold yellow]"
    ),
    "art_tools": (
        "[bold green]ZONE COMPLETE — THE SUPPLY CLOSET![/bold green]\n\n"
        "Pencils, watercolors, canvas, collage, perspective — the tools are no longer mysterious. "
        "[bold yellow]'Now you know what artists mean when they talk about their materials!'[/bold yellow]"
    ),
    "famous_artwork": (
        "[bold green]ZONE COMPLETE — THE GREAT GALLERY![/bold green]\n\n"
        "Mona Lisa, Starry Night, David, Water Lilies, Guernica — you know them now. "
        "[bold yellow]'These aren't just pictures. They're conversations across centuries.'[/bold yellow]"
    ),
    "art_elements": (
        "[bold green]ZONE COMPLETE — THE ELEMENTS ROOM![/bold green]\n\n"
        "Line, texture, foreground, contrast, negative space, proportion — "
        "the vocabulary of visual art is yours. "
        "[bold yellow]'Now you can TALK about what you see. That changes everything.'[/bold yellow]"
    ),
    "famous_artists": (
        "[bold green]ZONE COMPLETE — THE ARTISTS' HALL![/bold green]\n\n"
        "Da Vinci, Kahlo, Monet, O'Keeffe, Picasso, Basquiat — and now you. "
        "[bold yellow]'Everyone who ever made art started somewhere. "
        "Maybe this is where your story starts.'[/bold yellow]"
    ),
}

BOSS_INTROS = {
    "colors_and_mixing": (
        "[bold red]BOSS CHALLENGE — THE FULL COLOR WHEEL[/bold red]\n\n"
        "[bold yellow]'Name every primary color, every secondary color, "
        "and tell me which colors are warm and which are cool. "
        "The whole palette — no hints!'[/bold yellow]"
    ),
    "shapes_and_patterns": (
        "[bold red]BOSS CHALLENGE — THE MASTER PATTERN[/bold red]\n\n"
        "[bold yellow]'Symmetry, tessellation, organic vs geometric shapes — "
        "I'm going to test all of it. "
        "Show me you really understand how shapes work in art.'[/bold yellow]"
    ),
    "art_tools": (
        "[bold red]BOSS CHALLENGE — THE ARTIST'S CHOICE[/bold red]\n\n"
        "[bold yellow]'For each project, what tool is best? "
        "A portrait? A mosaic? A protest image? "
        "Explain your choices like a real artist would.'[/bold yellow]"
    ),
    "famous_artwork": (
        "[bold red]BOSS CHALLENGE — THE GALLERY GUIDE[/bold red]\n\n"
        "[bold yellow]'Pretend you are a museum guide. "
        "Tell me about every famous work we studied — "
        "who made it, when, and why it matters.'[/bold yellow]"
    ),
    "art_elements": (
        "[bold red]BOSS CHALLENGE — THE CRITICAL EYE[/bold red]\n\n"
        "[bold yellow]'Look at this painting in your mind: a stormy sky, "
        "a figure in the foreground, swirling lines, bold contrast. "
        "Name every element of art at work in it.'[/bold yellow]"
    ),
    "famous_artists": (
        "[bold red]BOSS CHALLENGE — THE ARTIST MATCH[/bold red]\n\n"
        "[bold yellow]'I will describe a style — you match it to an artist. "
        "Da Vinci to Basquiat. Every artist we met, every style we studied. "
        "Let's see if they stayed with you.'[/bold yellow]"
    ),
}
