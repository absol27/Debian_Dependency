import requests
import gzip
import datetime

def get_debian_bydate(date, ARCH="arm"):
    for DFSG in ["main", "contrib", "non-free"]:
        url = f"http://snapshot.debian.org/archive/debian/{date}/dists/stable/{DFSG}/binary-{ARCH}/Packages.gz"
        resp = requests.get(url)
        if resp.status_code == 200:
            decompressed_file = gzip.decompress(resp.content)
            with open(f"Packagelist_DUMP/{date}-{ARCH}-{DFSG}_Packages", "w") as f:
                f.write(decompressed_file.decode('utf-8'))
        else:
            print("Error: " + str(resp.status_code), url)
    return date

def date_to_ISO(date):
    date_object = datetime.datetime.strptime(date, "%Y-%m-%d")
    iso_8601_format = date_object.strftime("%Y%m%dT%H%M%S") + "Z"
    return iso_8601_format