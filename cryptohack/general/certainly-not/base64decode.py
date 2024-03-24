import base64

# ファイルをバイナリモードで読み込む
with open('2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der', 'rb') as f:
    encoded_data = f.read()

# データをBase64デコードする
decoded_data = base64.b64decode(encoded_data)

# デコードしたデータを出力する
print(decoded_data)