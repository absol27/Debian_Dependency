from utils.scrape_snapshot_helper import get_debian_bydate, date_to_ISO
from utils.parse_packagelist import populate_DB
from gen_graph import generate_graph

date = date_to_ISO("2019-10-04")
ARCH = "amd64"

get_debian_bydate(date, ARCH)

populate_DB(date, ARCH)

generate_graph(date = "sample", ARCH= "sample") # sample graph for a smaller subset of data, using Packagelist_DUMP test file

#Dec 2016 - 2022