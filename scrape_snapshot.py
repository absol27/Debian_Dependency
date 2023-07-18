from utils.scrape_snapshot_helper import get_debian_bydate, date_to_ISO
from utils.parse_packagelist import populate_DB
from gen_graph import generate_graph
import datetime
import matplotlib.pyplot as plt
from utils.DB_helper import *

# date = date_to_ISO("2019-10-04")
# ARCH = "arm64"

# get_debian_bydate(date, ARCH)

# populate_DB(date, ARCH)

# generate_graph(date = "sample", ARCH= "sample") # sample graph for a smaller subset of data, using Packagelist_DUMP test file

if __name__ == "__main__":
    LOCATION = 'debian_packages.db'
    ARCH = "amd64"
    date = datetime.date(2016, 12, 31)
    end_date = datetime.date(2022, 12, 31)
    while date < end_date:
        print(date.strftime("%Y-%m-%d"))
        get_debian_bydate(date_to_ISO(date.strftime("%Y-%m-%d")), ARCH)
        populate_DB(date_to_ISO(date.strftime("%Y-%m-%d")), ARCH, LOCATION)
        # generate_graph(date, ARCH)
        date += datetime.timedelta(days=90)
    pass

def SQL_query(sql):
    conn = open_db()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return result

    # analyze and plot the DB for the following: 
    # 1. number of packages that are new by added_at date (i.e. first snapshot they appear in)
    # 2. main, contrib, non-free breakdown of all packages and total number of packages
    # 3. number of packages that are new in each snapshot, broken down by main, contrib, non-free
    # 4. packages that has the most dependencies
    # 5. packages with most versions
    # 8. Packages that are updated the most (i.e. most versions) based on added_at date

    # # 1. plot a graph showing packages by added_at date
    # sql = "SELECT added_at, COUNT(*) FROM Publish_Packages GROUP BY added_at"
    # results = SQL_query(sql)
    # x = [row[0][2:4]+"-"+row[0][4:6] for row in results]
    # y = [row[1] for row in results]
    # plt.plot(x, y)
    # plt.xlabel("Date")
    # plt.ylabel("Number of Packages")
    # plt.title("Number of Packages by Added_at Date")
    # plt.show()


    # # 2. plot a pie chart showing main, contrib, non-free breakdown of all packages
    # sql = "SELECT COUNT(*) FROM Publish_Packages WHERE DFSG = 'main'"
    # conn = open_db()
    # cur = conn.cursor()
    # cur.execute(sql)
    # main = cur.fetchone()[0]
    # conn.close()
    # sql = "SELECT COUNT(*) FROM Publish_Packages WHERE DFSG = 'contrib'"
    # conn = open_db()
    # cur = conn.cursor()
    # cur.execute(sql)
    # contrib = cur.fetchone()[0]
    # conn.close()
    # sql = "SELECT COUNT(*) FROM Publish_Packages WHERE DFSG = 'non-free'"
    # conn = open_db()
    # cur = conn.cursor()
    # cur.execute(sql)
    # non_free = cur.fetchone()[0]
    # conn.close()
    # labels = 'main', 'contrib', 'non-free'
    # sizes = [main, contrib, non_free]
    # explode = (0, 0, 0)
    # fig1, ax1 = plt.subplots()
    # ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
    # ax1.axis('equal')
    # plt.title("Main, Contrib, Non-free Breakdown of All Packages")
    # plt.show()

    # 4. plot a graph showing packages that has the most dependencies
    # sql = "SELECT Package, COUNT(*) FROM Publish_Dependencies GROUP BY Package ORDER BY COUNT(*) DESC LIMIT 10"
    # results = SQL_query(sql)
    # x = [row[0] for row in results]
    # y = [row[1] for row in results]
    # plt.bar(x, y)
    # plt.xlabel("Package Name")
    # plt.ylabel("Number of Dependencies")
    # plt.title("Packages that has the Most Dependencies")
    # plt.show()

    # sql = '''
    #     SELECT Dependency, COUNT(*) AS dependency_count
    #     FROM Publish_Dependencies
    #     GROUP BY Dependency
    #     ORDER BY dependency_count DESC
    #     LIMIT 10;
    # '''
    # results = SQL_query(sql)
    # package_names = [row[0] for row in results]
    # dependency_counts = [row[1] for row in results]
    # plt.bar(package_names, dependency_counts)
    # plt.xlabel("Package Name")
    # plt.ylabel("Dependency Count")
    # plt.title("Top 10 Packages with Highest Dependency Counts")
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()