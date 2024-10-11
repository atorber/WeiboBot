from WeiboBot import Bot
from WeiboBot.const import *
import asyncio
import logging
from dotenv import load_dotenv
import os
# 加载 .env 文件中的环境变量
load_dotenv()

logging.basicConfig(level=logging.INFO)

# 从环境变量中读取 cookies、用户名和密码
cookies = os.getenv('WEIBO_COOKIES', '')

async def main():
    try:
        logging.info("实例化 Bot")
        myBot = Bot(cookies=cookies)  # 在异步函数内部实例化 Bot

        logging.info("开始登录")
        await asyncio.wait_for(myBot.login(), timeout=10)  # 先登录
        logging.info("登录成功")
        
        weibo_example1 = await myBot.get_weibo(1445403190)  # 获取微博
        # logging.info(f"获取到的微博: {weibo_example1}")
        console.info(weibo_example1)
        
        # weibo_example2 = await myBot.post_weibo("发一条微博", visible=VISIBLE.ALL)  # 发布微博
        # logging.info(f"发布的微博: {weibo_example2}")
        
        # ...... 其他操作
    except asyncio.TimeoutError:
        logging.error("登录超时，请检查网络连接或cookies是否有效。")
    except Exception as e:
        logging.error(f"发生错误: {e}", exc_info=True)
    finally:
        await myBot.close()  # 确保资源被正确关闭
        logging.info("资源已关闭")

if __name__ == '__main__':
    asyncio.run(main())