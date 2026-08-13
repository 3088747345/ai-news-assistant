from feedgen.feed import FeedGenerator
from pathlib import Path
from datetime import datetime


def generate_rss(content):

    fg = FeedGenerator()

    fg.id(
        "https://3088747345.github.io/ai-news-assistant/"
    )

    fg.title(
        "AI News Daily"
    )

    fg.description(
        "AI自动生成科技、游戏、动漫新闻日报"
    )

    fg.link(
        href="https://3088747345.github.io/ai-news-assistant/",
        rel="alternate"
    )


    fe = fg.add_entry()

    today = datetime.now().strftime("%Y-%m-%d")

    fe.id(today)

    fe.title(
        f"AI News Daily {today}"
    )

    fe.description(
        content
    )


    Path("docs").mkdir(
        exist_ok=True
    )

    fg.rss_file(
        "docs/daily.xml"
    )
