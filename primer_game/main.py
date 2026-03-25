"""
primer_game/main.py — Entry points for The Young Lady's Illustrated Primer.

Sets the skill-packs and campaigns directories for the engine, then launches
the appropriate pack or campaign.
"""

import os
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows (handles box-drawing chars, stars, etc.)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

_HERE = Path(__file__).parent.parent
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", str(_HERE / "primer_game" / "skill-packs"))
os.environ.setdefault("QUEST_CAMPAIGNS_DIR", str(_HERE / "primer_game" / "campaigns"))

from engine.main import run, run_campaign  # noqa: E402


def main_primer():
    run_campaign("young_ladys_primer")


def main_letters():
    run("letters")


def main_numbers():
    run("numbers")


def main_science():
    run("science")


def main_kindness():
    run("kindness")
