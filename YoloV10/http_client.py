import requests
# 定义 URL 数组
url_list_error = [
    "http://qhai.yuhuangdadi.top/2407/202407/1714113903.2250.jpg11111",
    "http://qhai.yuhuangdadi.top/2407/202407/1714112103.1289.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1714110303.2201.jpg",
]

# 定义 URL 数组
url_list_success = [
    "http://qhai.yuhuangdadi.top/2407/202407/1706853602.8558.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1709967001.4621.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1714112103.1289.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1706857802.5730.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1709968501.7308.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1714113903.2250.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1707099001.2447.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1709968501.8202.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1714117503.5497.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1707120001.3617.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1710488702.6718.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1715116502.8265.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1707120601.8431.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1710497701.2787.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1715149802.6687.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1707194702.5664.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1710532501.3304.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1715216702.4185.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1707208201.7329.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1710793801.1975.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1715221802.3245.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1707253502.3492.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1713231301.9620.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1716157505.4830.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1709238602.7237.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1714110303.2201.jpg",
]

# 定义 URL 数组
url_list_all = [
    "http://qhai.yuhuangdadi.top/2407/202407/1706853602.8558.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1706857802.5730.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1707099001.2447.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1707120001.3617.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1707120601.8431.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1707194702.5664.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1707208201.7329.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1707253502.3492.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1709238602.7237.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1709967001.4621.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1709968501.7308.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1709968501.8202.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1710488702.6718.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1710497701.2787.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1710532501.3304.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1710793801.1975.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1713231301.9620.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1714110303.2201.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1714112103.1289.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1714113903.2250.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1714117503.5497.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1715116502.8265.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1715149802.6687.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1715216702.4185.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1715221802.3245.jpg",
    "http://qhai.yuhuangdadi.top/2407/202407/1716157505.4830.jpg",
]

# 发送 POST 请求的函数
def send_post_request(url):
    api_endpoint = "http://qhai.yuhuangdadi.top/queue/sendQueue/queue"  # 替换为实际 API 端点
    payload = {"url": url}
    try:
        response = requests.post(api_endpoint, json=payload)
        response.raise_for_status()  # 如果响应码不是 200，会抛出异常
        print(f"成功发送请求，状态码: {response.status_code}, 响应内容: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")

for _ in range(1):
    for url in url_list_error:
        send_post_request(url)
