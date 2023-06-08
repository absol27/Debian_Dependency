# Generate a Dependency Graph from Debian Snapshot

Query a snapshot using Architecture and Date, get a list of all packages and it's dependencies from the stable distro at the selected date.
Generate a network graph of the dependencies.

## Steps

- Set Architecture and Date in scrape_snpashot.py
- Fetches neareast available snapshot and the stable distro at the set date
- Downloads metadata of binary packages in main, non-free and contrib (for that ARCH)
- Decompresses and stores the metadata in Packagelist_DUMP
- Parse package info and insert in DB
- Parse dependencies for each package and insert into a table linking to the package table

## Todo

- Integrate code with other components of debian supply chain
- Currently runs for one date and selected ARCH