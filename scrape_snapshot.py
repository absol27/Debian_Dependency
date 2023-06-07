from utils.scrape_snapshot_helper import get_debian_bydate, date_to_ISO
from utils.parse_packagelist import populate_DB

date = date_to_ISO("2019-10-04")
ARCH = "amd64"

get_debian_bydate(date, ARCH)

populate_DB(date, ARCH)