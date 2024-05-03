import requests

webhook_url = input("Discord webhook URL'sini girin: ")

message = input("Spam mesajınızı girin: ")

while True:
    requests.post(webhook_url, json={'content': message})
    print("mesaj gönderildi")