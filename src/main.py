from rss import fetch_news
from ai import summarize_news
from config import load_sources
from datetime import datetime


def main():

    print("读取新闻源配置...")

    sources = load_sources()


    all_news = []


    for source in sources:

        print(f"正在获取 {source['name']}")

        try:
             news = fetch_news(source)
             all_news.extend(news)

        except Exception:
             continue


    print(
        f"获取 {len(all_news)} 条新闻"
    )


    print("正在调用AI分析...")

    summary = summarize_news(all_news)


    today = datetime.now().strftime("%Y-%m-%d")

    filename = f"reports/{today}-news.md"


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(summary)


    print(
        f"日报生成完成: {filename}"
    )


if __name__ == "__main__":
    main()
