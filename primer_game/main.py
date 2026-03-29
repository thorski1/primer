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

# _HERE is the primer_game/ package directory — works both in development
# (repo/primer_game/) and when installed via uv/pip (site-packages/primer_game/).
_HERE = Path(__file__).parent
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", str(_HERE / "skill-packs"))
os.environ.setdefault("QUEST_CAMPAIGNS_DIR", str(_HERE / "campaigns"))

from engine.main import run, run_campaign          # noqa: E402
from engine.updater import check_and_prompt        # noqa: E402

_PACKAGE = "primer-quest"
_PACKS_DIR = str(_HERE / "skill-packs")   # primer_game/skill-packs/

_WEB = "--web" in sys.argv

PRIMER_PACKS = [
    "letters", "numbers", "science", "kindness", "geography",
    "math_advanced", "history", "art", "coding_basics", "space",
    "music", "animals", "words", "cooking", "body", "money", "environment", "thinking", "time",
]


def _web(pack_name: str, port: int = 8080):
    """Launch the web interface for *pack_name*."""
    from engine.web.server import serve
    serve(pack_name, port=port, packs_dir=_PACKS_DIR)


def main_primer():
    if _WEB:
        from engine.web.hub import serve_hub
        serve_hub(PRIMER_PACKS, port=8080, packs_dir=_PACKS_DIR)
        return
    check_and_prompt(_PACKAGE)
    run_campaign("young_ladys_primer")


def main_letters():
    if _WEB:
        _web("letters")
        return
    check_and_prompt(_PACKAGE)
    run("letters")


def main_numbers():
    if _WEB:
        _web("numbers")
        return
    check_and_prompt(_PACKAGE)
    run("numbers")


def main_science():
    if _WEB:
        _web("science")
        return
    check_and_prompt(_PACKAGE)
    run("science")


def main_kindness():
    if _WEB:
        _web("kindness")
        return
    check_and_prompt(_PACKAGE)
    run("kindness")


def main_geography():
    if _WEB:
        _web("geography")
        return
    check_and_prompt(_PACKAGE)
    run("geography")


def main_math_advanced():
    if _WEB:
        _web("math_advanced")
        return
    check_and_prompt(_PACKAGE)
    run("math_advanced")


def main_history():
    if _WEB:
        _web("history")
        return
    check_and_prompt(_PACKAGE)
    run("history")


def main_art():
    if _WEB:
        _web("art")
        return
    check_and_prompt(_PACKAGE)
    run("art")


def main_coding_basics():
    if _WEB:
        _web("coding_basics")
        return
    check_and_prompt(_PACKAGE)
    run("coding_basics")


def main_space():
    if _WEB:
        _web("space")
        return
    check_and_prompt(_PACKAGE)
    run("space")


def main_music():
    if _WEB:
        _web("music")
        return
    check_and_prompt(_PACKAGE)
    run("music")


def main_animals():
    if _WEB:
        _web("animals")
        return
    check_and_prompt(_PACKAGE)
    run("animals")


def main_words():
    if _WEB:
        _web("words")
        return
    check_and_prompt(_PACKAGE)
    run("words")


def main_cooking():
    if _WEB:
        _web("cooking")
        return
    check_and_prompt(_PACKAGE)
    run("cooking")


def main_body():
    if _WEB:
        _web("body")
        return
    check_and_prompt(_PACKAGE)
    run("body")


def main_money():
    if _WEB:
        _web("money")
        return
    check_and_prompt(_PACKAGE)
    run("money")


def main_environment():
    if _WEB:
        _web("environment")
        return
    check_and_prompt(_PACKAGE)
    run("environment")


def main_thinking():
    if _WEB:
        _web("thinking")
        return
    check_and_prompt(_PACKAGE)
    run("thinking")


def main_time():
    if _WEB:
        _web("time")
        return
    check_and_prompt(_PACKAGE)
    run("time")
