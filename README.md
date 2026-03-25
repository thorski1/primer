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

> **Tags:** educational game for kids, learning game, children's educational app, learn to read, math for kids, coding for kids, history for kids, terminal game for children, Neal Stephenson Diamond Age

---

## What's Inside

| Chapter | World | What You Learn | Ages |
|---------|-------|----------------|------|
| 1 | **The Letter Garden** | Phonics, vowels, blends, sight words, reading sentences | 5-7 |
| 2 | **The Counting Kingdom** | Numbers, addition, subtraction, shapes, time, money | 6-8 |
| 3 | **The World of Wondering** | Living things, weather, the body, simple machines, earth & space | 7-10 |
| 4 | **The Art of Being Kind** | Feelings, friendship, listening, handling hard emotions | 6+ |
| 5 | **The Atlas of Wonders** | Continents, oceans, capitals, maps, landforms, world wonders | 7-10 |
| 6 | **The Math Academy** | Multiplication, division, geometry, decimals, negative numbers | 8-11 |
| 7 | **The Time Traveler's Primer** | Ancient civilizations, explorers, inventors, wars, world leaders | 8-11 |
| 8 | **The Art Studio** | Colors, shapes, famous artwork, art elements, famous artists | 7-11 |
| 9 | **The Code Garden** | What coding is, loops, conditionals, variables, functions | 8-12 |

**500+ challenges** across 75+ zones. Every challenge is multiple-choice or fill-in-the-blank, designed for short focused sessions. Progress saves automatically.

---

## Finding Your Starting Place

When you begin a new campaign, **Puck will ask you a few short questions** to find the best place to start. There are no wrong answers — just a gentle way to begin where things are interesting, not too easy and not too hard.

You can also:
- Start at the beginning (Chapter 1: The Letter Garden)
- Jump to any chapter directly from the Chapter Map
- Play individual chapters as standalone adventures

---

## Install

### Mac / Linux

```bash
curl -sSL https://raw.githubusercontent.com/thorski1/primer/main/install.sh | bash
```

Then run:
```bash
primer
```

### Windows

**Requirements:** [Python 3.10+](https://python.org/downloads) (check "Add Python to PATH" during install) and [git](https://git-scm.com/download/win)

Open **PowerShell** and run:
```powershell
powershell -ExecutionPolicy Bypass -c "irm https://raw.githubusercontent.com/thorski1/primer/main/install.ps1 | iex"
```

Then **open a new terminal window** and run:
```
primer
```

> **Best experience:** Use [Windows Terminal](https://aka.ms/terminal) (free, Microsoft Store). The default `cmd.exe` may display characters incorrectly.

> **If you see "running scripts is disabled":** The one-liner above bypasses this automatically. If it still fails, run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` first.

> **If `primer` is not found after install:** Open a new terminal window and try again. If still not found, run `python -m primer_game.main` as a fallback.

### Manual Install (Mac / Linux / Windows)

Requires Python 3.10+ and git.

**Mac / Linux:**
```bash
git clone https://github.com/thorski1/quest-engine ~/.local/share/quest-engine
git clone https://github.com/thorski1/primer ~/.local/share/primer

python3 -m pip install -e ~/.local/share/quest-engine
python3 -m pip install -e ~/.local/share/primer
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/thorski1/quest-engine "$env:LOCALAPPDATA\QuestEngine\quest-engine"
git clone https://github.com/thorski1/primer "$env:LOCALAPPDATA\QuestEngine\primer"

python -m pip install -e "$env:LOCALAPPDATA\QuestEngine\quest-engine"
python -m pip install -e "$env:LOCALAPPDATA\QuestEngine\primer"
```

---

## Running

| Command | Description |
|---------|-------------|
| `primer` | Full 7-chapter story with Puck — start here |
| `letters-quest` | The Letter Garden — standalone |
| `numbers-quest` | The Counting Kingdom — standalone |
| `science-quest` | The World of Wondering — standalone |
| `kindness-quest` | The Art of Being Kind — standalone |
| `geography-quest` | The Atlas of Wonders — standalone |
| `math-advanced-quest` | The Math Academy — standalone |
| `coding-basics-quest` | The Code Garden — standalone |

---

## Gameplay

Puck introduces each topic through a short story, then presents challenges:

- **Multiple Choice** — read the question, type A / B / C / D
- **Fill in the Blank** — type the missing word or number

```
  Puck: [h] Hint  [b] Bookmark  [?] Help  [s] Skip  [q] Menu
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
| **Level Titles** | Seedling -> Sprout -> Bloom -> Star -> Wonder -> Sage |

---

## For Parents

- Each zone takes **5-15 minutes** — designed for short, focused sessions
- Progress saves automatically between sessions
- The game works independently or as a **shared reading experience** — especially for younger children
- A placement quiz at the start finds the right chapter for each child
- All content is age-appropriate and celebrates curiosity, kindness, and growth
- The Primer is designed for girls but welcomes every curious reader

---

## Requirements

- Python 3.10+
- A terminal (Terminal.app, iTerm2, Windows Terminal)
- 80+ column width recommended

---

## Built On

[Quest Engine](https://github.com/thorski1/quest-engine) — a pluggable terminal RPG framework.

Inspired by the Primer from Neal Stephenson's *The Diamond Age*.
