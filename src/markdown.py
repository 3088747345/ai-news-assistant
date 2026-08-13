
from datetime import datetime


def generate_markdown(news_list):

    today = datetime.now().strftime("%Y-%m-%d")

    content = f"# AI新闻日报 {today}\n\n"

    for news in news_list:
        content += f"## {news['title']}\n\n"
        content += f"链接: {news['link']}\n\n"

    return content


if __name__ == "__main__":

    test_news = [
        {
            "title": "OpenAI发布新模型",
            "link": "https://openai.com"
        },
        {
            "title": "Flutter更新",
            "link": "https://flutter.dev"
        }
    ]

    md = generate_markdown(test_news)

    print(md)
