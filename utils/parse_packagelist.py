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
                parsed_package["added_at"] = date
                cur = con.cursor()
                parsed_package["architecture"] = ARCH
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
                    for dependency_condition in dependency_list:
                        if '(' in dependency_condition:
                            dependency_package_name = dependency_condition.split('(')[0]
                        else:
                            dependency_package_name = dependency_condition
                        cur = con.cursor()
                        insert_dependeny(cur, parsed_package["package"], parsed_package["version"], ARCH, dependency_condition, dependency_package_name)
                        con.commit()
                header = ""
            else:
                header += line
    close_db(con)
    return

def populate_DB(date, ARCH, LOCATION):
    init_db(LOCATION)
    for DFSG in ["main", "contrib", "non-free"]:
        parse_packagelist(date, ARCH, LOCATION, DFSG)
        parse_dependencylist(date, ARCH, LOCATION, DFSG)