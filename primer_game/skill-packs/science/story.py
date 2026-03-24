"""
story.py — Narrative for the Science skill pack.

Nell and Puck explore the natural world — living things, sky and weather,
the human body, and how things work.
"""

INTRO_STORY = """
[bold yellow]THE WORLD OF WONDERING[/bold yellow]

[bold cyan]"Close your eyes,"[/bold cyan] Puck said.

Nell closed them.

[bold cyan]"Now open them slowly. What do you see?"[/bold cyan]

Nell looked around. Sunlight. A tree. A bird on a branch.
A cloud drifting. Her own hands.

[bold white]"Everything,"[/bold white] she said.

[bold cyan]"Exactly,"[/bold cyan] Puck said, settling on her shoulder.
[bold cyan]"Everything around you is a puzzle. The sun, the rain,
why trees grow up instead of sideways, how your heart beats
without you thinking about it — all of it follows rules.
And once you know the rules, the world stops being confusing
and starts being [italic]wonderful.[/italic]"[/bold cyan]

The Primer glowed with a soft green light.

[bold cyan]"Scientists are just people who ask the question [italic]why[/italic]
about everything they see. You've been doing it your whole life —
you just didn't have the word for it."[/bold cyan]

Nell looked at the tree. At the bird. At the cloud.

She was going to figure out how all of it worked.

[bold white]Let's explore![/bold white]
"""

ZONE_INTROS = {
    "living_things": """
[bold cyan]"First question,"[/bold cyan] Puck said. [bold cyan]"What's alive?"[/bold cyan]

Nell looked around. The tree was alive. The bird was alive.
The rock on the ground... probably not?

[bold cyan]"Living things do certain things that rocks can't do,"[/bold cyan]
Puck said. [bold cyan]"They grow. They eat. They breathe.
They can have babies. Once you know the rules,
you can tell what's living and what's not — and that's
the beginning of understanding life itself."[/bold cyan]

[bold white]What makes something alive?[/bold white]
""",
    "sky_and_weather": """
Puck zoomed up high and pointed at the sky.

[bold cyan]"Everything up there is happening for a reason.
The sun isn't just bright — it's keeping you warm,
making plants grow, pulling water into clouds.
The rain isn't just wet — it's the same water cycling
round and round, forever."[/bold cyan]

[bold white]What's happening in the sky above us?[/bold white]
""",
    "body_basics": """
[bold cyan]"You've been living in that body your whole life,"[/bold cyan]
Puck said, [bold cyan]"but do you know what's happening inside it?"[/bold cyan]

Nell looked at her hand. Her heart was beating right now.
Her lungs were breathing. Her eyes were seeing.
All without her doing anything at all.

[bold cyan]"Your body is the most amazing machine ever built.
Let's learn how it works."[/bold cyan]

[bold white]How does your amazing body work?[/bold white]
""",
    "how_things_work": """
[bold cyan]"Cause and effect,"[/bold cyan] Puck said.
[bold cyan]"That's the secret of science. Every effect has a cause.
Every cause has an effect. Once you find the pattern,
you can [italic]predict[/italic] what happens next — and that's
[italic]power.[/italic]"[/bold cyan]

A wheel turned. A lever lifted. A shadow moved.

[bold white]What happens when you push, pull, or spin?[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "living_things": """
[bold green]The garden glows![/bold green]

Every living thing around you seems a little more remarkable now.
You know what makes them alive — growing, eating, breathing, changing.

[bold cyan]"Wherever you go,"[/bold cyan] Puck says, [bold cyan]"you'll see living things
differently now. Every plant is working. Every insect has a job.
Life is everywhere."[/bold cyan]

The sky is next. Look up!
""",
    "sky_and_weather": """
[bold green]The sky opens up![/bold green]

Clouds, rain, seasons, the sun — you understand the patterns now.

[bold cyan]"The weather isn't random,"[/bold cyan] Puck says. [bold cyan]"There are reasons.
And once you know why it rains, why it gets cold in winter,
why the sun rises in the east — you'll never look at a
cloudy day the same way."[/bold cyan]

Now let's look closer — at your own amazing body!
""",
    "body_basics": """
[bold green]Your body hums with understanding![/bold green]

[bold cyan]"Five senses. A heart that never stops. Lungs breathing
without being told. Bones making you strong."[/bold cyan]

Puck nods with deep satisfaction.

[bold cyan]"Taking care of your body means understanding it.
And now you do."[/bold cyan]

One more zone — how do things around us work?
""",
    "how_things_work": """
[bold green]The world of cause and effect is yours![/bold green]

[bold cyan]"You know why things happen now,"[/bold cyan] Puck says.
[bold cyan]"You know that ramps make heavy things easier to lift,
that shadows are made by blocking light,
that magnets pull on some things and not others."[/bold cyan]

A long pause.

[bold cyan]"The whole world works on rules like these.
And now you know the rules."[/bold cyan]
""",
}

BOSS_INTROS = {
    "living_things": "Puck points to the tallest tree in the garden. [bold yellow]\"The hardest living things question is waiting at the top. Are you ready?\"[/bold yellow]",
    "sky_and_weather": "A big storm cloud gathers overhead. [bold yellow]\"This is the toughest sky question. Think carefully — you know this!\"[/bold yellow]",
    "body_basics": "A giant diagram of the body appears. [bold yellow]\"Final body question — it's a tricky one. But you've learned so much!\"[/bold yellow]",
    "how_things_work": "A tall machine with gears and levers stands before you. [bold yellow]\"The hardest 'how things work' question. All your science knowledge comes together here!\"[/bold yellow]",
}
