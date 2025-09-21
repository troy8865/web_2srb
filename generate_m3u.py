import yaml
import os

# Linkləri buraya əlavə edirsən
links = [
    {"name": "Kanal 1", "url": "http://proxylendim101010.mywire.org/proxy.php?url=https://five.4928d54d950ee70q45.lat/yayin1.m3u8"},
    {"name": "Kanal 2", "url": "http://example.com/stream2.m3u8"}
]

YAML_FILE = "channels.yaml"

def save_to_yaml(channels, yaml_file=YAML_FILE):
    """Linkləri YAML faylına yazır"""
    data = {"channels": channels}
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)
    print(f"✅ {yaml_file} yeniləndi")

def create_m3u_files(channels):
    """Hər kanal üçün ayrıca .m3u faylı yaradır"""
    # Köhnə m3u faylları silək
    for file in os.listdir():
        if file.endswith(".m3u"):
            os.remove(file)

    for i, channel in enumerate(channels, start=1):
        filename = f"kanal_{i}.m3u"
        content = f"""#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=5500000,AVERAGE-BANDWIDTH=8976000,RESOLUTION=1920x1080,CODECS="avc1.640028,mp4a.40.2",FRAME-RATE=25,SUBTITLES="subs"
{channel['url']}
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"{filename} yaradıldı ✅ ({channel['name']})")

if __name__ == "__main__":
    # YAML faylını yenilə
    save_to_yaml(links)

    # m3u faylları yarat
    create_m3u_files(links)
