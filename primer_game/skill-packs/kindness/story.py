"""
story.py — Narrative for the Kindness skill pack.

Nell and Puck explore feelings, friendship, and how to be a good person
in the world.
"""

INTRO_STORY = """
[bold yellow]THE ART OF BEING KIND[/bold yellow]

One afternoon, Nell saw a kid drop all her books.
Before she could think, Nell was already helping pick them up.

The kid smiled. [bold white]"Thank you."[/bold white]

It was a small thing. It took ten seconds.
But Nell noticed something: the small thing felt [italic]big.[/italic]

[bold cyan]"That,"[/bold cyan] Puck said from her pocket, [bold cyan]"is kindness.
And it might be the most important skill in the whole Primer."[/bold cyan]

[bold white]"More than reading? More than numbers?"[/bold white]

[bold cyan]"Reading and numbers help you understand the world.
Kindness helps you [italic]live in it.[/italic] With other people.
Happily. Most of the time."[/bold cyan]

Nell thought about the smile on the other kid's face.
And about how her own heart had felt warm for a minute after.

[bold cyan]"Kindness is a skill,"[/bold cyan] Puck said. [bold cyan]"You practice it.
You get better at it. And the more you use it,
the easier it becomes — and the better life gets
for everyone around you. And for you too."[/bold cyan]

[bold white]Ready to learn the art of being kind?[/bold white]
"""

ZONE_INTROS = {
    "feelings_garden": """
[bold cyan]"Before you can be kind to others,"[/bold cyan] Puck said,
[bold cyan]"you need to understand [italic]feelings.[/italic]
Your own, and other people's."[/bold cyan]

In a garden full of flowers, each one wore a different expression.
Happy flowers, sad flowers, surprised flowers, angry ones.

[bold cyan]"Every feeling has a name. Once you can name a feeling,
you understand it. And understanding it means you can deal with
it — and help other people deal with theirs."[/bold cyan]

[bold white]What is this feeling called?[/bold white]
""",
    "kindness_actions": """
[bold cyan]"Knowing what kindness is isn't enough,"[/bold cyan] Puck said.
[bold cyan]"You have to actually [italic]do[/italic] it."[/bold cyan]

A busy scene appeared — people helping, sharing, listening.
Some moments were big. Most were small.

[bold cyan]"The small moments are actually the most important ones.
Because they happen every day."[/bold cyan]

[bold white]What's the kind thing to do here?[/bold white]
""",
    "being_a_good_friend": """
Puck looked at Nell seriously.

[bold cyan]"Friendship is one of the best things in life.
But good friendships take work. They need honesty,
and patience, and paying attention to what the other
person actually needs — not just what you'd want
if you were them."[/bold cyan]

[bold white]What does a good friend do?[/bold white]
""",
    "solving_problems": """
[bold cyan]"Things go wrong,"[/bold cyan] Puck said. [bold cyan]"Always.
Someone says something hurtful. Plans fall apart.
Two people want the same thing. Feelings get hurt."[/bold cyan]

[bold cyan]"The question isn't whether problems happen —
it's [italic]what you do[/italic] when they do."[/bold cyan]

[bold white]What's the best way to handle this?[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "feelings_garden": """
[bold green]The garden blooms![/bold green]

Every flower has a name now — happy, sad, angry, scared, proud,
surprised, embarrassed, excited.

[bold cyan]"You can name what you feel now,"[/bold cyan] Puck says.
[bold cyan]"And when you can name it, you're in charge of it —
instead of it being in charge of you."[/bold cyan]

Now let's do something with those feelings. Kindness is next!
""",
    "kindness_actions": """
[bold green]The scene fills with warmth![/bold green]

Small acts, done well. A held door. A shared snack.
A listening ear. A genuine thank-you.

[bold cyan]"Every single one of those moments mattered,"[/bold cyan] Puck says.
[bold cyan]"You'll never know exactly how much — but they did."[/bold cyan]

Next up: what makes a good friendship?
""",
    "being_a_good_friend": """
[bold green]The friendship forest glows![/bold green]

[bold cyan]"Good friends show up,"[/bold cyan] Puck says. [bold cyan]"They listen.
They tell the truth kindly. They celebrate your wins
and sit with you when things are hard."[/bold cyan]

A pause.

[bold cyan]"And you know what? [italic]You[/italic] can be that friend."[/bold cyan]

One more zone — what to do when things get hard.
""",
    "solving_problems": """
[bold green]You found your way through![/bold green]

[bold cyan]"Conflict isn't the opposite of kindness,"[/bold cyan] Puck says.
[bold cyan]"How you handle conflict [italic]is[/italic] the kindness."[/bold cyan]

[bold cyan]"You know what to do now. Stay calm. Listen.
Look for what's fair. Ask for help if you need it.
Say sorry when you're wrong."[/bold cyan]

[bold white]These aren't small things. They're everything.[/bold white]
""",
}

BOSS_INTROS = {
    "feelings_garden": "A very complicated flower appears, wearing several feelings at once. [bold yellow]\"Sometimes people feel more than one thing. Can you figure out what this feeling is?\"[/bold yellow]",
    "kindness_actions": "A really tricky situation appears. [bold yellow]\"This one's harder than the others. What's the most genuinely kind thing to do here?\"[/bold yellow]",
    "being_a_good_friend": "Two friends are in a really hard situation together. [bold yellow]\"What does a truly good friend do in a moment like this?\"[/bold yellow]",
    "solving_problems": "A difficult problem appears with no easy answer. [bold yellow]\"This takes real wisdom. Think carefully — what would truly help here?\"[/bold yellow]",
}
