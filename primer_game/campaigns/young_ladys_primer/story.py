"""
story.py — Campaign narrative for The Young Lady's Illustrated Primer.
"""

# ── Entry Summaries ───────────────────────────────────────────────────────────
# Shown when a player jumps into a chapter without completing prior ones.
# Puck narrates what "happened before" so the story still makes sense.

CHAPTER_ENTRY_SUMMARIES = {
    "numbers": """
[bold cyan]Puck flutters open the Primer to a golden page.[/bold cyan]

[white]In the Letter Garden, young readers learned the twenty-six letters —
every vowel, every consonant, every blend that makes our words.
They crossed the Blend Bridge, built words in the Workshop,
and read full sentences in Sentence City.[/white]

[bold cyan]"You're starting here — in the Counting Kingdom,"[/bold cyan] Puck says.
[bold cyan]"Words and numbers are the twin languages of the world.
You're learning the second one now."[/bold cyan]
""",
    "geography": """
[bold cyan]Puck opens the Primer to a page showing the whole round Earth.[/bold cyan]

[white]Before this chapter: words were learned, numbers were mastered,
the natural world was explored, and kindness was practiced.
The Primer now opens its atlas pages — the world map glows with possibility.[/white]

[bold cyan]"Seven continents. Five oceans. Hundreds of countries," Puck says.
"The world is waiting to be known."[/bold cyan]
""",
    "math_advanced": """
[bold cyan]Puck opens the Primer to a page covered in numbers and shapes.[/bold cyan]

[white]A young learner has come far: letters and reading mastered,
numbers and basic arithmetic understood, the world explored,
kindness practiced, and now — the globe mapped.

The Primer turns to harder mathematics.[/white]

[bold cyan]"You already know addition and subtraction," Puck says.
"Now we go further: multiplication, division, fractions, geometry.
The full toolkit of mathematical thinking."[/bold cyan]
""",
    "coding_basics": """
[bold cyan]Puck stands at the entrance to the Code Garden.[/bold cyan]

[white]Words, numbers, science, kindness, geography, and mathematics —
all of it learned. The Primer now opens its final chapter:
how computers think, and how to give them instructions.[/white]

[bold cyan]"This isn't about memorizing commands," Puck says.
"It's about learning to think in steps.
To break a problem into pieces. To teach a machine what you want."[/bold cyan]
""",
    "science": """
[bold cyan]Puck opens the Primer to a page full of color and light.[/bold cyan]

[white]Before this chapter: a reader learned every letter and discovered
how words are built. Then she traveled through the Counting Kingdom —
numbers, addition, subtraction, shapes, and how to read a clock.

Now the Primer turns to the world outside.[/white]

[bold cyan]"Science,"[/bold cyan] Puck says, [bold cyan]"is what happens when
someone can't stop asking why. Let's find out why."[/bold cyan]
""",
    "kindness": """
[bold cyan]Puck turns to the warmest pages in the Primer.[/bold cyan]

[white]Three chapters behind you — or waiting to be explored when you're ready.
Letters and reading. Numbers and counting. Science and wondering.
Three ways of understanding the world.[/white]

[bold cyan]"But there's one more thing,"[/bold cyan] Puck says quietly.
[bold cyan]"Knowing things makes you powerful.
Kindness makes you someone worth knowing.
Let's learn both."[/bold cyan]
""",
}

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
    "geography": """
The Primer opened to a new page — and there was the whole world.

Oceans and mountains. City lights at night. Desert sands and Arctic ice.
The great rivers. The tallest peaks. The smallest island nations.

[bold cyan]"The world is very large,"[/bold cyan] Puck said. [bold cyan]"But knowing [italic]where[/italic]
things are — that's the beginning of understanding [italic]why[/italic] the world
is the way it is."[/bold cyan]

[bold white]The Atlas of Wonders is open. Let's explore![/bold white]
""",
    "math_advanced": """
[bold cyan]"You know how to count,"[/bold cyan] Puck said, [bold cyan]"and how to add and subtract.
Now we go further."[/bold cyan]

The Primer opened to the Math Academy — a grand building full of
number puzzles, geometry shapes floating in the air, and clocks
showing fractions of time.

[bold cyan]"Multiplication. Division. Fractions. Decimals. Geometry.
These aren't harder — they're deeper. They answer bigger questions."[/bold cyan]

[bold white]The Math Academy is ready. This is where thinking gets powerful![/bold white]
""",
    "coding_basics": """
The Primer's final chapter glowed with a special light —
softer, more focused, like the glow of a screen in a quiet room.

[bold cyan]"This,"[/bold cyan] Puck said, [bold cyan]"is the chapter about [italic]instructions.[/italic]
How computers work. How programs are written. Not the buttons and apps —
the ideas underneath."[/bold cyan]

Puck turned to look at you directly.

[bold cyan]"Loops. Choices. Variables. Functions.
These are the shapes that all programs are made of.
Learn them here, and you'll understand [italic]every[/italic] program you ever meet."[/bold cyan]

[bold white]The Code Garden is ready. Let's grow some ideas![/bold white]
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

[bold white]But the world is big — and the Primer has more pages.[/bold white]
""",
    "geography": """
The atlas closes softly.

Every continent, every ocean — named and known.
Capital cities memorized. Maps read with confidence.
Mountains, rivers, and deserts placed in their proper homes.
The wonders of the world, understood and celebrated.

[bold cyan]"Do you feel it?"[/bold cyan] Puck says.

[bold cyan]"That feeling that the world is [italic]smaller[/italic] now — not because it got smaller,
but because [italic]you[/italic] got bigger. You know where things are.
You know the shape of the Earth. That's not nothing — that's geography."[/bold cyan]

[bold white]Next: the Math Academy awaits. Numbers, patterns, and problem-solving.[/bold white]
""",
    "math_advanced": """
The Academy gates close behind you, golden light trailing in the air.

Multiplication mastered. Division understood. Word problems solved
step by step, with patience and logic. Geometry drawn and measured.
Decimals and fractions — the in-between numbers — finally making sense.
Even negative numbers, the ones that live below zero.

[bold cyan]"You are a mathematician,"[/bold cyan] Puck says simply.
[bold cyan]"Not because you're perfect — because you know how to think through problems.
That skill works in every subject, every job, every challenge.
Mathematics is just the clearest form of [italic]careful thinking.[/italic]"[/bold cyan]

[bold white]The Code Garden is next — and it grows from this very skill.[/bold white]
""",
    "coding_basics": """
The Code Garden is fully awake.

Every machine in it has instructions. Every loop is doing useful work.
Every function is named and ready to be called. The program at the heart
of the garden runs cleanly, without error, from start to finish.

[bold cyan]"You understand how computers think,"[/bold cyan] Puck says softly.
[bold cyan]"You know what a program is. You know how to break a problem into steps.
You know what a loop does. What a function does. What a variable remembers."[/bold cyan]

Puck glows warm gold.

[bold cyan]"Those are not just coding ideas. Those are [italic]thinking[/italic] ideas.
You will use them for the rest of your life."[/bold cyan]
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

# ── Placement Quiz ─────────────────────────────────────────────────────────────
# 6 questions, 2 per chapter (indices 0-2 = letters, numbers, science).
# "chapter" field tells the engine which chapter these questions test readiness for.
# Getting both questions for a chapter correct means the player can skip that chapter.
# Parent tip: for pre-readers, ask a grown-up to read these questions aloud!

PLACEMENT_QUESTIONS = [
    # Letters (chapter 0) — basic phonics and alphabet
    {
        "question": "Which of these is a vowel? (Ask a helper to read this if you need!)",
        "options": ["B", "E", "K", "T"],
        "answer": "b",
        "chapter": 0,
    },
    {
        "question": "Which word rhymes with 'cat'?",
        "options": ["dog", "hat", "run", "big"],
        "answer": "b",
        "chapter": 0,
    },
    # Numbers (chapter 1) — basic addition and subtraction
    {
        "question": "What is 3 + 4?",
        "options": ["6", "7", "8", "5"],
        "answer": "b",
        "chapter": 1,
    },
    {
        "question": "You have 9 apples and give away 3. How many are left?",
        "options": ["12", "5", "6", "8"],
        "answer": "c",
        "chapter": 1,
    },
    # Science (chapter 2) — basic world knowledge
    {
        "question": "Which of these is a living thing?",
        "options": ["Cloud", "Rock", "Flower", "Puddle"],
        "answer": "c",
        "chapter": 2,
    },
    {
        "question": "What warms the Earth and helps plants grow?",
        "options": ["Wind", "The Sun", "Rain", "Soil"],
        "answer": "b",
        "chapter": 2,
    },
]
