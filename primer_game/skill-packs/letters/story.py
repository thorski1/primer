"""
story.py — Narrative for the Letters skill pack.

Nell discovers the Primer and learns to read with the help of a
friendly companion named Puck, a small glowing creature who lives
inside the book and guides her through the world of letters and words.
"""

INTRO_STORY = """
[bold yellow]THE YOUNG LADY'S ILLUSTRATED PRIMER[/bold yellow]

Once upon a time, a little girl found a very special book.

The cover was the color of midnight blue, with tiny golden stars that
[italic]actually sparkled[/italic] when she tilted it toward the light.
When she opened the first page, a small glowing creature floated up
from between the words — no bigger than a firefly, but much friendlier.

[bold cyan]"Hello!"[/bold cyan] it said. [bold cyan]"My name is Puck. I've been waiting for you!"[/bold cyan]

The girl blinked. [bold white]"A talking book?"[/bold white]

[bold cyan]"Not just any book,"[/bold cyan] Puck said, spinning in a happy circle. [bold cyan]"THE book.
The one that will teach you everything — starting with the most
important skill of all. The one that unlocks all the others."[/bold cyan]

[bold white]"What's that?"[/bold white]

[bold cyan]"Reading, of course!"[/bold cyan]

Puck landed on the first page and pointed to a big golden letter.

[bold cyan]"Every story ever told, every adventure ever had,
every secret ever discovered — they're all waiting for you,
right here in these marks on the page. Once you know what
they say, [italic]no door will ever be closed to you.[/italic]"[/bold cyan]

The girl sat down, pulled the book onto her lap, and looked at
the letter Puck was pointing to.

[bold white]She was ready to begin.[/bold white]

[bold cyan]Are you ready too?[/bold cyan]
"""

ZONE_INTROS = {
    "letter_garden": """
Puck flew to a beautiful garden, where each flower had a letter
written on it in bright colors.

[bold cyan]"This is the Letter Garden,"[/bold cyan] Puck said. [bold cyan]"Every letter has its own
sound. Once you know all twenty-six of them, you can read
[italic]any word in the world![/italic]"[/bold cyan]

The flowers swayed gently. The letters waited.

[bold white]What sound does each letter make?[/bold white]
Let's find out together!
""",
    "vowel_pond": """
Puck led the way to a shimmering pond.

[bold cyan]"These are the Vowel Fish,"[/bold cyan] Puck said. [bold cyan]"They're special — only five
letters, but they appear in almost every single word. Their sounds
can change depending on what's around them!"[/bold cyan]

Five glowing fish leaped up from the water:
[bold yellow]A, E, I, O, U[/bold yellow]

[bold white]Short sounds and long sounds — can you tell them apart?[/bold white]
""",
    "blend_bridge": """
Puck pointed to a bridge made of letter blocks.

[bold cyan]"When two letters stand together, they often blend their sounds,"[/bold cyan]
Puck explained. [bold cyan]"Like friends holding hands — they each keep
their own sound, but they say it SO fast it sounds like one thing."[/bold cyan]

[italic]BR, ST, PL, TR...[/italic]

[bold white]Cross the bridge! Put the sounds together![/bold white]
""",
    "word_workshop": """
[bold cyan]"Now,"[/bold cyan] said Puck, [bold cyan]"we build!"[/bold cyan]

In a cozy workshop, letters floated in the air like pieces of a puzzle.
Put them in the right order, and they became words.
Put the words together, and they became [italic]meaning.[/italic]

[bold white]Take letters. Build words. Discover what they say.[/bold white]
""",
    "sentence_city": """
Puck spread wings wide as Nell looked out over a city made entirely
of words — buildings that were sentences, streets that were paragraphs.

[bold cyan]"A sentence is a complete thought,"[/bold cyan] Puck said. [bold cyan]"It has someone
doing something. Everything in this city is a thought someone wanted
to share. Can you read what they wrote?"[/bold cyan]

[bold white]Read the sentences. Understand the thoughts.[/bold white]
""",
}

ZONE_COMPLETIONS = {
    "letter_garden": """
[bold green]The Letter Garden glows![/bold green]

Every flower stands bright and tall. You know what each letter says.

[bold cyan]"You've done it!"[/bold cyan] Puck cheers. [bold cyan]"Twenty-six letters. Twenty-six sounds.
That's the whole alphabet — yours now, forever!"[/bold cyan]

The letters hum happily as you walk through the garden.
A new path has opened, leading toward the sparkling pond...
""",
    "vowel_pond": """
[bold green]The Vowel Fish leap with joy![/bold green]

The five vowels spin in joyful circles around you.

[bold cyan]"Now you know the special ones,"[/bold cyan] Puck says. [bold cyan]"A-E-I-O-U.
Short sounds. Long sounds. They're yours!"[/bold cyan]

The pond shimmers. The bridge ahead comes into view...
""",
    "blend_bridge": """
[bold green]The bridge is crossed![/bold green]

The letter blocks cheer as you reach the other side.

[bold cyan]"Look at that!"[/bold cyan] Puck says. [bold cyan]"You can hear the blend now, can't you?
BR and ST and TR — your ear is getting so sharp!"[/bold cyan]

The workshop is just ahead, and the letters are ready to be built into words...
""",
    "word_workshop": """
[bold green]The Workshop is buzzing![/bold green]

Words float around you like friendly butterflies — words you made!

[bold cyan]"You built real words,"[/bold cyan] Puck says proudly. [bold cyan]"CAT. TREE. JUMP. BLUE.
Each one means something. Each one is a little key that opens
a little door in the world of understanding."[/bold cyan]

The city glows on the horizon. Time to read what's written there!
""",
    "sentence_city": """
[bold green]The City is alive with your reading![/bold green]

Buildings light up as you read each sentence. The whole city buzzes.

[bold cyan]"You did it,"[/bold cyan] Puck says quietly. [bold cyan]"You read. Real sentences.
Real thoughts that real people wanted to share with you.
This is what it means to be a reader."[/bold cyan]

A door has opened — with a bigger adventure waiting on the other side.
""",
}

BOSS_INTROS = {
    "letter_garden": "Puck floats to the tallest flower. [bold yellow]\"The hardest letters are waiting at the center of the garden. You're ready for them!\"[/bold yellow]",
    "vowel_pond": "The biggest fish surfaces. [bold yellow]\"This one can make both a short sound AND a long sound. Can you tell which is which?\"[/bold yellow]",
    "blend_bridge": "A giant block with three letters stands in the middle of the bridge. [bold yellow]\"Three letters, all blending together! Listen carefully and you'll hear all three.\"[/bold yellow]",
    "word_workshop": "The letters rearrange into a long word. [bold yellow]\"This one has many pieces — but you know each piece already. Sound it out!\"[/bold yellow]",
    "sentence_city": "The tallest building in the city is covered in words. [bold yellow]\"One long sentence, all the way to the top. Read it — and the whole city celebrates!\"[/bold yellow]",
}
