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

A terminal adventure for girls. Four chapters. One companion. A world of things to know.

---

## What's Inside

| Chapter | World | What You Learn |
|---------|-------|----------------|
| 1 | **The Letter Garden** | Phonics, vowels, blends, sight words, reading sentences |
| 2 | **The Counting Kingdom** | Counting, addition, subtraction, skip counting, shapes, time, money |
| 3 | **The World of Wondering** | Living things, weather, the body, simple machines, earth & space |
| 4 | **The Art of Being Kind** | Feelings, kind actions, friendship, listening, handling emotions |

**140+ challenges** across 22 zones. Every challenge is multiple-choice or fill-in-the-blank, designed for short sessions. Progress saves automatically.

---

## Who Is This For?

The Primer grows with you. Each chapter builds on the last, but all four can be played independently:

| Chapter | Ages | Description |
|---------|------|-------------|
| Letters | 5–7 | Learning to read — letters, sounds, words, sentences |
| Numbers | 6–8 | Early math — counting, addition, subtraction, shapes |
| Science | 7–10 | Natural curiosity about how the world works |
| Kindness | 6+ | Emotional skills have no age ceiling |

**For very young children** (ages 4–6), a parent or helper sitting alongside is recommended for reading portions. The Primer is designed to be a shared experience.

---

## Finding Your Starting Place

When you begin a new campaign, **Puck will ask you a few questions** to find the best place to start. There are no wrong answers — it's just a way to begin where things are interesting, not too easy and not too hard.

If you prefer, you can:
- Start at the beginning (Chapter 1: The Letter Garden)
- Jump to any chapter from the Chapter Map
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

Open **PowerShell** and run:
```powershell
irm https://raw.githubusercontent.com/thorski1/primer/main/install.ps1 | iex
```

Then run:
```
primer
```

### Manual Install

Requires Python 3.10+ and git.

```bash
git clone https://github.com/thorski1/quest-engine ~/.local/share/quest-engine
git clone https://github.com/thorski1/primer ~/.local/share/primer

pip install -e ~/.local/share/quest-engine
pip install -e ~/.local/share/primer
```

---

## Running

| Command | Description |
|---------|-------------|
| `primer` | Full 4-chapter story with Puck |
| `letters-quest` | The Letter Garden — standalone |
| `numbers-quest` | The Counting Kingdom — standalone |
| `science-quest` | The World of Wondering — standalone |
| `kindness-quest` | The Art of Being Kind — standalone |

---

## Gameplay

Puck introduces each topic through a short story, then presents challenges:

- **Multiple Choice** — read the question, type A / B / C / D
- **Fill in the Blank** — type the missing word or number

```
  [h] Hint  (-10 XP)   [s] Skip   [q] Menu
```

Puck offers hints when you're stuck. No wrong answer is final — keep trying until it clicks.

---

## For Parents

- Each zone takes 5–15 minutes — designed for short, focused sessions
- Progress saves automatically between sessions
- The game can be played independently or with a parent reading alongside
- The Primer starts with a short placement quiz to find the right starting point
- All content is age-appropriate and encourages curiosity, kindness, and growth

---

## Requirements

- Python 3.10+
- A terminal (Terminal.app, iTerm2, Windows Terminal)
- 80+ column width recommended

---

## Built On

[Quest Engine](https://github.com/thorski1/quest-engine) — a pluggable terminal RPG framework.
