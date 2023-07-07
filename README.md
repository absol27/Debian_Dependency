# Generate a Dependency Graph from Debian Snapshot

Query a snapshot using Architecture and Date, get a list of all packages and it's dependencies from the stable distro at the selected date.
Generate a network graph of the dependencies.

## Steps

- Set Architecture and Dates in scrape_snpashot.py
- Fetches nearest available snapshot and the stable distro at the set date
- Downloads metadata of **published** binary packages in main, non-free, and contrib (for that ARCH)
- Decompresses and stores the metadata in Packagelist_DUMP
- Parse package info and insert it in DB
- Parse dependencies for each package and insert them into a table linking to the package table
