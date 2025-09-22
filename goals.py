import requests
import re
import os

# Trgoals domain kontrol
base = "https://trgoals"
domain = ""

for i in range(1393, 2101):
    test_domain = f"{base}{i}.xyz"
    try:
        response = requests.head(test_domain, timeout=3)
        if response.status_code == 200:
            domain = test_domain
            break
    except:
        continue

if not domain:
    print("Çalışır bir domain bulunamadı.")
    exit()

# Kanallar ve isimleri
channel_ids = {
    "yayinzirve": "beIN Sports 1 ☪️",
    "yayininat": "beIN Sports 1 ⭐",
    "yayin1": "beIN Sports 1 ♾️",
    "yayinb2": "beIN Sports 2",
    "yayinb3": "beIN Sports 3",
    "yayinb4": "beIN Sports 4",
    "yayinb5": "beIN Sports 5",
    "yayinbm1": "beIN Sports 1 Max",
    "yayinbm2": "beIN Sports 2 Max",
    "yayinss": "Saran Sports 1",
    "yayinss2": "Saran Sports 2",
    "yayint1": "Tivibu Sports 1",
    "yayint2": "Tivibu Sports 2",
    "yayint3": "Tivibu Sports 3",
    "yayint4": "Tivibu Sports 4",
    "yayinsmarts": "Smart Sports",
    "yayinsms2": "Smart Sports 2",
    "yayintrtspor": "TRT Spor",
    "yayintrtspor2": "TRT Spor 2",
    "yayinas": "A Spor",
    "yayinatv": "ATV",
    "yayintv8": "TV8",
    "yayintv85": "TV8.5",
    "yayinnbatv": "NBA TV",
    "yayinex1": "Tâbii 1",
    "yayinex2": "Tâbii 2",
    "yayinex3": "Tâbii 3",
    "yayinex4": "Tâbii 4",
    "yayinex5": "Tâbii 5",
    "yayinex6": "Tâbii 6",
    "yayinex7": "Tâbii 7",
    "yayinex8": "Tâbii 8"
}

# Çıkartmak istediğiniz örnek link ve ayar formatı:
# Bu örneği kendi veri ve ihtiyacınıza göre düzenleyebilirsiniz.
def generate_m3u_content(url):
    return f"""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=5500000,AVERAGE-BANDWIDTH=8976000,RESOLUTION=1920x1080,CODECS="avc1.640028,mp4a.40.2",FRAME-RATE=25,SUBTITLES="subs"
{url}
"""

# Klasör oluştur
folder_name = "channels_files"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Her kanal için dosya oluşturuyoruz
for channel_id, channel_name in channel_ids.items():
    channel_url = f"{domain}/channel.html?id={channel_id}"
    try:
        r = requests.get(channel_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        match = re.search(r'const baseurl = "(.*?)"', r.text)
        if match:
            baseurl = match.group(1)
            # Tek URL örneği, ihtiyaca göre liste veya farklı varyantlar eklenebilir
            full_url = f"http://proxylendim101010.mywire.org/proxy.php?url={baseurl}{channel
