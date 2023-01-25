import csv

def read_books(file_name):
    books = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

def search_author(author, books):
    return [book for book in books if book['author'] == author]

def search_isbn(isbn, books):
    for book in books:
        if book['ISBN'] == isbn:
            return {'title': book['title'], 'price': book['price']}
    return None

def search_price(min_price, max_price, books):
    return [book for book in books if float(book['price']) >= min_price and float(book['price']) <= max_price]

def add_book(title, author, ISBN, price, file_name):
    fieldnames = ['title', 'author', 'ISBN', 'price']
    with open(file_name, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'title': title, 'author': author, 'ISBN': ISBN, 'price': price})

books = read_books('books.csv')
while True:
    print("1. Search by author")
    print("2. Search by ISBN")
    print("3. Search by price range")
    print("4. Add a new book")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        author = input("Enter author name: ")
        print(search_author(author, books))
    elif choice == '2':
        isbn = input("Enter ISBN: ")
        print(search_isbn(isbn, books))
    elif choice == '3':
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        print(search_price(min_price, max_price, books))
    elif choice == '4':
        title = input("Enter title: ")
        author = input("Enter author: ")
        ISBN = input("Enter ISBN: ")
        price = input("Enter price: ")
        add_book(title, author, ISBN, price, 'books.csv')
    elif choice == '5':
        break
    else:
        print("Invalid input. Please try again.")
