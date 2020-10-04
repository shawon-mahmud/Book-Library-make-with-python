class Library:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lend_books = {}
        self.add_books = {}

    def display_book(self):
        for book in self.list_of_books:
            print(book)

    def lend_book(self):
        name = input('Enter your name: ').lower()
        book_name = input('Which book you want to lend: ')
        if book_name in self.list_of_books:
            self.lend_books[name] = book_name
            self.list_of_books.remove(book_name)
            print(f'{book_name} is lended by {name}')
            print(f'Thanks {name} for lending our book'
                  f'\nWe are waiting for return book.')
        else:
            print(f'{book_name} book is not in our Library')
        return self.list_of_books

    def add_book(self):
        aname = input('Enter your name: ').lower()
        abook_name = input('Enter your book name: ')
        self.list_of_books.append(abook_name)
        self.add_books[aname] = abook_name
        print(f'{aname} your book added successfully')

    def return_book(self):
        rname = input('Enter your name: ').lower()
        rbook_name = input('Enter book name: ')
        if rname in self.lend_books.keys():
            if rbook_name in self.lend_books.values():
                self.list_of_books.append(rbook_name)
                self.lend_books.pop(rname)
                print(f'Thanks {rname} for returning our book')
            else:
                print(f'{rname} you lend another book from our library')
        else:
            print("You don't lend any book from our library")


book_list = [
    'Harry Porter',
    'Rich Dad and Poor Dad',
    'A great Cook',
    'Think rich and grow rich',
    'Chomics',
    'Rymes'
]
Shawon_Library = Library(book_list, 'Shawon Library')

if __name__ == '__main__':
    print("\nRead it carefully.......\nTo Display book type 'd'\nTo lend book type 'l'"
          "\nTo add book type 'a'\nTo return book 'r'\nEnter 'x' to close")


    while True:
        user_input = input('\nType here: ').lower()

        if user_input == 'x':
            break
        elif user_input == 'd':
            Shawon_Library.display_book()

        elif user_input == 'l':
            Shawon_Library.lend_book()

        elif user_input == 'a':
            Shawon_Library.add_book()

        elif user_input == 'r':
            Shawon_Library.return_book()

        else:
            print('wrong input')

