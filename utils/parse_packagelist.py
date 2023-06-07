from .headerparser_helper import parser
from .DB_helper import *
from .scrape_snapshot_helper import *

def parse_packagelist(date, ARCH, db_location, DFSG):
    con = open_db(db_location)
    with open(f'Packagelist_DUMP/{date}-{ARCH}-{DFSG}_Packages','r') as rf:
        header = ""
        for line in rf:
            if line == "\n":
                parsed_package =  parser.parse_string(header).normalized_dict()
                cur = con.cursor()
                insert_package(cur, parsed_package, DFSG)
                con.commit()
                header = ""
            else:
                header += line
    close_db(con)
    return

def parse_dependencylist(date, ARCH, db_location, DFSG):
    con = open_db(db_location)
    with open(f'Packagelist_DUMP/{date}-{ARCH}-{DFSG}_Packages','r') as rf:
        header = ""
        for line in rf:
            if line == "\n":
                parsed_package =  parser.parse_string(header).normalized_dict()
                for dependency_list in parsed_package["depends"]:
                    for dependency in dependency_list:
                        if '(' in dependency:
                            dependency_package_name = dependency.split('(')[0]
                        else:
                            dependency_package_name = dependency
                        cur = con.cursor()
                        insert_dependeny(cur, {"package": parsed_package["package"], "condition": dependency, "dependency": dependency_package_name})
                        con.commit()
                header = ""
            else:
                header += line
    close_db(con)
    return

def populate_DB(date, ARCH):
    LOCATION = 'debian_packages.db'
    init_db(LOCATION)
    for DFSG in ["main", "contrib", "non-free"]:
        parse_packagelist(date, ARCH, LOCATION, DFSG)
        parse_dependencylist(date, ARCH, LOCATION, DFSG)