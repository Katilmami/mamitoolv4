import requests

def ip_to_location(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    data = response.json()
    if data['status'] == 'success':
        return f"IP adresi: {data['query']}, Konum: {data['city']}, {data['regionName']}, {data['country']}, Koordinatlar: {data['lat']}, {data['lon']}"
    else:
        return "Konum bulunamadı."

ip = input("Bir IP adresi girin: ")
print(ip_to_location(ip))
