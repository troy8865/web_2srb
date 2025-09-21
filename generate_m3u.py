import os
from datetime import datetime

links = [
    {"name": "sports-trgolas-b1", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayin1.m3u8"},
    {"name": "sports-trgolas-b2", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinb2.m3u8"},
    {"name": "sports-trgolas-b3", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinb3.m3u8"},
    {"name": "sports-trgolas-b4", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinb4.m3u8"},
    {"name": "sports-trgolas-b5", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinb5.m3u8"},
    {"name": "sports-trgolas-ss1", "url": "http://example.com/stream2.m3u8"},
    {"name": "sports-trgolas-ss2", "url": "http://example.com/stream2.m3u8"},
    {"name": "sports-trgolas-sm1", "url": "http://example.com/stream2.m3u8"},
    {"name": "sports-trgolas-sm2", "url": "http://example.com/stream2.m3u8"},
    {"name": "sports-trgolas-ts", "url": "http://example.com/stream2.m3u8"},
]

OUTPUT_DIR = "m3u_files"

def sanitize_filename(name):
    """Fayl adlarında problem yarada biləcək simvolları çıxarır"""
    return "".join(c for c in name if c.isalnum() or c in "-_")

def create_m3u_files(channels):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Köhnə faylları sil
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith(".m3u8"):
            os.remove(os.path.join(OUTPUT_DIR, file))

    # Yeni faylları yarat
    for channel in channels:
        safe_name = sanitize_filename(channel["name"])
        filename = os.path.join(OUTPUT_DIR, f"{safe_name}.m3u")
        content = f"""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=5500000,AVERAGE-BANDWIDTH=8976000,RESOLUTION=1920x1080,CODECS="avc1.640028,mp4a.40.2",FRAME-RATE=25,SUBTITLES="subs"
{channel['url']}
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"{filename} yaradıldı ✅ ({channel['name']})")

if __name__ == "__main__":
    print(f"⏳ Script başladı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    create_m3u_files(links)
    print("✅ Bütün kanallar yeniləndi.\n")
