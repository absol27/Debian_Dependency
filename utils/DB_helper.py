import sqlite3

LOCATION = 'debian_packages.db'

def init_db(location = LOCATION):
    conn = sqlite3.connect(location)
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Packages ("
                   "Package varchar PRIMARY KEY,"
                   "Architecture varchar,"
                   "Version varchar,"
                   "Section varchar,"
                   "Size varchar,"
                   "Filename varchar,"
                   "DFSG varchar"
                   ")")  
    
    cur.execute("CREATE TABLE IF NOT EXISTS Dependencies ("
                   "Package varchar,"
                   "Condition varchar,"
                   "Dependency varchar,"
                   "FOREIGN KEY (Package) REFERENCES Packages (Package)"
                   "ON DELETE CASCADE ON UPDATE CASCADE,"
                   "FOREIGN KEY (Dependency) REFERENCES Packages (Package)"
                   "ON DELETE CASCADE ON UPDATE CASCADE"
                   ")")

    # unique(source_id,type,build_date),

    conn.commit()
    conn.close()

def open_db(location = LOCATION):
    conn = sqlite3.connect(location)
    return conn

def close_db(conn = None):
    if not conn:
        raise Exception("I need a database handle to close!")
    conn.close()

INSERT_DEPENDENCY = '''INSERT OR IGNORE INTO Dependencies (package, condition, dependency) VALUES (?,?,?)'''
INSERT_PACKAGE = '''INSERT OR IGNORE INTO Packages (package, architecture, version, section, size, filename, DFSG) VALUES (?,?,?,?,?,?,?)'''

def insert_package(cur, package_data, DFSG):
    cur.execute(INSERT_PACKAGE, (package_data['package'], package_data['architecture'], package_data['version'], package_data['section'], package_data['size'], package_data['filename'], DFSG))

def insert_dependeny(cur, package_data):
    cur.execute(INSERT_DEPENDENCY, (package_data["package"], package_data["condition"], package_data["dependency"]))