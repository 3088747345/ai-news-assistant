from feedgen.feed import FeedGenerator
from pathlib import Path
from datetime import datetime
import html


def generate_rss(content):

    fg = FeedGenerator()

    base_url = "https://3088747345.github.io/ai-news-assistant/"

    fg.id(base_url)

    fg.title(
        "AI News Daily"
    )

    fg.description(
        "AI自动生成科技、游戏、动漫新闻日报"
    )

    fg.link(
        href=base_url,
        rel="alternate"
    )


    fe = fg.add_entry()

    today = datetime.now().strftime("%Y-%m-%d")

    article_url = base_url + today

    fe.id(article_url)

    fe.link(
        href=article_url
    )

    fe.title(
        f"AI News Daily {today}"
    )

    fe.description(
        html.escape(content)
    )


    Path("docs").mkdir(
        exist_ok=True
    )

    fg.rss_file(
        "docs/daily.xml"
    )
