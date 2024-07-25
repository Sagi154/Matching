from Guest import *
from Host import *
import sqlite3

DB_NAME: str = "UsersDB.db"


def new_guest():
    #add to data base
    #scan for hosts
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
    pass


def main():
    guest = Guest("207190406", "Sagi", "Eis", "Shoham", 3, "Has huge bulbul")
    add_guest_to_db(guest)


if __name__ == "__main__":
    main()