import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# 🚨 需要修改的部分 🚨
TARGET_URL = "https://weibo.com/u/1705586121"  # ← 替换成你的目标网址
FANS_SELECTOR = ".#app > div.woo-box-flex.woo-box-column.Frame_wrap_3g67Q > div.woo-box-flex.Frame_content_3XrxZ.Frame_noside1_3M1rh.Frame_noside2_1lBwY > div:nth-child(2) > main > div > div > div.woo-panel-main.woo-panel-top.woo-panel-right.woo-panel-bottom.woo-panel-left.Card_wrap_2ibWe.Card_bottomGap_2Xjqi > div.woo-box-flex.woo-box-alignStart.ProfileHeader_box1_1qC-g > div.woo-box-item-flex > div.woo-box-flex.woo-box-alignCenter.ProfileHeader_h4_gcwJi > a:nth-child(1) > span"                  # ← 替换成网页元素选择器

# 自动记录当前日期
today = datetime.now().strftime("%Y-%m-%d")

# 尝试抓取数据
try:
    headers = {'User-Agent': 'Mozilla/5.0'}  # 假装是浏览器
    response = requests.get(TARGET_URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 提取粉丝数（关键步骤，需要根据实际网页调整）
    fan_count = soup.select_one(FANS_SELECTOR).text.strip()
    
    # 准备新数据
    new_data = {'日期': [today], '粉丝数': [fan_count]}
    
    # 读取旧数据或创建新表格
    try:
        df = pd.read_csv('data.csv')
    except:
        df = pd.DataFrame(columns=['日期', '粉丝数'])
    
    # 合并新数据
    new_df = pd.DataFrame(new_data)
    df = pd.concat([df, new_df], ignore_index=True)
    
    # 保存到文件
    df.to_csv('data.csv', index=False)
    
except Exception as e:
    print(f"出错啦: {e}")
