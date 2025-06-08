# 引入 OpenAI SDK 和 Mem0 的记忆模块
from openai import OpenAI
from mem0 import Memory
import os
class MemoryStore:
    def __init__(self):
        # 设置 OpenAI API Key 和自定义的 Base URL（适用于自托管或代理）
        os.environ["OPENAI_API_KEY"] = "sk-8a1ed1b559ce48a589da5e6c671882a5"
        os.environ["OPENAI_BASE_URL"] = "https://dashscope.aliyuncs.com/compatible-mode/v1/"

        # 定义 Mem0 的配置，包括 LLM 模型信息和向量数据库（使用 Chroma）
        config = {
            "llm": {
                "provider": "openai",  # 使用 OpenAI 提供的模型
                "config": {
                    "model": "qwen-turbo-latest",  # 模型名称
                    "temperature": 0.2,      # 输出的随机程度（越小越稳定）
                    "max_tokens": 2000,      # 最大输出长度
                }
            },
            "embedder": {
                "provider": "openai",
                "config": {
                    "model": "text-embedding-v2",
                    "embedding_dims": 1536
                }
            },
            "vector_store": {
                "provider": "chroma",       # 使用 Chroma 作为向量存储
                "config": {
                    "collection_name": "test",  # 数据集合名
                    "path": "db",               # Chroma 数据库存储路径
                }
            }
        }

        # text-embedding-v2
        # 初始化 OpenAI 客户端
        openai_client = OpenAI(
            api_key = "sk-123456",
            base_url = "http://127.0.0.1:8080/openai/v1"
        )

        # 根据上述配置初始化记忆对象
        self.memory = Memory.from_config(config)
