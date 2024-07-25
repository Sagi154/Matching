from Guest import *
from Host import *
import sqlite3

DB_NAME: str = "UsersDB.db"


def new_guest(data):
    guest = Guest(data["id"], data["first_name"], data["last_name"], data["city"], data["number_of_guests"], data["info"])
    add_guest_to_db(guest)
    available_hosts = scan_for_hosts(guest)
    return available_hosts

def new_host(data):
    host = Host(data["id"], data["first_name"], data["last_name"], data["city"], data["max_guests"],
                  data["requirements"])
    add_host_to_db(host)


def add_guest_to_db(guest):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            command = """INSERT OR IGNORE INTO Guests (ID, First_Name, Last_Name, City, Number_Of_Guests, Info) 
            VALUES(?, ?, ?, ?, ?, ?);"""
            conn.execute(command, (guest.id, guest.first_name, guest.last_name, guest.city, guest.number_of_guests, guest.info))
            conn.commit()
    except sqlite3.OperationalError as err:
        if "database is locked" in str(err):
            print("Database is locked")


def scan_for_hosts(guest):
    hosts_list = []
    try:
        with sqlite3.connect(DB_NAME) as conn:
            command = """ 
            SELECT * FROM Hosts 
            WHERE Availability = 1 AND ? <= Max_Guests;"""
            cursor = conn.execute(command, (guest.number_of_guests, ))
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            for row in rows:
                hosts_list.append(dict(zip(columns, row)))
            conn.commit()
    except sqlite3.OperationalError as err:
        if "database is locked" in str(err):
            print("Database is locked")
    return hosts_list


def add_host_to_db(host):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            command = """INSERT OR IGNORE INTO Hosts (ID, First_Name, Last_Name, City, max_guests, Availability, requirements) 
            VALUES(?, ?, ?, ?, ?, 1, ?);"""
            conn.execute(command, (host.id, host.first_name, host.last_name, host.city, host.max_guests, host.requirements))
            conn.commit()
    except sqlite3.OperationalError as err:
        if "database is locked" in str(err):
            print("Database is locked")


def main():
    guest = Guest("307190406", "hagi", "Eis", "Shoham", 2, "Has huge bulbul")
    add_guest_to_db(guest)
    host1 = Host("207490406", "Ido", "Eis", "Ashdod", 3, "Has microscopic bulbul")
    host2 = Host("807490406", "Yoav", "Eis", "Ashdod", 3, "Has microscopic bulbul")
    add_host_to_db(host1)
    add_host_to_db(host2)
    print(f"Hosts: {scan_for_hosts(guest)}")


if __name__ == "__main__":
    main()
