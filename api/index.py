"""
Vercel entrypoint for The Young Lady's Illustrated Primer — serves all 10 chapters via the hub.

Vercel routes all HTTP traffic here via vercel.json.

    /               → Chapter chooser (hub landing page)
    /letters/       → The Letter Garden
    /numbers/       → The Counting Kingdom
    /science/       → The World of Wondering
    ... and so on for all 10 chapters.

To serve only a single chapter, set QUEST_PACK in Vercel's Environment
Variables dashboard (e.g. QUEST_PACK=letters). Leave unset for the full hub.
"""

import os
import sys
from pathlib import Path

# Make the repo root importable so primer_game/ is available as a package.
_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT))

# Point the engine at the skill-packs bundled inside primer_game/.
import primer_game as _pkg  # noqa: E402
_PACKS_DIR = str(Path(_pkg.__file__).parent / "skill-packs")
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", _PACKS_DIR)

from engine.skill_pack import load_skill_pack  # noqa: E402

_PRIMER_PACKS = [
    "letters", "numbers", "science", "kindness", "geography",
    "math_advanced", "history", "art", "coding_basics", "space",
    "music", "animals", "words", "cooking", "body", "money", "environment", "thinking", "telling_time", "inventions", "oceans", "civics",
]

def _make_app():
    _single_pack = os.environ.get("QUEST_PACK", "")
    if _single_pack:
        # Single-pack mode: serve one chapter at the root.
        from engine.web.server import create_app
        return create_app(load_skill_pack(_single_pack, packs_dir=_PACKS_DIR))
    # Hub mode (default): serve all 10 chapters.
    from engine.web.hub import create_hub_app
    _packs = [load_skill_pack(p, packs_dir=_PACKS_DIR) for p in _PRIMER_PACKS]
    return create_hub_app(_packs)


app = _make_app()
