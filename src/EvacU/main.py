from Guest import *
from Host import *
import sqlite3

DB_NAME: str = "UsersDB.db"


def new_guest():
    # add to database
    # scan for hosts
    pass


def new_host():
    pass


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


def add_host_to_db(host):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            command = """INSERT OR IGNORE INTO Hosts (ID, First_Name, Last_Name, City, max_guests, Availability, requirements) 
            VALUES(?, ?, ?, ?, ?, 1, ?);"""
            conn.execute(command,
                         (host.id, host.first_name, host.last_name, host.city, host.max_guests, host.requirements))
            conn.commit()
    except sqlite3.OperationalError as err:
        if "database is locked" in str(err):
            print("Database is locked")


def main():
    guest = Guest("207190401", "hagi", "Eis", "Shoham", 3, "Has huge bulbul")
    add_guest_to_db(guest)
    host = Host("207190406", "Sagit", "Eis", "ashdod", 3, "Has microscopic bulbul")
    add_host_to_db(host)


if __name__ == "__main__":
    main()
