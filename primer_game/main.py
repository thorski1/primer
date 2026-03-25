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

from engine.main import run, run_campaign          # noqa: E402
from engine.updater import check_and_prompt        # noqa: E402

_PACKAGE = "primer"


def main_primer():
    check_and_prompt(_PACKAGE)
    run_campaign("young_ladys_primer")


def main_letters():
    check_and_prompt(_PACKAGE)
    run("letters")


def main_numbers():
    check_and_prompt(_PACKAGE)
    run("numbers")


def main_science():
    check_and_prompt(_PACKAGE)
    run("science")


def main_kindness():
    check_and_prompt(_PACKAGE)
    run("kindness")


def main_geography():
    check_and_prompt(_PACKAGE)
    run("geography")


def main_math_advanced():
    check_and_prompt(_PACKAGE)
    run("math_advanced")


def main_history():
    check_and_prompt(_PACKAGE)
    run("history")


def main_art():
    check_and_prompt(_PACKAGE)
    run("art")


def main_coding_basics():
    check_and_prompt(_PACKAGE)
    run("coding_basics")
