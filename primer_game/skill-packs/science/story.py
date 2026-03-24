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
    "simple_machines": """
[bold cyan]"Long before electricity,"[/bold cyan] Puck said, eyes wide,
[bold cyan]"before engines or computers — people built
the pyramids, the great cathedrals, whole cities.
With their hands. And six tools."[/bold cyan]

Six. That's all.

[bold cyan]"The lever. The wheel and axle. The inclined plane.
The pulley. The wedge. The screw.
These are the six ancient tools that built every civilization
that ever existed. And once you understand them,
you'll see them [italic]everywhere.[/italic]"[/bold cyan]

[bold white]What's the secret of each simple machine?[/bold white]
""",
    "earth_and_space": """
Puck pointed straight up.

[bold cyan]"We live on a giant ball,"[/bold cyan] Puck said, [bold cyan]"spinning through
space, flying around a star, while a moon circles around us,
and billions of other suns burn silently in every direction."[/bold cyan]

Nell looked up at the blue sky.

[bold cyan]"On a clear night you can see some of those other suns.
They look like tiny dots. They're not tiny.
They're enormous — just very, very far away."[/bold cyan]

[bold white]What do you know about our place in the sky?[/bold white]
""",
    "matter_and_energy": """
[bold cyan]"Everything around you,"[/bold cyan] Puck said, gesturing at the walls,
the floor, the air, [bold cyan]"is made of matter.
And all matter exists in one of three states:
solid, liquid, or gas."[/bold cyan]

[bold cyan]"Your pencil. The water in your glass.
The air filling your lungs right now.
All matter — just in different forms.
And here's the amazing part:"[/bold cyan] Puck paused for effect.

[bold cyan]"They can change from one to another."[/bold cyan]

[bold white]Let's find out what's solid, what's liquid, and what's gas![/bold white]
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
    "simple_machines": """
[bold green]The workshop rings with the sound of discovery![/bold green]

[bold cyan]"Six tools,"[/bold cyan] Puck says with great satisfaction.
[bold cyan]"Lever, wheel and axle, inclined plane,
pulley, wedge, and screw.
You now understand every simple machine
that built human civilization."[/bold cyan]

[bold cyan]"Next time you see a ramp, a jar lid, a bicycle —
you'll know exactly what's happening.
And that knowledge is yours forever."[/bold cyan]
""",
    "earth_and_space": """
[bold green]The sky observatory lights up![/bold green]

[bold cyan]"Earth goes around the Sun. The Moon goes around Earth.
Day and night from spinning. A year from orbiting.
The Moon's phases from where we stand."[/bold cyan]

Puck looks at the stars beginning to appear.

[bold cyan]"And every single one of those stars is a sun.
Burning. Enormous. Some of them might have their
own Earths going around them."[/bold cyan]

A pause full of wonder.

[bold cyan]"Isn't that the most AMAZING thing?"[/bold cyan]
""",
    "matter_and_energy": """
[bold green]The matter lab glows with understanding![/bold green]

[bold cyan]"Solid, liquid, gas,"[/bold cyan] Puck says.
[bold cyan]"And they transform. Melt. Freeze. Evaporate.
The water in your glass might have been a glacier once.
Or a cloud. Or part of the ocean."[/bold cyan]

[bold cyan]"Matter doesn't disappear — it just changes.
And now you understand how."[/bold cyan]

[bold white]That's the science of the world all around you![/bold white]
""",
}

BOSS_INTROS = {
    "living_things": "Puck points to the tallest tree in the garden. [bold yellow]\"The hardest living things question is waiting at the top. Are you ready?\"[/bold yellow]",
    "sky_and_weather": "A big storm cloud gathers overhead. [bold yellow]\"This is the toughest sky question. Think carefully — you know this!\"[/bold yellow]",
    "body_basics": "A giant diagram of the body appears. [bold yellow]\"Final body question — it's a tricky one. But you've learned so much!\"[/bold yellow]",
    "how_things_work": "A tall machine with gears and levers stands before you. [bold yellow]\"The hardest 'how things work' question. All your science knowledge comes together here!\"[/bold yellow]",
}
