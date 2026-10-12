
#!/usr/bin/env python3
"""Generate a weekly YouTube content plan using Python's standard library."""

import json
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "config" / "channel_config.json"
OUTPUT_DIR = ROOT / "content_plans"


def load_config():
    if not CONFIG.exists():
        raise SystemExit(f"Config file not found: {CONFIG}")

    with CONFIG.open(encoding="utf-8") as file:
        config = json.load(file)

    return config


def generate_plan(config, start_date):
    channel = config.get("channel_name", "ArushplayzLive")
    niche = config.get("niche", "BGMI / PUBG Mobile Gaming")
    language = config.get("language", "Hinglish")

    ideas = [
        {
            "format": "Anchor Video",
            "title": "BGMI Rank Push 🔥 | Intense Squad Gameplay",
            "thumbnail": "RANK PUSH",
            "description": "Watch our BGMI squad gameplay, intense fights and clutch attempts!",
            "hashtags": ["#BGMI", "#ArushPlayz", "#BGMIClutch"],
        },
        {
            "format": "Live Stream",
            "title": "BGMI LIVE 🔴 | Squad Rank Push & Intense Fights",
            "thumbnail": "LIVE RANK PUSH",
            "description": "Join the squad for BGMI rank push, fights and live chat!",
            "hashtags": ["#BGMILive", "#PUBGMobile", "#Gaming"],
        },
        {
            "format": "Short",
            "title": "Insane BGMI Clutch 😱 | Wait for the Finish!",
            "thumbnail": "1V4 CLUTCH",
            "description": "A BGMI clutch attempt. Watch till the end!",
            "hashtags": ["#Shorts", "#BGMI", "#GamingShorts"],
        },
        {
            "format": "Gameplay Video",
            "title": "BGMI Squad Fight 🔥 | Close Range Battles",
            "thumbnail": "SQUAD FIGHT",
            "description": "Close-range BGMI battles and squad gameplay highlights.",
            "hashtags": ["#BGMI", "#BGMIHighlights", "#Gaming"],
        },
        {
            "format": "Live Stream",
            "title": "ArushplayzLive 🔴 | BGMI Custom Rooms & Squad Fun",
            "thumbnail": "CUSTOM ROOMS",
            "description": "Squad gameplay and custom-room fun with the community.",
            "hashtags": ["#ArushPlayz", "#BGMILive", "#BGMI"],
        },
        {
            "format": "Short",
            "title": "BGMI Funny Moment 😂 | Squad Reaction",
            "thumbnail": "FUNNY MOMENT",
            "description": "A funny squad moment from BGMI gameplay.",
            "hashtags": ["#Shorts", "#BGMI", "#Gaming"],
        },
        {
            "format": "Community",
            "title": "Choose Our Next BGMI Challenge!",
            "thumbnail": "YOU DECIDE",
            "description": "Ask viewers to choose the next challenge in the comments.",
            "hashtags": ["#BGMI", "#ArushPlayz"],
        },
    ]

    lines = [
        f"# Weekly YouTube Content Plan — {start_date.isoformat()}",
        "",
        f"- **Channel:** {channel}",
        f"- **Niche:** {niche}",
        f"- **Language:** {language}",
        "- **Status:** DRAFT — review before publishing",
        "- **Note:** Ideas only; no live analytics or performance claims.",
        "",
    ]

    for day, idea in enumerate(ideas):
        publish_date = start_date + timedelta(days=day)
        lines.extend([
            f"## {publish_date.strftime('%A, %d %B %Y')}",
            f"**Format:** {idea['format']}",
            f"**Title draft:** {idea['title']}",
            f"**Thumbnail text:** {idea['thumbnail']}",
            f"**Description draft:** {idea['description']}",
            f"**Hashtags:** {' '.join(idea['hashtags'])}",
            "",
            "**Before posting:** Verify the footage, title and description.",
            "Do not claim a clutch, kill count or result unless the footage confirms it.",
            "",
        ])

    return "\n".join(lines)


def main():
    config = load_config()
    today = date.today()
    plan = generate_plan(config, today)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"weekly_plan_{today.isoformat()}.md"

    if output_file.exists():
        raise SystemExit(
            f"File already exists; refusing to overwrite: {output_file}"
        )

    output_file.write_text(plan, encoding="utf-8")
    print(f"Draft plan created: {output_file}")
    print("Status: DRAFT. Review every idea before publishing.")


if __name__ == "__main__":
    main()
