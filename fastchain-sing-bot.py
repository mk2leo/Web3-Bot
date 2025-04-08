import httpx
import os

# 從青龍面板中環境變量獲取 authorization token,,若本地運行請直接修改或AI修改
auth_token = os.environ.get('FASTCHAIN_TOKEN')  # 你需要在青龍面板設置這個變量

# 設置請求頭
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/json',
    'sec-ch-ua-platform': '"Windows"',
    'authorization': f'Bearer {auth_token}',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'origin': 'https://fastchain.org',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://fastchain.org/',
    'accept-language': 'zh-CN,zh-MO;q=0.9,zh;q=0.8,zh-TW;q=0.7,en;q=0.6,be;q=0.5',
    'priority': 'u=1, i'
}

# API 端點
url = 'https://api.fastchain.org/v2/check-in'

# 使用 httpx 發送 POST 請求並啟用 HTTP/2
try:
    with httpx.Client(http2=True) as client:
        response = client.post(url, headers=headers, json={})
        # 檢查響應
        if response.status_code == 200:
            print("簽到成功！")
            # 檢查 Content-Encoding 頭，確認是否有壓縮
            content_encoding = response.headers.get('Content-Encoding', '無壓縮')
            print(f"Content-Encoding: {content_encoding}")
            
            # 先嘗試以文本形式查看響應
            try:
                print("響應內容（文本）:", response.text)
                # 如果是 JSON，嘗試解析
                print("響應內容（JSON）:", response.json())
            except UnicodeDecodeError as decode_error:
                print(f"解碼錯誤：{decode_error}")
                print("原始字節內容:", response.content)  # 顯示原始字節
            except ValueError as json_error:
                print(f"JSON 解析錯誤：{json_error}")
                print("響應內容（文本）:", response.text)  # 如果不是 JSON，直接顯示文本
        else:
            print(f"簽到失敗，狀態碼：{response.status_code}")
            print("響應內容:", response.text)
except Exception as e:
    print(f"發生錯誤：{str(e)}")
