import os

def install_requirements():
    try:
        os.system("pip3 install -r requirements.txt") 
    except:
        os.system("pip install -r requirements.txt")
install_requirements()

def main():
    try:
        os.system("clear") 
    except:
        os.system("cls") 
    text = "MAMİTOOL INSTALLER"
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)
  
def clear():
    try:
        os.system("clear")
    except:
        os.system("cls") 



print("KURULUM BİTTİ")
os.system("python mamitoolv4.py")