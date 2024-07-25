
class Guest:
    id: str
    first_name: str
    last_name: str
    city: str
    number_of_guests: int
    info: str

    def __init__(self, id:str,  first_name: str, last_name: str, city: str, number_of_guests: int, info: str) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.number_of_guests = number_of_guests
        self.info = info
