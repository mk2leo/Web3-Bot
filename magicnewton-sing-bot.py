import requests
import time
import json
import os

# 获取当前时间（毫秒级 Unix 时间戳）
current_time = int(time.time() * 1000)  # 当前时间（毫秒）
session_timeout = 1800000  # 30分钟（1800秒 = 1800000毫秒）
expires_at = current_time + session_timeout  # 过期时间

# 定义 wagmi.store 的 JSON 并转义
wagmi_store = json.dumps({
    "state": {
        "connections": {"__type": "Map", "value": []},
        "chainId": 1,
        "current": None
    },
    "version": 2
})

# 從青龍面板環境變量獲取基礎 Cookie...MAGICNEWTON_COOKIE 請登入網站後F12.把整個COOKIE 貼上到變量中
base_cookie = os.getenv("MAGICNEWTON_COOKIE", "")

# 動態替換 Cookie 中的時間相關變量
cookie = base_cookie.format(
    current_time=current_time,
    expires_at=expires_at,
    session_timeout=session_timeout,
    wagmi_store=wagmi_store
)

# 请求的 URL
url = "https://www.magicnewton.com/portal/api/userQuests"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/json",
    "sec-ch-ua-platform": "Windows",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "origin": "https://www.magicnewton.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.magicnewton.com/portal/rewards",
    "accept-language": "zh-CN,zh-MO;q=0.9,zh;q=0.8,zh-TW;q=0.7,en;q=0.6,be;q=0.5",
    "priority": "u=1, i",
    "Cookie": cookie
}

# 请求体
data = {
    "questId": "f56c760b-2186-40cb-9cbc-3af4a3dc20e2",
    "metadata": {}
}

# 发送 POST 请求并添加错误处理
try:
    response = requests.post(url, headers=headers, json=data)
    # 打印响应状态码和内容
    print(f"Status Code: {response.status_code}")
    print("Response Headers:", response.headers)
    print("Response Body:", response.text)
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
