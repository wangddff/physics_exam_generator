import os
from crewai import LLM

def get_deepseek_llm():
    """
    配置DeepSeek模型
    """
    return LLM(
        model="deepseek-chat",
        base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        temperature=0.7
    )