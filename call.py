import requests

# リクエストヘッダーとペイロードデータを定義
headers = {
    "Content-Type": "application/json"
}
data = {
    "name": "dummy",
    "age": 21,
    "friends": ["dummy1", "dummy2", "dummy3"],
    "is_man": False
}

# POSTリクエストを送信
url = 'http://127.0.0.1:5000/try_rest'
response = requests.post(url, headers=headers, json=data)

# レスポンスのステータスコードとコンテンツを表示
print(f"Status Code: {response.status_code}")
print("Response:")
print(response.text)

# JSONデータの取得とfriendsのループでの出力
response_json = response.json()
friends = response_json.get('friends', [])

print("Friends:")
for friend in friends:
    print(friend)
