from dataclasses import dataclass


@dataclass
class Actor:
    id: str
    name: str
    height: int
    date_of_birth: str
    known_for_movies: str

    def __str__(self):
        return f"l'attore '{self.name}' nato nel {self.date_of_birth}"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id