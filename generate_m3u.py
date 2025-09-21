import os
from datetime import datetime

links = [
    {"name": "sports-trgolas-sms2", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinsms2.m3u8"},
    {"name": "sports-trgolas-1", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayin1.m3u8"},
    {"name": "sports-trgolas-as", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinas.m3u8"},
    {"name": "sports-trgolas-atv", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinatv.m3u8"},
    {"name": "sports-trgolas-b2", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinb2.m3u8"},
    {"name": "sports-trgolas-b3", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinb3.m3u8"},
    {"name": "sports-trgolas-b4", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinb4.m3u8"},
    {"name": "sports-trgolas-b5", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinb5.m3u8"},
    {"name": "sports-trgolas-bm1", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinbm1.m3u8"},
    {"name": "sports-trgolas-bm2", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinbm2.m3u8"},
    {"name": "sports-trgolas-eu1", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayineu1.m3u8"},
    {"name": "sports-trgolas-eu2", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayineu2.m3u8"},
    {"name": "sports-trgolas-ex1", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinex1.m3u8"},
    {"name": "sports-trgolas-ex2", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinex2.m3u8"},
    {"name": "sports-trgolas-ex3", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinex3.m3u8"},
    {"name": "sports-trgolas-ex4", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinex4.m3u8"},
    {"name": "sports-trgolas-ex5", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinex5.m3u8"},
    {"name": "sports-trgolas-ex6", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinex6.m3u8"},
    {"name": "sports-trgolas-ex7", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinex7.m3u8"},
    {"name": "sports-trgolas-f1", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinf1.m3u8"},
    {"name": "sports-trgolas-nbatv", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinnbatv.m3u8"},
    {"name": "sports-trgolas-smarts", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinsmarts.m3u8"},
    {"name": "sports-trgolas-ss", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinss.m3u8"},
    {"name": "sports-trgolas-ss2", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinss2.m3u8"},
    {"name": "sports-trgolas-t1", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayint1.m3u8"},
    {"name": "sports-trgolas-t2", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayint2.m3u8"},
    {"name": "sports-trgolas-t3", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayint3.m3u8"},
    {"name": "sports-trgolas-t4", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayint4.m3u8"},
    {"name": "sports-trgolas-trt1", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayintrt1.m3u8"},
    {"name": "sports-trgolas-trtspor", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayintrtspor.m3u8"},
    {"name": "sports-trgolas-trtspor2", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayintrtspor2.m3u8"},
    {"name": "sports-trgolas-tv8", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayintv8.m3u8"},
    {"name": "sports-trgolas-tv85", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayintv85.m3u8"},
    {"name": "sports-trgolas-zirve", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayinzirve.m3u8"},
]

OUTPUT_DIR = "m3u_files"

def sanitize_filename(name):
    """Fayl adlarında problem yarada biləcək simvolları çıxarır"""
    return "".join(c for c in name if c.isalnum() or c in "-_")

def create_m3u_files(channels):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Köhnə faylları sil
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith(".m3u"):
            os.remove(os.path.join(OUTPUT_DIR, file))

    # Yeni faylları yarat
    for channel in channels:
        safe_name = sanitize_filename(channel["name"])
        filename = os.path.join(OUTPUT_DIR, f"{safe_name}.m3u8")
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
