"""
story.py — Narrative for the Numbers skill pack.

Nell and Puck venture into a magical counting kingdom to learn math.
"""

INTRO_STORY = """
[bold yellow]THE COUNTING KINGDOM[/bold yellow]

Puck zipped to a new page in the Primer.

[bold cyan]"Now that you can read the words,"[/bold cyan] Puck said, [bold cyan]"it's time
to learn the other language. The one that describes how many,
how much, how far, how long."[/bold cyan]

[bold white]"Numbers?"[/bold white]

[bold cyan]"Numbers!"[/bold cyan] Puck spun in a happy circle. [bold cyan]"Numbers are everywhere —
every time you count cookies, read a clock, save up money,
or figure out if your backpack is too heavy. Understanding
numbers means understanding [italic]how things work.[/italic]"[/bold cyan]

The page turned to reveal a bright, colorful kingdom.
Rolling hills covered in giant numbered stones.
A river counting off the seconds.
A town where every shop had a sign with a number on it.

[bold cyan]"The Counting Kingdom,"[/bold cyan] Puck said proudly. [bold cyan]"I built it myself.
Well — the Primer did. But I helped."[/bold cyan]

Nell looked out at the numbered hills and took a deep breath.

[bold white]Here we go.[/bold white]
"""

ZONE_INTROS = {
    "counting_hills": """
Puck landed on the first hill, which had a big stone [bold yellow]1[/bold yellow] on top.

[bold cyan]"Counting seems simple,"[/bold cyan] Puck said, [bold cyan]"but it's the foundation of
everything else. Once you can count to 100, you can understand
[italic]any[/italic] amount of anything."[/bold cyan]

Numbers stretched across the hills as far as Nell could see.

[bold white]Count carefully. Don't skip any![/bold white]
""",
    "addition_meadow": """
Two paths through a meadow joined into one.

[bold cyan]"Addition,"[/bold cyan] Puck said, [bold cyan]"is just counting two groups together.
You don't need anything fancy — if you can count, you can add.
And once you can add, you can [italic]build[/italic] things."[/bold cyan]

[bold white]What happens when we put groups together?[/bold white]
""",
    "subtraction_valley": """
Puck led the way into a valley where numbers shrank as you walked.

[bold cyan]"Subtraction is addition's twin,"[/bold cyan] Puck said. [bold cyan]"When you add,
you combine. When you subtract, you take away. Both are
ways of understanding change."[/bold cyan]

[bold white]Take away carefully — how much is left?[/bold white]
""",
    "shape_forest": """
The trees in this forest all had shapes — triangles, squares,
circles, rectangles, hexagons — some shining like stained glass.

[bold cyan]"Shapes are everywhere,"[/bold cyan] Puck said. [bold cyan]"Every building, every piece
of food, every window — all shapes. Once you name them,
you'll see them in everything."[/bold cyan]

[bold white]Name the shapes. Count their sides.[/bold white]
""",
    "time_tower": """
A great clock tower rose from the center of the kingdom.

[bold cyan]"Time,"[/bold cyan] Puck said solemnly, [bold cyan]"is the most important number of all.
Everyone gets the same amount of it each day — twenty-four hours.
Understanding the clock means understanding your day."[/bold cyan]

The clock hands ticked. The numbers waited.

[bold white]Can you read the time?[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "counting_hills": """
[bold green]The hills are counted![/bold green]

Every numbered stone glows as Nell walks past. One, two, three...
all the way up the hills and back down.

[bold cyan]"You've got it,"[/bold cyan] Puck cheers. [bold cyan]"Counting is in your bones now!
The meadow is next — let's see what happens when we
put groups together."[/bold cyan]
""",
    "addition_meadow": """
[bold green]The meadow blooms![/bold green]

The two paths are one now, and the flowers are twice as bright.

[bold cyan]"Addition!"[/bold cyan] Puck does a little spin. [bold cyan]"3 + 4 = 7. 6 + 8 = 14.
You know it now — it lives in your head, ready whenever you need it."[/bold cyan]

The valley below calls. Something is about to be taken away...
""",
    "subtraction_valley": """
[bold green]The valley balances![/bold green]

Addition and subtraction sit on opposite sides of Nell, both nodding.

[bold cyan]"Add and subtract,"[/bold cyan] Puck says. [bold cyan]"Two sides of the same idea.
You now understand both. The forest of shapes is ahead —
and shapes have [italic]sides[/italic] too!"[/bold cyan]
""",
    "shape_forest": """
[bold green]The forest glows with shapes![/bold green]

Every tree shows off its shape: 3 sides, 4 sides, 6 sides!
Circles with no sides at all, just endless curve.

[bold cyan]"Geometry!"[/bold cyan] Puck announces proudly. [bold cyan]"Shapes are just math
you can see. And now you can see them everywhere."[/bold cyan]

The clock tower stands ahead, its hands still moving...
""",
    "time_tower": """
[bold green]The clock tower chimes![/bold green]

The big bell rings out the hour, and Nell reads it perfectly.

[bold cyan]"You can read the clock,"[/bold cyan] Puck says quietly. [bold cyan]"Do you know what
that means? It means you're in charge of your own time now.
You know when things start, when they end, and how long
you have."[/bold cyan]

[bold white]That is a powerful thing to know.[/bold white]
""",
}

BOSS_INTROS = {
    "counting_hills": "The biggest hill has a stone with [bold yellow]100[/bold yellow] on it. [bold yellow]\"Count all the way to here — without skipping!\"[/bold yellow]",
    "addition_meadow": "Two large groups of flowers merge in a big burst of color. [bold yellow]\"Bigger numbers now! Can you add them?\"[/bold yellow]",
    "subtraction_valley": "A large pile shrinks quickly. [bold yellow]\"How much is left when you take a big number away?\"[/bold yellow]",
    "shape_forest": "A many-sided shape hovers in the air, sparkling. [bold yellow]\"Count every side — what shape is this?\"[/bold yellow]",
    "time_tower": "The clock shows a tricky time. [bold yellow]\"Read the clock — what time is it exactly?\"[/bold yellow]",
}
