
class Host:
    first_name: str
    last_name: str
    city: str
    max_guests: int
    requirements: str

    def __init__(self, first_name: str, last_name: str, city: str, max_guests: int, requirements: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.max_guests = max_guests
        self.requirements = requirements
