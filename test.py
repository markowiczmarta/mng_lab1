import unittest

from mail import EmailExtractor


class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],

            ["marta.markowicz@student.wat.edu.pl", True, False, "Marta", "Markowicz"],
            ["rafal.marczuk@student.wat.edu.pl", True, True, "Rafal", "Marczuk"],
            ["aleksandra.nowicka@wat.edu.pl", False, False, "Aleksandra", "Nowicka"],
            ["aleksander.nowicki@wat.edu.pl", False, True, "Aleksander", "Nowicki"],
            ["olga.ostasz@student.wat.edu.pl", True, False, "Olga", "Ostasz"],
            ["jakub.koziarz@student.wat.edu.pl", True, True, "Jakub", "Koziarz"],
            ["malgorzata.pekala@wat.edu.pl", False, False, "Malgorzata", "Pekala"],
            ["krzysztof.barnabas@wat.edu.pl", False, True, "Krzysztof", "Barnabas"],
            ["kinga.markiewicz01@student.wat.edu.pl", True, False, "Kinga", "Markiewicz"],
            ["marcin.laskowski02@student.wat.edu.pl", True, True, "Marcin", "Laskowski"]
        ]

    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                mail = x[0]
                is_student = x[1]
                # then
                extractor = EmailExtractor(mail)
                # expect
                self.assertEqual(is_student, extractor.is_student())

    def test_is_male(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname, extractor.get_surname())


if __name__ == '__main__':
    unittest.main()
