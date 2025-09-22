import requests
import re
import os
import shutil

print("🚀 goals.py çalışmaya başladı...")

# Trgoals domain kontrol
base = "https://trgoals"
domain = ""

print("🔍 Uygun domain aranıyor...")
for i in range(1393, 2101):
    test_domain = f"{base}{i}.xyz"
    try:
        response = requests.head(test_domain, timeout=3)
        if response.status_code == 200:
            domain = test_domain
            print(f"✅ Çalışır domain bulundu: {domain}")
            break
    except Exception as e:
        continue  # sessizce geç

if not domain:
    print("❌ UYARI: Hiçbir domain çalışmıyor — script sonlanıyor.")
    exit(1)  # 👈 CRON'DA BU exit() YÜZÜNDEN ÇIKIYOR OLABİLİR

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

# ========== KLÖRÜ TAMAMEN TEMİZLEME ==========
folder_name = "channels_files"

print(f"🧹 {folder_name} klasörü temizleniyor...")

if os.path.exists(folder_name):
    try:
        shutil.rmtree(folder_name)
        print(f"🗑️  {folder_name} fiziksel olarak silindi.")
    except Exception as e:
        print(f"⚠️  Silme hatası: {e} — Tek tek siliniyor...")
        for root, dirs, files in os.walk(folder_name, topdown=False):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except:
                    pass
            for dir in dirs:
                try:
                    os.rmdir(os.path.join(root, dir))
                except:
                    pass
        try:
            os.rmdir(folder_name)
            print(f"🗑️  {folder_name} elle silindi.")
        except:
            print(f"❌ {folder_name} silinemedi — devam ediliyor.")

# Klasörü yeniden oluştur
try:
    os.makedirs(folder_name, exist_ok=False)
    print(f"📁 {folder_name} yeniden oluşturuldu.")
except FileExistsError:
    print(f"⚠️  {folder_name} hâlâ var — zorla siliniyor...")
    shutil.rmtree(folder_name)
    os.makedirs(folder_name)
    print(f"✅ {folder_name} zorla yeniden oluşturuldu.")
except Exception as e:
    print(f"❌ Klasör oluşturulamadı: {e}")
    exit(1)

# ========== KANAL DOSYALARI OLUŞTURMA ==========
print(f"📺 {len(channel_ids)} kanal işleniyor...")

created_count = 0
for channel_id, channel_name in channel_ids.items():
    channel_url = f"{domain}/channel.html?id={channel_id}"
    try:
        r = requests.get(channel_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
        match = re.search(r'const baseurl = "(.*?)"', r.text)
        if match:
            baseurl = match.group(1)
            full_url = f"http://proxylendim101010.mywire.org/proxy.php?url={baseurl}{channel_id}.m3u8"

            m3u_content = f"""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=5500000,AVERAGE-BANDWIDTH=8976000,RESOLUTION=1920x1080,CODECS="avc1.640028,mp4a.40.2",FRAME-RATE=25
{full_url}
"""

            safe_filename = "".join(c if c.isalnum() or c in " ._-" else "_" for c in channel_name)
            file_path = os.path.join(folder_name, f"{safe_filename}.m3u8")

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(m3u_content)

            print(f"✅ {channel_name} → {safe_filename}.m3u8 yazıldı.")
            created_count += 1
        else:
            print(f"❌ {channel_name} için baseurl bulunamadı.")
    except Exception as e:
        print(f"⚠️ {channel_name} işlenirken hata: {e}")

print(f"🎉 Toplam {created_count} dosya oluşturuldu.")
print("✅ goals.py başarıyla tamamlandı.")
