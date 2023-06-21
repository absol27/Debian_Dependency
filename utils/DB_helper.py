import sqlite3

LOCATION = 'debian_packages.db'

def init_db(location = LOCATION):
    conn = sqlite3.connect(location)
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS Publish_Packages ("
                   "Package_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "Package varchar,"
                   "Architecture varchar,"
                   "Version varchar,"
                   "Section varchar,"
                   "Size varchar,"
                   "Filename varchar,"
                   "DFSG varchar,"
                   "Added_at TIMESTAMP,"
                   "Unique (Package, Architecture, Version) ON CONFLICT IGNORE"
                   ")")  
    
    cur.execute("CREATE TABLE IF NOT EXISTS Publish_Dependencies ("
                   "Dependency_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "Package_id INTEGER,"
                   "Dependency_package varchar,"
                   "Condition varchar,"
                   "FOREIGN KEY (Package_id) REFERENCES Publish_Packages (Package_id)"
                   "ON DELETE CASCADE ON UPDATE CASCADE"
                   ")")

    conn.commit()
    conn.close()

def open_db(location = LOCATION):
    conn = sqlite3.connect(location)
    return conn

def close_db(conn = None):
    if not conn:
        raise Exception("I need a database handle to close!")
    conn.close()

INSERT_PACKAGE = '''INSERT OR IGNORE INTO Publish_Packages (package, architecture, version, section, size, filename, DFSG, added_at) VALUES (?,?,?,?,?,?,?,?)'''
INSERT_DEPENDENCY = '''INSERT OR IGNORE INTO Publish_Dependencies (package_id, condition, dependency_package) VALUES (?,?,?)'''

def insert_package(cur, package_data, DFSG):
    cur.execute(INSERT_PACKAGE, (package_data['package'], package_data['architecture'], package_data['version'], package_data['section'], package_data['size'], package_data['filename'], DFSG, package_data['added_at']))

def insert_dependeny(cur, package, version, architecture, dependency_condition, dependency):
    # cur.execute(INSERT_DEPENDENCY, (package_data["package"], package_data["version"], package_data["condition"], package_data["dependency"]))
    package_query = "SELECT Package_id FROM Publish_Packages WHERE Package = ? AND Version = ? AND Architecture = ?"
    package_id = cur.execute(package_query, (package, version, architecture)).fetchone()
    if package_id:
        cur.execute(INSERT_DEPENDENCY, (package_id[0], dependency_condition, dependency))
    else:
        print("Package not found.")

def get_packages_and_dependencies(conn, package_name=None, architecture=None):
    query = """
    SELECT p.Package, p.Architecture, p.Version, d.Dependency_package
    FROM Publish_Packages p
    LEFT JOIN Publish_Dependencies d ON p.Package_id = d.Package_id
    """

    conditions = []

    if package_name:
        conditions.append(f"p.Package = '{package_name}'")

    if architecture:
        conditions.append(f"p.Architecture = '{architecture}'")

    if conditions:
        query += "WHERE " + " AND ".join(conditions)

    cursor = conn.execute(query)
    rows = cursor.fetchall()

    packages = {}
    for row in rows:
        package = row[0]
        architecture = row[1]
        version = row[2]
        dependency_package = row[3]

        if package not in packages:
            packages[package] = {
                "Package": package,
                "Architecture": architecture,
                "Version": version,
                "Dependencies": []
            }

        packages[package]["Dependencies"].append(
            dependency_package
        )

    return list(packages.values())

# def recentPackages(cur):
#     sql = "SELECT COUNT(*) FROM packages WHERE added_at = (SELECT MIN(added_at) FROM packages)"
#     cur.execute(sql)
#     return cur.fetchall()