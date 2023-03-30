import re


class EmailExtractor:

    def __init__(self, email):
        self.email = email

    def is_student(self) -> bool:
        x = re.compile("(?<=\@)\w+")
        match = x.search(self.email)
        if match.group() == "student":
            return True
        else:
            return False

    def get_name(self):
        x = re.compile("(?P<name>^\w+)")
        match = x.search(self.email)
        name = match.group()
        return name.title()  # zamiana na wielka litere

    def get_surname(self):
        x = re.compile("(?<=\.)\w+[a-z]")
        match = x.search(self.email)
        surname = match.group()
        return surname.title()

    def is_men(self) -> bool:
        x = re.compile("(?P<name>^\w+)")
        match = x.search(self.email)
        name = match.group()
        if name.endswith("a"):
            return False
        else:
            return True
