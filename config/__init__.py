print("Config package initialized.")

DEBUG = True

# MODEL ------------------------------------------------------------------------

# 模型支持OpenAI规范接口
GPT_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions'
MODEL = 'qwen-turbo-latest'
API_KEY = 'sk-8a1ed1b559ce48a589da5e6c671882a5'
SYSTEM_PROMPT = 'You are a helpful assistant.'

# MODEL ------------------------------------------------------------------------

# CONFIGURATION ------------------------------------------------------------------------

# 意图相关性判断阈值0-1
RELATED_INTENT_THRESHOLD = 0.5

# CONFIGURATION ------------------------------------------------------------------------
