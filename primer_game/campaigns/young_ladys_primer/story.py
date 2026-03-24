"""
story.py — Campaign narrative for The Young Lady's Illustrated Primer.
"""

CAMPAIGN_INTRO = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]

Once upon a time, in a world that was big and sometimes confusing,
a little girl found a very special book.

It was the color of midnight blue, with tiny gold stars on the cover
that sparkled in the light. When she opened it, a small glowing creature
floated up from between the pages.

[bold cyan]"Hello!"[/bold cyan] it said. [bold cyan]"My name is Puck.
And this book — [italic]this[/italic] book — is for you."[/bold cyan]

The girl blinked. [bold white]"For me? Why?"[/bold white]

[bold cyan]"Because you're going to grow up in a world full of things
to know. And the more you know, the freer you'll be.
Free to go where you want. Free to do what you love.
Free to help the people you care about."[/bold cyan]

Puck floated closer and looked her in the eyes.

[bold cyan]"The Primer will teach you. Not just facts — [italic]how to think.[/italic]
How to read every word anyone has written. How to add up
what's real. How to understand the world well enough to
[italic]change it[/italic] if you decide to."[/bold cyan]

The girl looked at the first page.

[bold white]"Where do we start?"[/bold white]

[bold cyan]"At the beginning,"[/bold cyan] Puck said, smiling. [bold cyan]"With the letters."[/bold cyan]

[bold white]Are you ready?[/bold white]
"""

CHAPTER_INTROS = {
    "letters": """
Puck opened the Primer to the very first page.

[bold cyan]"Every word ever written — every story, every recipe, every letter
someone sent to someone they loved — it all starts here.
With twenty-six marks. Twenty-six letters."[/bold cyan]

The page glowed with color. Letters danced gently, each one
in its own bright light.

[bold cyan]"Learn these, and you can read [italic]anything.[/italic]"[/bold cyan]

[bold white]The Letter Garden is waiting. Puck will be right beside you.[/bold white]
""",
    "numbers": """
[bold cyan]"You can read,"[/bold cyan] Puck said proudly. [bold cyan]"Now let's add numbers."[/bold cyan]

The Primer opened to a new section — bright and colorful, with
a golden kingdom stretching across the pages.

[bold cyan]"Numbers are another language. They describe [italic]how many,[/italic]
[italic]how much,[/italic] [italic]how far,[/italic] [italic]how long.[/italic]
When you understand numbers, you understand the world more completely."[/bold cyan]

Nell looked out at the Counting Kingdom and felt curious.
She'd always liked counting things.

[bold white]The numbers are waiting. Let's explore the kingdom![/bold white]
""",
    "science": """
[bold cyan]"You can read and you understand numbers,"[/bold cyan] Puck said.
[bold cyan]"Now — look around you. What do you [italic]see?[/italic]"[/bold cyan]

The Primer opened to a page full of color and light.
A garden. A sky. A body. A workshop with gears turning.

[bold cyan]"The world runs on rules. Once you learn the rules,
everything stops being random and starts being [italic]wonderful.[/italic]
Scientists aren't special people — they're just people who
kept asking [italic]why[/italic] and wouldn't stop until they found out."[/bold cyan]

[bold white]The World of Wondering is waiting. Let's explore![/bold white]
""",
    "kindness": """
[bold cyan]"You've been learning about the world outside you,"[/bold cyan]
Puck said. [bold cyan]"Now let's learn about the world [italic]between[/italic] people."[/bold cyan]

The Primer turned to its warmest pages yet.
A garden of feelings. A kitchen full of kind actions.
A forest where friendships grow.

[bold cyan]"Everything you've learned so far helps you understand things.
This chapter teaches you how to [italic]be[/italic] with people.
How to make them feel seen. How to make things better.
How to be the kind of person that others are glad to know."[/bold cyan]

[bold white]The kindness chapter is waiting. This one matters most.[/bold white]
""",
}

CHAPTER_OUTROS = {
    "letters": """
The Letter Garden glows with every color of the alphabet.

[bold cyan]"You did it,"[/bold cyan] Puck says quietly. [bold cyan]"You can read.
Not just letters — words. Not just words — sentences.
Not just sentences — [italic]meaning.[/italic]"[/bold cyan]

Puck does a slow, happy spin.

[bold cyan]"From now on, every sign, every book, every note someone
leaves for you — you'll be able to read it. That's a gift
that never goes away."[/bold cyan]

[bold white]The Counting Kingdom shimmers in the distance. Numbers are next.[/bold white]
""",
    "numbers": """
The Counting Kingdom glows at every corner — numbered hills,
full meadows, shapes in every tree, the great clock tower chiming.

[bold cyan]"You understand numbers now,"[/bold cyan] Puck says.
[bold cyan]"You can count, add, subtract. You know shapes.
You can read a clock."[/bold cyan]

Puck pauses.

[bold cyan]"Those aren't small things. Those are the building blocks
of science, of money, of time, of [italic]everything.[/italic]"[/bold cyan]

[bold white]The world of wondering is waiting — science is next![/bold white]
""",
    "science": """
The world is humming with questions answered and mysteries understood.
Living things, weather, the body, how things work.

[bold cyan]"You're a scientist now,"[/bold cyan] Puck says with pride.
[bold cyan]"Not because you know everything — because you know [italic]how to ask.[/italic]
Why does this happen? What's the pattern? How does it work?
Those questions are the engine of all human knowledge."[/bold cyan]

A warm glow. A turning page.

[bold white]Now for the most important chapter of all — kindness.[/bold white]
""",
    "kindness": """
The garden glows. The kitchen is warm. The friendship forest stands tall.
The bridge of solutions stretches across calm water.

[bold cyan]"You did it,"[/bold cyan] Puck says quietly.
[bold cyan]"You learned the feelings. You practiced the actions.
You understood what friendship really means.
And you found out what to do when things get hard."[/bold cyan]

A long pause.

[bold cyan]"Those aren't small things.
Those are [italic]everything.[/italic]"[/bold cyan]
""",
}

CAMPAIGN_FINAL = """
[bold yellow]★ ★ ★  THE PRIMER IS YOURS  ★ ★ ★[/bold yellow]

[bold white]The Young Lady's Illustrated Primer.[/bold white]

You can read. Every word ever written is yours now.

You understand numbers. The world of quantity, shape, and time is yours.

You know how the world works. Living things, weather, your own body,
cause and effect — yours.

And you know how to be kind. How to feel your feelings,
care for others, be a true friend, and handle hard moments with grace.

[bold cyan]Puck floated up slowly, glowing a little brighter than usual.[/bold cyan]

[bold cyan]"Four things,"[/bold cyan] Puck said. [bold cyan]"Most people learn them slowly, over a lifetime.
You've started on all four, and that beginning is everything."[/bold cyan]

The Primer hummed.

[bold cyan]"There's more inside — always more inside.
But today? Today you have what you need to start
[italic]becoming whoever you want to be.[/italic]"[/bold cyan]

[italic]The best adventures always have a next chapter.[/italic]
[italic]You just have to keep turning the pages.[/italic]

[bold white]This one is yours.[/bold white]

[bold cyan]Well done. — Puck[/bold cyan]
"""
