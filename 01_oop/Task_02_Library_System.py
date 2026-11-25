
class LibraryItem:
    def __init__(self, title: str, item_id: int) -> None:
        self.title = title
        self.item_id = item_id

    def display_info(self) -> None:
        print(f"Title: {self.title}")
        print(f"Item ID: {self.item_id}")

    def get_item_type(self) -> str:
        return "Unknown"


class Book(LibraryItem):
    def __init__(self, title: str, item_id: int, author: str) -> None:
        super().__init__(title, item_id)
        self.author = author

    def display_info(self) -> None:
        super().display_info()
        print(f"Author: {self.author}")

    def get_item_type(self) -> str:
        return "Book"


class Magazine(LibraryItem):
    def __init__(self, title: str, item_id: int,
                 issue_number: int) -> None:
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def display_info(self) -> None:
        super().display_info()
        print(f"Issue Number: {self.issue_number}")

    def get_item_type(self) -> str:
        return "Magazine"


# Creating Objects
book1 = Book("Python Programming", 101, "John Smith")
magazine1 = Magazine("Science Today", 201, 15)


# Testing Inherited Methods
print("=" * 50)
print("INHERITANCE TEST")
print("=" * 50)

print("\nBook Information:")
book1.display_info()

print("\nMagazine Information:")
magazine1.display_info()


# Testing Method Overriding
print("\n" + "=" * 50)
print("METHOD OVERRIDING TEST")
print("=" * 50)

print(f"Book Type: {book1.get_item_type()}")
print(f"Magazine Type: {magazine1.get_item_type()}")


# Testing Polymorphism
print("\n" + "=" * 50)
print("POLYMORPHISM TEST")
print("=" * 50)

library_items: list[LibraryItem] = [book1, magazine1]

for item in library_items:
    print(f"{item.title}: {item.get_item_type()}")


# Testing Base Class
print("\n" + "=" * 50)
print("BASE CLASS TEST")
print("=" * 50)

item1 = LibraryItem("General Item", 301)

item1.display_info()
print(f"Item Type: {item1.get_item_type()}")
