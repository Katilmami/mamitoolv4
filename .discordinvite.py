import json
import requests


discord_server_invite_code = input("Discord sunucu davet kodunu girin: ")

if not discord_server_invite_code:
    print("Geçersiz discord_server_invite_code.")
    exit()

response = requests.get(f"https://discord.com/api/v9/invites/{discord_server_invite_code}?with_counts=true")
if response.status_code != 200:
    print("Discord API'sine istek yapılırken bir sorun oluştu, lütfen daha sonra tekrar deneyin.")
    exit()

data = response.json()

print("Type:", data["type"])
print("Code:", data["code"])
print("Expires At:", data["expires_at"])
print("Flags:", data["flags"])
print("Approximate Member Count:", data["approximate_member_count"])
print("Approximate Presence Count:", data["approximate_presence_count"])

print("Inviter:")
print("ID:", data["inviter"]["id"])
print("Username:", data["inviter"]["username"])
print("Avatar:", data["inviter"]["avatar"])
print("Discriminator:", data["inviter"]["discriminator"])
print("Public Flags:", data["inviter"]["public_flags"])
print("Flags:", data["inviter"]["flags"])
print("Global Name:", data["inviter"]["global_name"])
print("Guild ID:", data["guild"]["id"])
print("Guild Name:", data["guild"]["name"])
print("Features:", data["guild"]["features"])
print("Verification Level:", data["guild"]["verification_level"])
print("Approximate Member Count:", data["approximate_member_count"])
print("Approximate Presence Count:", data["approximate_presence_count"])
print("Channel ID:", data["channel"]["id"])
print("Channel Type:", data["channel"]["type"])
print("Channel Name:", data["channel"]["name"])
