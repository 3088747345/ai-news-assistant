import feedparser


def fetch_news(source, limit=5):
    """
    获取RSS新闻

    source格式:

    {
        "name": "GameSpot",
        "category": "Game",
        "url": "https://xxx"
    }
    """

    feed = feedparser.parse(source["url"])

    news_list = []

    for entry in feed.entries[:limit]:

        news_list.append(
            {
                "source": source["name"],
                "category": source["category"],
                "title": entry.title,
                "link": entry.link
            }
        )

    return news_list

