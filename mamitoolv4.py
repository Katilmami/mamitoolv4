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
clear()
main()
print("""
İslemler

1) Discord Nitro Gen
2) Spam Discord Webhook
3) DdoS Attack
4) İp To Location
5) Discord İnvite Bilgi
Q) Cıkış

""")

islemno =input("İslem numarasini giriniz: ")

if islemno=="1":
        clear()
        os.system("python3 .discord.py")
elif islemno=="2":
          clear()
          os.system("python3 .spamwebhook.py")
elif islemno=="3":
          clear()
          os.system("python3 .ddos.py")
elif islemno=="4":
          clear()
          os.system("python3 .iptolocation.py")
elif islemno=="5":
          clear()
          os.system("python3 .discordinvite.py")
elif islemno=="q" or islemno=="Q":
          quit()

else:
     os.system("python3 mamitoolv4.py")