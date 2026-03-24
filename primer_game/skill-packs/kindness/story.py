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
    "listening_skills": """
[bold cyan]"Most people think they're good listeners,"[/bold cyan] Puck said.
[bold cyan]"But real listening is rarer than you think.
And it might be the greatest gift you can give another person."[/bold cyan]

In the Listening Garden, every flower leaned toward
the ones that truly paid attention.

[bold cyan]"When you really listen — not just waiting to talk,
but actually [italic]hearing[/italic] — people feel seen.
And feeling seen is one of the best feelings there is."[/bold cyan]

[bold white]What does real listening look like?[/bold white]
""",
    "helping_community": """
A busy square appeared — neighbors talking, kids helping,
someone picking up something a stranger dropped.

[bold cyan]"You don't live by yourself on an island,"[/bold cyan] Puck said warmly.
[bold cyan]"You live in communities — your family, your class,
your neighborhood. And communities only work
when people look out for each other."[/bold cyan]

[bold cyan]"Even small things add up. Even you — right now — can help."[/bold cyan]

[bold white]How do we take care of each other?[/bold white]
""",
    "handling_hard_feelings": """
[bold cyan]"Big feelings,"[/bold cyan] Puck said gently, [bold cyan]"are not your enemy.
They're your body and heart trying to tell you something."[/bold cyan]

Nell thought about times she'd felt so angry she couldn't speak,
or so sad she didn't want to move.

[bold cyan]"The trick isn't to make the feelings go away.
The trick is to understand them — and to be kind to yourself
while you're feeling them."[/bold cyan]

[bold white]What do you do when feelings get really big?[/bold white]
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
    "listening_skills": """
[bold green]The Listening Garden is in full bloom![/bold green]

[bold cyan]"You know the secret now,"[/bold cyan] Puck says.
[bold cyan]"Eye contact. Waiting. Asking. Reflecting back.
Checking in on someone who seems quiet."[/bold cyan]

[bold cyan]"Most people never learn all of that.
You have. And the people in your life
are going to feel it — even if they can't say why."[/bold cyan]
""",
    "helping_community": """
[bold green]The Community Square is alive with warmth![/bold green]

[bold cyan]"Every community gets better,"[/bold cyan] Puck says,
[bold cyan]"when each person in it decides to help.
You just decided."[/bold cyan]

[bold cyan]"A thank-you. A turn taken fairly. A smile.
An act of kindness that costs nothing.
Those things ripple out further than you know."[/bold cyan]
""",
    "handling_hard_feelings": """
[bold green]The Feelings Workshop glows with gentle light.[/bold green]

[bold cyan]"Pause and breathe. Notice your body.
Let yourself cry if you need to.
Ask for help. Be kind to yourself."[/bold cyan]

Puck rests quietly beside Nell for a moment.

[bold cyan]"Big feelings aren't problems to be solved.
They're part of being alive and caring about things.
And now you know how to move through them —
with grace, and with kindness toward yourself."[/bold cyan]
""",
}

BOSS_INTROS = {
    "feelings_garden": "A very complicated flower appears, wearing several feelings at once. [bold yellow]\"Sometimes people feel more than one thing. Can you figure out what this feeling is?\"[/bold yellow]",
    "kindness_actions": "A really tricky situation appears. [bold yellow]\"This one's harder than the others. What's the most genuinely kind thing to do here?\"[/bold yellow]",
    "being_a_good_friend": "Two friends are in a really hard situation together. [bold yellow]\"What does a truly good friend do in a moment like this?\"[/bold yellow]",
    "solving_problems": "A difficult problem appears with no easy answer. [bold yellow]\"This takes real wisdom. Think carefully — what would truly help here?\"[/bold yellow]",
    "listening_skills": "A friend is quieter than usual and hasn't said anything is wrong. [bold yellow]\"This is the hardest listening challenge. No one told you there was a problem. What do you do?\"[/bold yellow]",
    "helping_community": "A single warm smile is all you have to give. [bold yellow]\"Can something that costs nothing really change someone's day? Think about what kindness truly is.\"[/bold yellow]",
    "handling_hard_feelings": "Two people are hurting each other. One of them is having a terrible day. [bold yellow]\"Does feeling bad make it okay to act mean? This is the hardest feelings question of all.\"[/bold yellow]",
}
