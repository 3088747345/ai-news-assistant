import openai
import os


openai.api_key = os.getenv("DEEPSEEK_API_KEY")

openai.api_base = "https://api.deepseek.com"


def summarize_news(news_list):

    news_text = ""

    for news in news_list:
        news_text += f"""
     来源:{news['source']}
     分类:{news['category']}
     标题:{news['title']}
     链接:{news['link']}

     """


    response = openai.ChatCompletion.create(
        model="deepseek-chat",
        messages=[
            {
              "role": "system",
              "content": """
            你是一名科技新闻分析助手。

            请根据提供的新闻内容生成日报。

            要求：
            1. 总结新闻核心事件，并分析影响。
            2. 按 AI科技、游戏、动漫娱乐分类整理。
            3. 只基于提供的信息，不编造内容。
            4. 使用 Markdown 格式输出。
            5. 最后总结当天主要行业趋势。
            """
            },
            {
                "role": "user",
                "content": news_text
            }
        ]
    )


    return response["choices"][0]["message"]["content"]

