"""
The Young Lady's Illustrated Primer — the campaign.
An adventure through words and numbers, guided by Puck.
"""

from engine.campaign import Campaign, ChapterDef
from .story import (
    CAMPAIGN_INTRO,
    CAMPAIGN_FINAL,
    CHAPTER_INTROS,
    CHAPTER_OUTROS,
)

BANNER_ASCII = r"""
 _____ _         _____     _
|_   _| |_  ___ |  __ \   (_)
  | | | ' \/ _ \| |__) | _ _ _ __ ___   ___ _ __
  | | | . | __/|  ___/ | | | '_ ` _ \ / _ \ '__|
  |_| |_|_|\___||_|    |_|_| | | | | |  __/ |
                              |_|_|_| |_|\___|_|
"""

CAMPAIGN = Campaign(
    id="young_ladys_primer",
    title="THE YOUNG LADY'S ILLUSTRATED PRIMER",
    subtitle="◈  Letters · Numbers · Science · Kindness — With Puck as Your Guide  ◈",
    save_file_name="young_ladys_primer",
    intro_story=CAMPAIGN_INTRO,
    final_story=CAMPAIGN_FINAL,
    quit_message="The Primer rests. Puck is keeping your place. Come back whenever you're ready!",
    banner_ascii=BANNER_ASCII,
    player_name_prompt="What's your name?",
    default_player_name="Explorer",
    chapters=[
        ChapterDef(
            pack_name="letters",
            title="The Letter Garden",
            intro_bridge=CHAPTER_INTROS["letters"],
            outro_bridge=CHAPTER_OUTROS["letters"],
        ),
        ChapterDef(
            pack_name="numbers",
            title="The Counting Kingdom",
            intro_bridge=CHAPTER_INTROS["numbers"],
            outro_bridge=CHAPTER_OUTROS["numbers"],
        ),
        ChapterDef(
            pack_name="science",
            title="The World of Wondering",
            intro_bridge=CHAPTER_INTROS["science"],
            outro_bridge=CHAPTER_OUTROS["science"],
        ),
        ChapterDef(
            pack_name="kindness",
            title="The Art of Being Kind",
            intro_bridge=CHAPTER_INTROS["kindness"],
            outro_bridge=CHAPTER_OUTROS["kindness"],
        ),
    ],
)
