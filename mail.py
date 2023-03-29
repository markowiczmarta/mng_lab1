import re


class EmailExtractor:

    def __init__(self, emailD):
        self.email = emailD

    def is_student(self) -> bool:
        x = re.compile(r"(?<=\@)\w+")
        if x.match(self.email) == "student":
            return True
        else:
            return False

    def get_name(self):
        x = re.compile(r"/^\w+/")
        x.match(self.email)
        pass

    def get_surname(self):
        x = re.compile(r"(?<=\.)\w+")  # poprawic tak zeby nie lapalo 01 jako nazwiska
        x.match(self.email)
        pass

    def is_men(self) -> bool:
        x = re.compile(r"/^\w+/")
        if x.endswith("a"):
            return False
        else:
            return True
