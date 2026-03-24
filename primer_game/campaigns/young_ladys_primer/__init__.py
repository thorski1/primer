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
    CHAPTER_ENTRY_SUMMARIES,
    PLACEMENT_QUESTIONS,
)

BANNER_ASCII = """
    ✦  ·  ˚  ·  ✦  ·  ˚  ·  ✦  ·  ˚  ·  ✦  ·  ˚  ·  ✦

 ██████╗ ██████╗ ██╗███╗   ███╗███████╗██████╗
 ██╔══██╗██╔══██╗██║████╗ ████║██╔════╝██╔══██╗
 ██████╔╝██████╔╝██║██╔████╔██║█████╗  ██████╔╝
 ██╔═══╝ ██╔══██╗██║██║╚██╔╝██║██╔══╝  ██╔══██╗
 ██║     ██║  ██║██║██║ ╚═╝ ██║███████╗██║  ██║
 ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

    ✦  ·  ˚  ·  ✦  ·  ˚  ·  ✦  ·  ˚  ·  ✦  ·  ˚  ·  ✦
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
    placement_questions=PLACEMENT_QUESTIONS,
    chapters=[
        ChapterDef(
            pack_name="letters",
            title="The Letter Garden",
            recommended_age="5-7",
            intro_bridge=CHAPTER_INTROS["letters"],
            outro_bridge=CHAPTER_OUTROS["letters"],
            # No entry_summary for the first chapter
        ),
        ChapterDef(
            pack_name="numbers",
            title="The Counting Kingdom",
            recommended_age="6-8",
            intro_bridge=CHAPTER_INTROS["numbers"],
            outro_bridge=CHAPTER_OUTROS["numbers"],
            entry_summary=CHAPTER_ENTRY_SUMMARIES["numbers"],
        ),
        ChapterDef(
            pack_name="science",
            title="The World of Wondering",
            recommended_age="7-10",
            intro_bridge=CHAPTER_INTROS["science"],
            outro_bridge=CHAPTER_OUTROS["science"],
            entry_summary=CHAPTER_ENTRY_SUMMARIES["science"],
        ),
        ChapterDef(
            pack_name="kindness",
            title="The Art of Being Kind",
            recommended_age="6+",
            intro_bridge=CHAPTER_INTROS["kindness"],
            outro_bridge=CHAPTER_OUTROS["kindness"],
            entry_summary=CHAPTER_ENTRY_SUMMARIES["kindness"],
        ),
    ],
)
