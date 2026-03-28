# The Young Lady's Illustrated Primer

```
    *  .  .    *  . * .    *  .    *  .  .  *  .

____________ ________  ___ ___________
| ___ \ ___ \_   _|  \/  ||  ___| ___ \
| |_/ / |_/ / | | | .  . || |__ | |_/ /
|  __/|    /  | | | |\/| ||  __||    /
| |   | |\ \ _| |_| |  | || |___| |\ \
\_|   \_| \_|\___/\_|  |_/\____/\_| \_|

    *  .  .    *  . * .    *  .    *  .  .  *  .
```

> *"The book would be her guardian, her teacher, and her best friend.*
> *It would be everything she needed. Whenever she needed it."*
> — Neal Stephenson, *The Diamond Age*

---

The cover is midnight blue, with tiny gold stars that sparkle when you tilt it. When you open it, a small glowing creature floats up from between the pages.

**"Hello,"** it says. **"My name is Puck. And this book — *this* book — is for you."**

A terminal and web adventure for young learners. Sixteen chapters. One companion. A whole world to explore.

**16 chapters. 893 challenges. Ages 5-12. Guided by Puck.**

`v1.16.0` · Python 3.10+ · MIT License

---

## What's Inside

| # | Chapter | World | What You Learn | Ages |
|---|---------|-------|----------------|------|
| 1 | `letters-quest` | **The Letter Garden** | Phonics, vowels, blends, sight words, reading sentences | 5-7 |
| 2 | `numbers-quest` | **The Counting Kingdom** | Numbers, addition, subtraction, shapes, time, money | 6-8 |
| 3 | `science-quest` | **The World of Wondering** | Living things, weather, the body, simple machines, earth & space | 7-10 |
| 4 | `kindness-quest` | **The Art of Being Kind** | Feelings, friendship, listening, handling hard emotions | 6+ |
| 5 | `geography-quest` | **The Atlas of Wonders** | Continents, oceans, capitals, maps, landforms, world wonders | 7-10 |
| 6 | `math-advanced-quest` | **The Math Academy** | Multiplication, division, geometry, decimals, negative numbers | 8-11 |
| 7 | `history-quest` | **The Time Traveler's Primer** | Ancient civilizations, explorers, inventors, wars, world leaders | 8-11 |
| 8 | `art-quest` | **The Art Studio** | Colors, shapes, famous artwork, art elements, famous artists | 7-11 |
| 9 | `coding-basics-quest` | **The Code Garden** | What coding is, loops, conditionals, variables, functions | 8-12 |
| 10 | `space-quest` | **The Book of Stars** | Solar System, stars, the Moon, space exploration, seasons | 7-10 |
| 11 | `music-quest` | **The Music Room** | Notes, rhythm, instruments, singing, world music, composers | 7-10 |
| 12 | `animals-quest` | **The Animal Kingdom** | Animal groups, habitats, food chains, endangered species, ocean life | 7-10 |
| 13 | `words-quest` | **The Word Workshop** | Compound words, synonyms, prefixes, parts of speech, figurative language | 7-10 |
| 14 | `cooking-quest` | **The Kitchen Adventure** | Food groups, vitamins, labels, kitchen safety, world foods | 7-10 |
| 15 | `body-quest` | **The Body Explorer** | Bones, muscles, heart, lungs, brain, digestion, exercise | 7-10 |
| 16 | `money-quest` | **The Treasure Chest** | Story of money, earning, saving, spending, banks, entrepreneurship | 7-10 |

Every challenge is multiple-choice or fill-in-the-blank, designed for short focused sessions. Progress saves automatically.

---

## Install

### Recommended

```bash
uv tool install primer-quest
```

> Don't have `uv`? Install it in one line: `curl -LsSf https://astral.sh/uv/install.sh | sh`
>
> `uv tool install` creates an isolated environment — no venv setup, no system Python conflicts.

### Pip

```bash
pip install primer-quest
```

> On macOS with system Python, prefer `uv` — `pip install` may fail with an "externally managed environment" error.

### One-liner (no package manager)

```bash
curl -sSL https://raw.githubusercontent.com/thorski1/primer/main/install.sh | bash
```

---

## Play in the Terminal

```bash
primer                   # full 16-chapter story with Puck — start here
```

Each chapter is also playable standalone — see the command column in the table above. Examples:

```bash
letters-quest            # The Letter Garden
numbers-quest            # The Counting Kingdom
space-quest              # The Book of Stars
animals-quest            # The Animal Kingdom
```

---

## Play in the Browser

Launch a local web interface — colorful, playful theme designed for kids, runs at `localhost:8080`:

```bash
primer --web             # full hub with all 16 chapters
letters-quest --web      # single chapter
# any chapter command + --web
```

The web UI opens automatically in your browser. No separate server setup required.

### Features

- Warm, playful theme with rounded corners and Nunito font
- Sound effects on correct/wrong answers and level-ups
- Confetti celebrations on correct answers
- Keyboard shortcuts (A-D for answers, H for hint, S for skip)
- PWA — installable on tablets and phones
- Parent dashboard for monitoring progress

### Deploy on Vercel

Great for classroom use or sharing with family:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fthorski1%2Fprimer&project-name=primer-quest&repository-name=primer-quest)

After deploy, set `QUEST_PACK` in Vercel environment variables to choose a chapter (`letters`, `numbers`, `science`, `kindness`, `geography`, `math_advanced`, `history`, `art`, `coding_basics`, `space`, `music`, `animals`, `words`, `cooking`, `body`, `money`).

For persistent leaderboards and user accounts, add a `DATABASE_URL` environment variable pointing to a Postgres instance.

---

## Finding Your Starting Place

When you begin a new campaign, **Puck will ask you a few short questions** to find the best place to start. There are no wrong answers — just a gentle way to begin where things are interesting, not too easy and not too hard.

You can also:
- Start at the beginning (Chapter 1: The Letter Garden)
- Jump to any chapter directly from the Chapter Map
- Play individual chapters as standalone adventures

---

## Gameplay

Puck introduces each topic through a short story, then presents challenges:

- **Multiple Choice** — read the question, type A / B / C / D
- **Fill in the Blank** — type the missing word or number

Controls:

```
Puck: [h] Hint   [l] Lesson   [b] Bookmark   [s] Skip   [q] Menu
```

Puck offers hints when you're stuck. Every wrong answer is just a step toward the right one.

### Features

| Feature | Description |
|---------|-------------|
| **Daily Challenge** | One special challenge each day with bonus XP |
| **Bookmarks** | Save any challenge to revisit later |
| **Zone Preview** | See what's coming before entering a zone |
| **Speed Records** | Personal bests tracked per challenge |
| **Star Ratings** | Zones rated 1-3 stars based on how you did |
| **Completion Certificate** | Printed on campaign completion |
| **Level Titles** | Seedling > Sprout > Bloom > Star > Wonder > Sage |
| **Adaptive Difficulty** | Engine adjusts based on performance |
| **Web Mode** | Colorful browser UI — playful theme, sound effects, PWA |
| **Leaderboards** | Rankings when Postgres is configured |
| **User Accounts** | Signup/login for cross-device progress with Postgres |
| **Auto-Updates** | Puck checks for new lessons at startup |

Progress saves automatically to `~/.quest_engine/`. Resume any time.

---

## For Parents & Educators

- Each zone takes **5-15 minutes** — designed for short, focused sessions
- Progress saves automatically between sessions
- Works independently or as a **shared reading experience** — especially for younger children
- A placement quiz at the start finds the right chapter for each child
- All content is age-appropriate and celebrates curiosity, kindness, and growth
- The web mode works on any device with a browser — tablets, Chromebooks, desktops
- Deploy on Vercel for a classroom-wide instance with leaderboards
- Parent dashboard available in web mode for tracking progress

---

## Requirements

- Python 3.10+ (for local install)
- A terminal (Terminal.app, iTerm2, Windows Terminal) for terminal mode
- Any modern browser for web mode
- 80+ column width recommended for the terminal UI

---

## Built On

[Quest Engine](https://github.com/thorski1/quest-engine) — an open-source pluggable terminal + web RPG framework.

Inspired by the Primer from Neal Stephenson's *The Diamond Age*.

---

## License

MIT
