# The Young Lady's Illustrated Primer

```
 _____ _         ___      _
|_   _| |_  ___ | _ \_ _(_)_ __  ___ _ _
  | | | ' \/ -_)|  _/ '_| | '  \/ -_) '_|
  |_| |_||_\___||_| |_| |_|_|_|_\___|_|
```

> *"The book would be her guardian, her teacher, and her best friend. It would be everything she needed. Whenever she needed it."*
> — Neal Stephenson, *The Diamond Age*

A terminal learning game for girls, inspired by Neal Stephenson's *Young Lady's Illustrated Primer*. A companion named **Puck** guides players through four essential life skills, delivered as an interactive story.

---

## What's Inside

| Chapter | Topic | What You Learn |
|---------|-------|----------------|
| 1 | **Letters** | Phonics, vowels, blends, reading sentences |
| 2 | **Numbers** | Counting, addition, subtraction, shapes, time |
| 3 | **Science** | Living things, weather, the body, how things work |
| 4 | **Kindness** | Feelings, kind actions, friendship, solving problems |

**105 challenges** across 18 zones. Every challenge is multiple-choice or fill-in-the-blank, designed to be completed in short sessions. Progress saves automatically.

---

## Who Is This For?

The Primer is designed to grow with you. Each chapter builds on the last, but all four can be played independently. Roughly:

- **Letters**: Ages 5–7 (learning to read)
- **Numbers**: Ages 6–8 (early math)
- **Science**: Ages 7–10 (natural curiosity about the world)
- **Kindness**: Ages 6+ (emotional skills have no age ceiling)

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
| `letters-quest` | Letters chapter standalone |
| `numbers-quest` | Numbers chapter standalone |
| `science-quest` | Science chapter standalone |
| `kindness-quest` | Kindness chapter standalone |

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

- Sessions are short: each zone takes 5–15 minutes
- Progress saves automatically between sessions
- The game can be played independently or alongside a parent
- All content is age-appropriate and encourages curiosity, kindness, and growth

---

## Requirements

- Python 3.10+
- A terminal (Terminal.app, iTerm2, Windows Terminal)
- 80+ column width recommended

For very young children (ages 4–6), a parent sitting alongside is recommended for the reading portions.

---

## Built On

[Quest Engine](https://github.com/thorski1/quest-engine) — a pluggable terminal RPG framework.
