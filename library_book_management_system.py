# THIS IS THE MAINUE
def menu():
    text = """1. Add Book
2. View Catalog 
3. Search Books
4. Update Details
5. Delete Book
6. Save to File
7. Load fromFile
8. Exit"""
    print("=" * 50)
    print("WELCOME TO DELIMITED FLAT-FILE CATALOG MANAGEMENTSYSTEM")
    print("=" * 50)
    print(text)
    print("-" * 50)
    try:
        choice = int(input("SELECT THE UNDER 1 TO 8 OPTION: "))
        return choice
    except ValueError as err:
        print("THE CHOICE UNDER THE NUM AND NOT ANY STRING VALUE.!")
        return -1


# THIS IS FOR ADD THE BOOK IN THE CATALOG.
def add_book_entry(catalog: list[dict], next_id: int):
    book = {}
    while True:
        title_ = input("ENTER THE TITLE OF THE BOOK:-> ").strip().title()
        if not title_.replace(" ", "").isalpha():
            print("RE WRITE THE NAME OF BOOK.")
        else:
            break

    while True:
        author_ = input("ENTER THE AUTHOR OF THE BOOK:-> ").strip().title()
        if not author_.replace(" ", "").isalpha():
            print("RE WRITE THE NAME OF AUTHOR.")
        else:
            break

    while True:
        genre_ = input("ENTER THE GENRE OF THE BOOK:-> ").strip().title()
        if not genre_.replace(" ", "").isalpha():
            print("RE WRITE THE NAME OF GENRE.")
        else:
            break

    while True:
        try:
            price_ = int(input("ENTER PRICE OF THE BOOK: "))
            if price_ < 0:
                print(
                    "PRICE OF THE PRODUCE MUST BE POSATIVE VALUE PLEASE RE ENTRT THR PRICE."
                )
            else:
                break
        except ValueError as err:
            print("ENTER THE VALIDE PRICE OF THE BOOK.")

    while True:
        try:
            copies_ = int(input("ENTER COPIES OF THE BOOK: "))
            if copies_ < 0:
                print(
                    "COPIES OF THE PRODUCE MUST BE POSATIVE VALUE PLEASE RE ENTRT THR."
                )
            else:
                break
        except ValueError as err:
            print("ENTER THE VALIDE COPIE OF THE BOOK.")

    book = {
        "id_": next_id,
        "title": title_,
        "author": author_,
        "genre": genre_,
        "price": price_,
        "copies": copies_,
    }
    catalog.append(book)
    print("BOOK ADD SUCCESFULLY IN THE CATALOG.")
    print(book)


# THIS IS FOR DISPLAY THE BOOK.
def render_catalog(catalog: list[dict]):
    if len(catalog) == 0:
        print("NO BOOK IS THERE IN THE CATALOG.")
    elif len(catalog) == 1:
        print("=" * 50)
        print("THE BOOK IS")
        print("=" * 50)
        print(f"""
        ID          : {catalog[0]['id_']}
        BOOK TITLE  : {catalog[0]['title']}
        AUTHOR NAME : {catalog[0]['author']}
        GENRE       : {catalog[0]['genre']}
        PRICE       : {catalog[0]['price']}
        COPIES      : {catalog[0]['copies']}""")
        print("-" * 50)
    else:
        print("=" * 100)
        print(
            f"{"ID":^5} {"Book Title":<30} {"Author Name":<20} {"Genre":<10} {"Price":>10}{"Copies":>10}"
        )
        print("=" * 100)
        for book in catalog:
            id_, title, author, genre, price, copies = book.values()
            print(
                f"{id_:^5} {title:<30} {author:<20} {genre:<10} {price:>10.2f}{copies:>10}"
            )
            print("-" * 100)


# THIS IS FOR THE ENTRY OF THE SEARCH QUERY V.1]
def serch_option():
    print("=" * 50)
    print("""1. SEARCH BY ID_
2. SEARCH BY AUTHOR NAME""")
    print("=" * 50)
    while True:
        try:
            choice = int(input("ENTERTHE COIHOICE HOW YOU WANT TO SEARCH WITH: "))
            break
        except ValueError as err:
            print("SELECT THE NUM UNDE 1 AND 2 NO OTHOR OPTION ARE THERE.")
    match choice:
        case 2:
            while True:
                search_term = (
                    input("ENTER THE NAME OF AUTHOR YOU ARE SEARCH FOR: ")
                    .strip()
                    .title()
                )
                if not search_term.replace(" ", "").isalpha():
                    print("PLEASE REENTER THE AUTHOR NAME.")
                else:
                    break
            query_books_name(catalog, search_term)
        case 1:
            while True:
                try:
                    book_id = int(
                        input("ENTER THE ID OF THE BOOK YOU WANT TO SEARCH OFR: ")
                    )
                    break
                except ValueError:
                    print("ENTER THE CORRECT ENTRY.")
            query_books_id(catalog, book_id)


# THIS IS FOR SEARCH THE BOOK BY AUTHOR NAME. V.1.1]
def query_books_name(catalog: list[dict], search_term: str):
    for book in catalog:
        if search_term == book["author"]:
            print("=" * 50)
            print(f"       THE SERCH RESULT IS HERE")
            print("=" * 50)
            print(f"""ID          : {book['id_']}
BOOK TITLE  : {book['title']}
AUTHOR NAME : {book['author']}
GENRE       : {book['genre']}
PRICE       : {book['price']}
COPIES      : {book['copies']}""")
            return
    print(f"NO BOOK IS THER {search_term} RELATED TO THIS NAME")


# THIS USE FOR SEARCH THE USER WITH THE HELP OF USER ID  V.1.2]
def query_books_id(catalog: list[dict], search_term: int):
    for book in catalog:
        if search_term == book["id_"]:
            print("=" * 50)
            print(f"       THE SERCH RESULT IS HERE")
            print("=" * 50)
            print(f"""    ID          : {book['id_']}
    BOOK TITLE  : {book['title']}
    AUTHOR NAME : {book['author']}
    GENRE       : {book['genre']}
    PRICE       : {book['price']}
    COPIES      : {book['copies']}""")
            return
    print(f"NO BOOK IS THER {search_term} RELATED TO THIS NAME")


# THIS IS FOR THE UPDAT THE DATA.
def modify_book_details(catalog: list[dict], book_id: int):
    for book in catalog:
        if book_id == book["id_"]:
            title = input(
                f"ENTER THE NAMR OF THE AUTHOR YOU WANT TO CHANGE FOR ({book['title']}) : "
            )
            if not title:
                pass
            else:
                book["title"] = title
                # -------------
            author = input(
                f"ENTER THE NAMR OF THE AUTHOR YOU WANT TO CHANGE FOR ({book['author']}) : "
            )
            if not author:
                pass
            else:
                book["author"] = author
                # -------------
            genre = input(
                f"ENTER THE NAMR OF THE AUTHOR YOU WANT TO CHANGE FOR ({book['genre']}) : "
            )
            if not genre:
                pass
            else:
                book["genre"] = genre
                # -------------
            price = int(
                input(
                    f"ENTER THE NAMR OF THE AUTHOR YOU WANT TO CHANGE FOR ({book['price']}) : "
                )
            )
            if not price:
                pass
            else:
                book["price"] = price
                # -------------
            copies = int(
                input(
                    f"ENTER THE NAMR OF THE AUTHOR YOU WANT TO CHANGE FOR ({book['copies']}) : "
                )
            )
            if not copies:
                pass
            else:
                book["copies"] = copies

            return


# THIS IS FOR DELET THE FILE
def delet_file(catalog: list[dict], book_id: int):
    for book in catalog:
        if book_id == book["id_"]:
            conferm = (
                input("ARE YOU SHOUURE YOU WANT TO DELET THE DATA Y/N: ")
                .strip()
                .upper()
            )
            if conferm == "Y":
                catalog.remove(book)
        return f"BOOK REMOVED SUCESSFULLY."


def sync_catalog_to_file(filepath: str, catalog: list[dict]):
    with open(filepath, "wt") as fs:
        for c in catalog:
            id_, title, author, genre, price, copies = c.values()
            fs.write(f"{id_}|{title}|{author}|{genre}|{price}|{copies}\n")


# THIS IS USE AS A DUMMY DB
catalog = [
    {
        "id_": 1,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Fiction",
        "price": 299.0,
        "copies": 5,
    },
    {
        "id_": 2,
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "Self Help",
        "price": 450.0,
        "copies": 3,
    },
    {
        "id_": 3,
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "genre": "Finance",
        "price": 399.0,
        "copies": 7,
    },
]


def auto_id():
    dummy = len(catalog) + 1
    return dummy


# THIS IS THE MAIN ENTRY POINT
def main():
    while True:
        match menu():
            case 1:
                next_id = auto_id()
                add_book_entry(catalog, next_id)
            case 2:
                render_catalog(catalog)
            case 3:
                serch_option()
            case 4:
                try:
                    book_id = int(input("ENTER THE BOOK ID YOU WANT TO UPDATE FOR"))
                    modify_book_details(catalog, book_id)
                except ValueError:
                    print("INCORRECT CHOICE PLEASE TRY AGAIN.")
            case 5:
                try:
                    book_id = int(input("ENTER THE BOOK ID YOU WANT TO UPDATE FOR"))
                    delet_file(catalog, book_id)
                except ValueError:
                    print("INCORRECT CHOICE PLEASE TRY AGAIN.")
            case 6:
                filepath = input("Enter: ")
                sync_catalog_to_file(filepath, catalog)


if __name__ == "__main__":
    main()


#  "id_": next_id,
#         "title": title_,
#         "author": author_,
#         "genre": genre_,
#         "price": price_,
#         "copies": copies_,
