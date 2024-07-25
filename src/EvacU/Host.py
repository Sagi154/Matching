
class Host:
    id: str
    first_name: str
    last_name: str
    city: str
    max_guests: int
    requirements: str

    def __init__(self, id: str, first_name: str, last_name: str, city: str, max_guests: int, requirements: str) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.max_guests = max_guests
        self.requirements = requirements
