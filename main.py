# documents = [
#     {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#     {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#     {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
# ]

# directories = {
#     '1': ['2207 876234', '11-2', '5455 028765'],
#     '2': ['10006'],
#     '3': []
# }
documents = list()
directories = dict()


# Вспомогательные функции


def get_shelf(doc_number):
    for shelf in directories:
        if doc_number in directories[shelf]:
            return shelf


def get_document(doc_number):
    for document in documents:
        if document['number'] == doc_number:
            return document


def delete_document_from_documents(doc_number):
    has_delete = False
    for document in documents:
        if document['number'] == doc_number:
            documents.remove(document)
            has_delete = True
            print(f"   Документ с номером {doc_number} удалён из Каталога")
            return doc_number
    if not has_delete:
        print(f"   Документ {doc_number} отсутствует в Каталоге")
        return None


def delete_document_from_shelves(doc_number):
    shelf = get_shelf(doc_number)
    if shelf is None:
        print(f"   Документ {doc_number} отсутствует на полках")
        return None
    else:
        directories[shelf].remove(doc_number)
        print(f"   Документ {doc_number} удалён с полки номер {shelf}")
        return doc_number


def has_shelf_exists(shelf):
    if shelf in directories.keys():
        return True
    return False


# Основные функции из меню
def print_name_from_document_number():
    doc_number = input("   Введите номер документа: ")
    document = get_document(doc_number)
    if document is None:
        print(f"   Документ {doc_number} отсутствует в Каталоге")
        return None
    else:
        print(
            f"   Документ {doc_number} принадлежит человеку по имени {document['name']}")
        return document['name']


def print_shelf_from_document_number():
    doc_number = input("   Введите номер документа: ")
    shelf = get_shelf(doc_number)
    if shelf is None:
        print(f"   Документ {doc_number} на полках отсутствует")
        return None
    else:
        print(f"   Документ {doc_number} находится на полке номер {shelf}")
        return shelf


def print_all_documents():
    result = ""
    for document in documents:
        tmp = f'{document["type"]} "{document["number"]}" "{document["name"]}"'
        result = result + tmp
        print(tmp)
    return result


def add_new_document_to_shelf():
    shelves = list()
    for shelf in directories:
        shelves.append(shelf)
    doc_type = input("   Введите тип документа: ")
    doc_number = input("   Введите номер документа: ")
    doc_owner = input("   Введите ФИО владельца документа: ")
    while True:
        # Вероятно было бы грустно вводить документы и ошибиться в номере полке, поэтому цикл
        doc_shelf = input(
            "   Введите номер полки (q - отмена ввода документа): ")
        if doc_shelf in shelves:
            break
        elif shelf == "q":
            return None
        elif doc_shelf not in shelves:
            print(f"   Полка {doc_shelf} отсутствует")
    documents.append(
        {"type": doc_type, "number": doc_number, "name": doc_owner})
    directories[doc_shelf].append(doc_number)
    print(f"Документ {doc_number} добавлен на полку {doc_shelf}")
    return {doc_number: doc_shelf}


def delete_document():
    doc_number = input("   Введите номер документа для удаления: ")
    # if get_document(doc_number) == None:
    #   print("   Документ {doc_number} отсутствует в Каталоге")
    # else
    #   return
    if delete_document_from_documents(doc_number) is not None or delete_document_from_shelves(doc_number) is not None:
        return True
    return False


def move_document_from_shelf_to_shelf():
    doc_number = input("   Введите номер перемещаемого документа: ")
    doc_from_shelf = get_shelf(doc_number)
    if doc_from_shelf is None:
        print(f"   Документ {doc_number} отсутствует на полках")
        return
    doc_shelf = input(
        f"   Введите номер полки, куда должен переместиться документ {doc_number}: ")
    if not has_shelf_exists(doc_shelf):
        print(f"   Полка {doc_shelf} не существует")
        return
    delete_document_from_shelves(doc_number)
    directories[doc_shelf].append(doc_number)
    print(f"   , и перемещён на полку номер {doc_shelf}")


def add_new_shelf():
    new_shelf = input(f"   Введите номер новой полки: ")
    if new_shelf not in directories.keys():
        directories[new_shelf] = []
        print(f"Полка {new_shelf} создана")
    else:
        print(f"Полка {new_shelf} уже существует")


def print_all_shelves():
    for shelf in directories:
        print(
            f"На полке {shelf} содержатся следующие документы: {directories[shelf]}")


def main():

    while True:
        command = input(
            "\nВведите команду (\np (people), \ns (shelf), " +
            "\nl (list documents), \na (add), \nd (delete), " +
            "\nm (move), \nas (add shelf), \nls (list shelves) " +
            "\nлюбая другая - выход): ")
        if command == 'p':
            print_name_from_document_number()
        elif command == 's':
            print_shelf_from_document_number()
        elif command == 'l':
            print_all_documents()
        elif command == 'a':
            add_new_document_to_shelf()
        elif command == 'd':
            delete_document()
        elif command == 'm':
            move_document_from_shelf_to_shelf()
        elif command == 'as':
            add_new_shelf()
        elif command == 'ls':
            print_all_shelves()
        else:
            break


if __name__ == "__main__":
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

    directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
    }
    main()
