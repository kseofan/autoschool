from users.models import Person


class Curator(Person):

    def __str__(self):
        return Person.__str__(self) + '(Куратор)'
