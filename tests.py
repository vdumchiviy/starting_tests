import unittest
from mock import patch
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print(f"\n/================ Start {self} ================")
        print(f"| ==== setup main.documents and main.directories ")
        main.documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        main.directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }
        print(f"| -----------------------------------------------------------------------------------")

    def tearDown(self):
        print(f"| -----------------------------------------------------------------------------------")
        print(f"\\================ End {self}  ================\n")

    def test_delete_document(self):
        expected_documents = [
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        main.delete_document_from_documents("2207 876234")
        actual_documents = main.documents
        self.assertListEqual(actual_documents, expected_documents)

    def test_print_all_documnets(self):
        expected = 'passport "2207 876234" "Василий Гупкин"' + \
            'invoice "11-2" "Геннадий Покемонов"' + 'insurance "10006" "Аристарх Павлов"'
        actual = main.print_all_documents()
        self.assertMultiLineEqual(expected, actual)

    @patch('builtins.input', lambda *args: '5')
    def test_add_new_shelf(self):
        expected = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': [],
            '5': []
        }
        main.add_new_shelf()
        actual = main.directories
        self.assertDictEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
