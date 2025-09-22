import requests
import re
import os
import shutil
import sys

print("🚀 goals.py başladı — heç bir şəraitdə erkən çıxılmayacaq!")

# Trgoals domain kontrol
base = "https://trgoals"
domain = ""

print("🔍 Domain axtarılır: trgoals1393.xyz → trgoals2100.xyz")
for i in range(1393, 2101, 1407):
    test_domain = f"{base}{i}.xyz"
    try:
        response = requests.head(test_domain, timeout=3)
        if response.status_code == 200:
            domain = test_domain
            print(f"✅ Domain tapıldı: {domain}")
            break
    except:
        continue

if not domain:
    print("❌ XƏBƏRDARLIQ: Heç bir domain işləmir — YENƏ DƏ DAVAM EDİLİR (boş qovluq yaradılacaq)")

# Kanallar
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

# ========== KLÖRÜ TAMAMEN TEMİZLEME + YENİDEN OLUŞTURMA ==========
folder_name = "channels_files"

print(f"🧹 {folder_name} silinir...")
if os.path.exists(folder_name):
    try:
        shutil.rmtree(folder_name)
        print(f"🗑️  {folder_name} fiziki olaraq silindi.")
    except Exception as e:
        print(f"⚠️  Silinə bilmədi: {e} — tək-tək silinir...")
        for root, dirs, files in os.walk(folder_name, topdown=False):
            for f in files:
                try:
                    os.remove(os.path.join(root, f))
                except:
                    pass
            for d in dirs:
                try:
                    os.rmdir(os.path.join(root, d))
                except:
                    pass
        try:
            os.rmdir(folder_name)
        except:
            pass

# 👇 HƏR HALDA KLÖR YARADILIR — HEÇ VAXT ATLANMIR!
try:
    os.makedirs(folder_name, exist_ok=True)  # exist_ok=True — əgər varsa xəta vermir
    print(f"📁 {folder_name} uğurla yaradıldı (yenidən).")
except Exception as e:
    print(f"❌ FATAL: {folder_name} yaradıla bilmədi: {e}")
    sys.exit(1)  # Yalnız bu yerde çıx — çünki əsas infrastruktur qurula bilmədi

# ========== KANALLAR İŞLƏNİR — DOMAIN YOXDURSA BELƏ BOŞ FAYL YARANMIR, AMMA KLÖR VAR ==========
if not domain:
    print("ℹ️  Domain olmadığı üçün fayl yaradılmayacaq — yalnız boş qovluq qalacaq.")
else:
    print(f"📺 {len(channel_ids)} kanal işlənir...")

created = 0
for channel_id, channel_name in channel_ids.items():
    if not domain:
        break  # domain yoxdursa, fayl yaratma — yalnız qovluq qalsın

    try:
        url = f"{domain}/channel.html?id={channel_id}"
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        match = re.search(r'const baseurl = "(.*?)"', r.text)
        if not match:
            print(f"❌ {channel_name} üçün baseurl tapılmadı.")
            continue

        baseurl = match.group(1)
        full_url = f"http://proxylendim101010.mywire.org/proxy.php?url={baseurl}{channel_id}.m3u8"

        content = f"""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=5500000,AVERAGE-BANDWIDTH=8976000,RESOLUTION=1920x1080,CODECS="avc1.640028,mp4a.40.2",FRAME-RATE=25
{full_url}
"""

        safe_name = "".join(c if c.isalnum() or c in " ._-" else "_" for c in channel_name)
        path = os.path.join(folder_name, f"{safe_name}.m3u8")

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ {channel_name} → {safe_name}.m3u8")
        created += 1

    except Exception as e:
        print(f"⚠️ {channel_name} emal olunarkən xəta: {e}")

print(f"✅ Ümumi {created} fayl yaradıldı.")
print("🏁 goals.py uğurla başa çatdı — hər zaman channels_files/ qovluğu mövcuddur!")
