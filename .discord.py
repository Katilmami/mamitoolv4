import requests
import random
import string
import os
import pyfiglet

def main():
    try:
        os.system("clear") 
    except:
        os.system("cls") 
    text = "MAMİTOOL"
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)
  
def clear():
    try:
        os.system("clear")
    except:
        os.system("cls") 

clear()
print("")
print("")
print("")
main()
print("")
print("")
print("")
print("")
print("")
print("")


iteration_count = int(input("Kaç kez deneme yapmak istersiniz? "))

found_valid_code = False 

for _ in range(iteration_count):

    nitro_code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    print("Rastgele Discord Nitro Kodu:", nitro_code)


    api_url = f"https://discord.com/api/v10/entitlements/gift-codes/{nitro_code}"
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Bu Nitro kodu geçerli.")
        found_valid_code = True 
        break 
    else:
        print("Bu Nitro kodu geçersiz.")

if found_valid_code:
    print("Geçerli bir Nitro kodu bulundu.")
else:
    print("Geçerli bir Nitro kodu bulunamadı.")