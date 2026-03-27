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

The cover is midnight blue, with tiny gold stars that sparkle when you tilt it.
When you open it, a small glowing creature floats up from between the pages.

**"Hello,"** it says. **"My name is Puck. And this book — *this* book — is for you."**

A terminal adventure for young learners. Nine chapters. One companion. A whole world to explore.

---

## What's Inside

| Chapter | World | What You Learn | Ages |
|---------|-------|----------------|------|
| 1 | **The Letter Garden** | Phonics, vowels, blends, sight words, reading sentences | 5–7 |
| 2 | **The Counting Kingdom** | Numbers, addition, subtraction, shapes, time, money | 6–8 |
| 3 | **The World of Wondering** | Living things, weather, the body, simple machines, earth & space | 7–10 |
| 4 | **The Art of Being Kind** | Feelings, friendship, listening, handling hard emotions | 6+ |
| 5 | **The Atlas of Wonders** | Continents, oceans, capitals, maps, landforms, world wonders | 7–10 |
| 6 | **The Math Academy** | Multiplication, division, geometry, decimals, negative numbers | 8–11 |
| 7 | **The Time Traveler's Primer** | Ancient civilizations, explorers, inventors, wars, world leaders | 8–11 |
| 8 | **The Art Studio** | Colors, shapes, famous artwork, art elements, famous artists | 7–11 |
| 9 | **The Code Garden** | What coding is, loops, conditionals, variables, functions | 8–12 |

**670+ challenges** across 93+ zones. Every challenge is multiple-choice or fill-in-the-blank, designed for short focused sessions. Progress saves automatically.

---

## Install

### Recommended

```bash
uv tool install primer-quest
```

> Don't have `uv`? Install it in one line: `curl -LsSf https://astral.sh/uv/install.sh | sh`
>
> `uv tool install` creates an isolated environment — no venv setup, no system Python conflicts.

### Pip fallback

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
primer                   # full 9-chapter story with Puck — start here
```

Each chapter is also playable standalone:

| Command | Chapter |
|---------|---------|
| `letters-quest` | The Letter Garden |
| `numbers-quest` | The Counting Kingdom |
| `science-quest` | The World of Wondering |
| `kindness-quest` | The Art of Being Kind |
| `geography-quest` | The Atlas of Wonders |
| `math-advanced-quest` | The Math Academy |
| `history-quest` | The Time Traveler's Primer |
| `art-quest` | The Art Studio |
| `coding-basics-quest` | The Code Garden |

---

## Play in the Browser

Launch a local web interface for any chapter — colorful, playful theme designed for kids, runs at `localhost:8080`:

```bash
primer --web
letters-quest --web
numbers-quest --web
# any chapter command + --web
```

The web UI opens automatically in your browser. No separate server setup required.

### Host on Vercel

Deploy your own instance — great for classroom use or sharing with family:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fthorski1%2Fprimer&project-name=primer-quest&repository-name=primer-quest)

After deploy, the Math Academy chapter is live. Set `QUEST_PACK` in Vercel environment variables to run a different chapter (`letters`, `numbers`, `science`, `kindness`, `geography`, `math_advanced`, `history`, `art`, `coding_basics`).

> Game progress is per browser session on hosted instances. For persistent save files, run locally.

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
| **Star Ratings** | Zones rated 1–3 stars based on how you did |
| **Completion Certificate** | Printed on campaign completion |
| **Level Titles** | Seedling → Sprout → Bloom → Star → Wonder → Sage |
| **Web Mode** | Colorful browser UI — playful theme, same content and XP |
| **Auto-Updates** | Puck checks for new lessons at startup |

Progress saves automatically to `~/.quest_engine/`. Resume any time.

---

## For Parents & Educators

- Each zone takes **5–15 minutes** — designed for short, focused sessions
- Progress saves automatically between sessions
- Works independently or as a **shared reading experience** — especially for younger children
- A placement quiz at the start finds the right chapter for each child
- All content is age-appropriate and celebrates curiosity, kindness, and growth
- The web mode works on any device with a browser — tablets, Chromebooks, desktops

---

## Requirements

- Python 3.10+ (for local install)
- A terminal (Terminal.app, iTerm2, Windows Terminal) for terminal mode
- Any modern browser for web mode
- 80+ column width recommended for the terminal UI

---

## Built On

[Quest Engine](https://github.com/thorski1/quest-engine) — an open-source pluggable terminal RPG framework.

Inspired by the Primer from Neal Stephenson's *The Diamond Age*.
