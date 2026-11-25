# Python OOP 

## 1. Classes and Objects

### What is a Class?

A **Class** is a blueprint or template used to create objects.

It defines the attributes (data) and methods (behavior) that its objects will have.

### What is an Object?

An **Object** is an instance of a class.

Each object can have its own data, while sharing the structure and behavior defined by the class.

**Example:**

```python
class Student:
    pass

student1 = Student()
student2 = Student()
```

- `Student` is the class.
- `student1` and `student2` are objects.
- Both objects are created from the same class.

---

## 2. Constructor (`__init__`)

The `__init__()` method is a special method that is automatically called when a new object is created.

It is commonly used to initialize an object's attributes.

**Example:**

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Ali", 20)
```

**Explanation:**

- `__init__()` initializes the object's data.
- `name` and `age` are parameters.
- `self.name` and `self.age` are instance attributes.
- `"Ali"` and `20` are passed when creating the object.

**Important:** `__init__()` initializes an object; it does not create the object itself. Object creation is handled by `__new__()`.

## `__new__()` vs `__init__()`

Python uses two special methods during normal object creation:

### `__new__()`

- Responsible for creating a new object.
- Receives `cls` as its first parameter.
- Must return the newly created object.
- Called before `__init__()`.

### `__init__()`

- Responsible for initializing an already-created object.
- Receives `self` as its first parameter.
- Used to initialize instance attributes.
- Returns `None`.
- Called after `__new__()` when a new instance is created normally.

### Comparison

| `__new__()` | `__init__()` |
|---|---|
| Creates the object | Initializes the object |
| Receives `cls` | Receives `self` |
| Returns an object | Returns `None` |
| Called first | Called second |

### Object Creation Process

1. Python calls `__new__()` to create the object.
2. `__new__()` returns the new object.
3. Python calls `__init__()` to initialize it.
4. The object is ready to use.

**Example:**

```python
class Student:
    def __new__(cls, name):
        print("Creating object...")
        return super().__new__(cls)

    def __init__(self, name):
        print("Initializing object...")
        self.name = name
```

**Important:**

- We usually override `__init__()`, not `__new__()`.
- Most classes do not need a custom `__new__()` method.
- `__new__()` is mainly used in advanced object creation scenarios.
---

## 3. The `self` Parameter

`self` refers to the current object (the instance on which a method is called).

It allows instance methods to access and modify that object's attributes and call its other methods.

**Example:**

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(self.name)

student1 = Student("Ali")
student1.display_info()
```

When we write:

```python
student1.display_info()
```

Python automatically passes `student1` as the first argument (`self`).

This is conceptually similar to:

```python
Student.display_info(student1)
```

**Remember:**

- `self` is not a Python keyword, but it is the standard naming convention.
- It represents the current instance.
- Each object has its own instance attributes.

---

## 4. Attributes and Methods

### Attributes

Attributes are variables that store data associated with a class or an object.

### Methods

Methods are functions defined inside a class. They represent the behavior of objects or the class itself.

| Attributes             | Methods                   |
| ---------------------- | ------------------------- |
| Store data             | Perform actions           |
| Represent properties   | Represent behavior        |
| Example: `name`, `age` | Example: `display_info()` |

**Example:**

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")
```

- `name` and `age` are attributes.
- `introduce()` is a method.

---

## 5. Instance Attributes vs Class Attributes

### Instance Attributes

Instance attributes belong to a specific object.

- Usually defined inside `__init__()` using `self`.
- Each object can have different values.
- Changing one object's instance attribute does not directly change another object's attribute.

### Class Attributes

Class attributes belong to the class itself.

- Defined directly inside the class, outside methods.
- Shared by instances by default.
- Commonly used for values shared by all objects.

**Example:**

```python
class Student:
    university = "KFSU"  # Class Attribute

    def __init__(self, name):
        self.name = name  # Instance Attribute
```

```python
student1 = Student("Ali")
student2 = Student("Sara")
```

Both students share the same class attribute:

```python
print(student1.university)  # KFSU
print(student2.university)  # KFSU
```

### Modifying Class Attributes

```python
Student.university = "Cairo University"
```

This changes the class attribute, so instances without an overriding instance attribute will see the new value.

### Overriding a Class Attribute on an Instance

```python
student1.university = "Alexandria University"
```

This creates an instance attribute named `university` on `student1`.

It does not change the class attribute or affect `student2`.

### Comparison

| Instance Attribute           | Class Attribute                 |
| ---------------------------- | ------------------------------- |
| Belongs to an object         | Belongs to the class            |
| Usually uses `self`          | Defined directly in the class   |
| Can differ between objects   | Shared by default               |
| Accessed through an instance | Best accessed through the class |

**Important:** Be careful with mutable class attributes such as lists and dictionaries. All instances can share the same mutable object. Use instance attributes when each object needs its own separate collection.

---

## 6. Encapsulation

**Encapsulation** means organizing data and the methods that work with that data inside a class, while controlling how the data is accessed or modified.

It helps protect an object's data from invalid or unintended changes.

**Example:**

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
```

Instead of allowing unrestricted changes to the balance, we provide a method that checks the amount before updating it.

```python
account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())  # 1500
```

**Benefits of Encapsulation:**

- Protects data from invalid modifications.
- Controls access to internal data.
- Makes code easier to maintain.
- Keeps data and related behavior together.

### Properties (`@property`)

Python provides the `@property` decorator to control attribute access using method logic.

It allows a method to be accessed like an attribute.

```python
class Student:
    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" in value:
            self.__email = value
        else:
            raise ValueError("Invalid email")
```

**Usage:**

```python
student = Student("ali@gmail.com")

print(student.email)  # Reading

student.email = "new@gmail.com"  # Updating
```

- `@property` defines a getter.
- `@email.setter` defines a setter.
- Validation can be performed before changing the internal value.

---

## 7. Public, Protected, and Private Conventions

Python uses naming conventions to communicate the intended level of access to attributes and methods.

| Convention | Syntax   | Meaning                                               |
| ---------- | -------- | ----------------------------------------------------- |
| Public     | `name`   | Intended to be accessible from anywhere               |
| Protected  | `_name`  | Intended for internal use and subclasses              |
| Private    | `__name` | Uses name mangling to avoid accidental name conflicts |

### Public

Public attributes can be accessed and modified normally.

```python
self.name = "Ali"
```

```python
student.name = "Sara"
```

### Protected (`_attribute`)

A single leading underscore indicates that an attribute is intended for internal use.

It is still accessible from outside the class, but users of the class are expected to treat it as non-public.

```python
self._username = "ali123"
```

### Private (`__attribute`)

A double leading underscore triggers **Name Mangling**.

Python changes the attribute's internal name to include the class name.

```python
class Student:
    def __init__(self):
        self.__email = "ali@gmail.com"
```

Python internally stores this attribute under a name similar to:

```python
_Student__email
```

This helps avoid accidental access and naming conflicts, especially in inheritance.

**Important:**

- Python does not provide strict private access control like some other languages.
- Name mangling does not make an attribute completely inaccessible.
- Avoid accessing mangled attributes directly; use methods or properties instead.

---

## 8. Inheritance

**Inheritance** allows a class (Child Class) to inherit attributes and methods from another class (Parent Class).

It promotes code reuse and reduces code duplication.

**Syntax:**

```python
class ChildClass(ParentClass):
    pass
```

**Example:**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Eating...")


class Dog(Animal):
    def bark(self):
        print("Woof!")
```

```python
dog = Dog("Max")

dog.eat()
dog.bark()
```

- `Animal` is the Parent Class (Base Class).
- `Dog` is the Child Class (Derived Class).
- `Dog` inherits the `eat()` method and can define its own methods.

**Benefits:**

- Code reusability.
- Better organization.
- Easier extension of existing classes.

---

## 9. The `super()` Function

`super()` returns a proxy object that provides access to methods through the next class in the **Method Resolution Order (MRO)**.

It is commonly used in inheritance to reuse a parent class's implementation.

### Calling the Parent Constructor

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

`super().__init__(name)` calls the next `__init__()` implementation in the MRO.

This allows the child class to reuse the parent's initialization logic.

### Calling Another Inherited Method

```python
class Dog(Animal):
    def display_info(self):
        super().display_info()
        print(self.breed)
```

This calls the inherited implementation before adding the child's own information.

**Important:**

- `super()` is not simply an alias for the parent class.
- It follows the MRO.
- It is especially important in multiple inheritance.
- `super()` itself does not call a method; you specify the method after it, such as `super().__init__()`.

---

## 10. Method Overriding

**Method Overriding** occurs when a child class provides its own implementation of a method already defined in the parent class.

The child class version is used when the method is called on an instance of that child class.

**Example:**

```python
class Animal:
    def make_sound(self):
        print("Some sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")
```

```python
dog = Dog()
dog.make_sound()  # Woof!
```

The `Dog` class overrides the `make_sound()` method inherited from `Animal`.

**Why use overriding?**

To customize or extend inherited behavior for a specific child class.

---

## 11. Polymorphism

**Polymorphism** means "Many Forms".

It allows objects of different classes to respond differently to the same method call.

It commonly works with method overriding.

**Example:**

```python
class Dog:
    def make_sound(self):
        print("Woof!")


class Cat:
    def make_sound(self):
        print("Meow!")


animals = [Dog(), Cat()]

for animal in animals:
    animal.make_sound()
```

**Output:**

```text
Woof!
Meow!
```

The same method call:

```python
animal.make_sound()
```

produces different behavior depending on the object's type.

**Key Idea:** We focus on what an object can do rather than requiring all objects to belong to the same class.

Python also supports duck typing: if an object provides the required behavior, it can often be used without sharing a common parent class.

---

## 12. Instance, Class, and Static Methods

Python supports three common types of methods.

### A. Instance Methods

- Work with a specific object.
- Receive `self` as the first parameter.
- Can access and modify instance attributes.
- Can also access class attributes.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)
```

Usage:

```python
student = Student("Ali")
student.display_name()
```

### B. Class Methods

- Work with the class itself.
- Use the `@classmethod` decorator.
- Receive `cls` as the first parameter.
- Commonly access or modify class attributes.

```python
class Student:
    university = "KFSU"

    @classmethod
    def change_university(cls, new_name):
        cls.university = new_name
```

Usage:

```python
Student.change_university("Cairo University")
```

`cls` refers to the class, not a particular object.

### C. Static Methods

- Use the `@staticmethod` decorator.
- Do not receive `self` or `cls` automatically.
- Do not need instance or class data.
- Usually contain utility logic related to the class.

```python
class Student:
    @staticmethod
    def is_valid_age(age):
        return 16 <= age <= 100
```

Usage:

```python
print(Student.is_valid_age(20))  # True
```

### Comparison Table

| Feature              | Instance Method | Class Method     | Static Method               |
| -------------------- | --------------- | ---------------- | --------------------------- |
| Decorator            | None            | `@classmethod`   | `@staticmethod`             |
| First parameter      | `self`          | `cls`            | None                        |
| Works with           | Object          | Class            | Neither automatically       |
| Access instance data | Yes             | No, not directly | No, not directly            |
| Access class data    | Yes             | Yes              | Only if accessed explicitly |

### How to Choose?

- Use an **Instance Method** when the operation depends on an object's data.
- Use a **Class Method** when the operation depends on class-level data or creates objects in an alternative way.
- Use a **Static Method** for a utility operation logically related to the class but independent of its data.

---

## 13. Type Hints for Variables

Type Hints indicate the expected data type of a variable.

They improve code readability, editor assistance, and static type checking.

**Example:**

```python
name: str = "Ali"
age: int = 20
gpa: float = 3.8
is_active: bool = True
```

Common types:

| Type Hint | Expected Value |
| --------- | -------------- |
| `str`     | Text           |
| `int`     | Integer        |
| `float`   | Decimal number |
| `bool`    | True or False  |

**Important:** Type hints are not automatically enforced at runtime by Python. They are mainly used by developers, editors, and static type checkers.

---

## 14. Type Hints for Functions

Type hints can specify the expected types of function parameters and the return type.

**Syntax:**

```python
def function_name(parameter: type) -> return_type:
    ...
```

**Example:**

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

- `price: float` indicates that price is expected to be a float.
- `quantity: int` indicates that quantity is expected to be an integer.
- `-> float` indicates the expected return type.

### Functions That Return Nothing

Use `None` as the return type when a function does not return a meaningful value.

```python
def display_message(message: str) -> None:
    print(message)
```

**Remember:**

- `:` specifies a parameter's type.
- `->` specifies the function's return type.

---

## 15. Type Hints with Lists and Dictionaries

Python allows us to specify the types of items stored inside collections.

### Lists

Use `list[Type]` to specify the type of elements in a list.

```python
names: list[str] = ["Ali", "Sara", "Omar"]

scores: list[int] = [90, 85, 95]
```

Examples:

| Type Hint     | Meaning          |
| ------------- | ---------------- |
| `list[str]`   | List of strings  |
| `list[int]`   | List of integers |
| `list[float]` | List of floats   |
| `list[bool]`  | List of booleans |

### Dictionaries

Use `dict[KeyType, ValueType]`.

```python
student: dict[str, int] = {
    "Ali": 20,
    "Sara": 21
}
```

- `str` is the key type.
- `int` is the value type.

More examples:

```python
prices: dict[str, float] = {
    "Book": 100.5,
    "Pen": 15.0
}

grades: dict[int, str] = {
    1: "Excellent",
    2: "Good"
}
```

### Nested Collections

Type hints can describe nested data structures.

```python
students: list[dict[str, int]] = [
    {"age": 20},
    {"age": 21}
]
```

This means a list containing dictionaries with string keys and integer values.

### Multiple Possible Types

Use `|` to allow more than one type.

```python
values: list[int | float] = [10, 2.5, 30]
```

Each list element can be either an integer or a float.

---

## 16. Optional Values (`str | None`)

Sometimes a variable may contain a value or may have no value.

In Python, `None` represents the absence of a value.

**Example:**

```python
bio: str | None = None
```

This means `bio` can contain:

- A string, such as `"AI Student"`.
- `None`, meaning no bio is available.

### Optional Function Parameters

```python
def create_student(name: str, bio: str | None = None) -> None:
    print(name)
    print(bio)
```

The `bio` parameter is optional because it has a default value of `None`.

```python
create_student("Ali")
create_student("Sara", "AI Student")
```

### `str | None` vs `str = None`

These are different concepts:

```python
bio: str | None
```

This describes the allowed types: string or None.

```python
bio: str | None = None
```

This describes the allowed types and assigns a default value.

### The Older `Optional` Syntax

```python
from typing import Optional

bio: Optional[str] = None
```

`Optional[str]` means the same as `str | None`.

**Important:** A type hint does not make a function parameter optional by itself. A default value, such as `= None`, makes it optional to omit when calling the function.

---

## 17. Type Hints with Classes

A class name can be used as a type hint.

This is useful when a function or method expects an object created from a specific class.

**Example:**

```python
class Student:
    def __init__(self, name: str):
        self.name = name


def display_student(student: Student) -> None:
    print(student.name)
```

Here:

```python
student: Student
```

means the variable is expected to refer to a `Student` object.

### A Method That Receives Another Class Object

```python
class Course:
    def __init__(self, title: str):
        self.title = title

    def enroll_student(self, student: Student) -> None:
        print(f"{student.name} enrolled in {self.title}")
```

The `enroll_student()` method expects a `Student` object, not just a student's name.

### A Method That Returns a Class Object

```python
def create_student(name: str) -> Student:
    return Student(name)
```

The return type indicates that the function returns a `Student` object.

### A List of Class Objects

```python
students: list[Student] = [
    Student("Ali"),
    Student("Sara")
]
```

This means the list is expected to contain `Student` objects.

### Optional Class Objects

```python
def find_student(student_id: int) -> Student | None:
    ...
```

This means the function may return:

- A `Student` object if found.
- `None` if no student is found.

**Key Idea:** Type hints with classes help describe how different classes interact with each other.

---

# 18. Quick Revision – Important Differences

| Concept                  | Main Idea                                      |
| ------------------------ | ---------------------------------------------- |
| Class                    | Blueprint for creating objects                 |
| Object                   | An instance of a class                         |
| Constructor              | Initializes an object                          |
| `self`                   | Refers to the current instance                 |
| Instance Attribute       | Belongs to one object                          |
| Class Attribute          | Shared by instances by default                 |
| Encapsulation            | Organizes data and controls access to it       |
| Public                   | Normal public naming                           |
| Protected                | Single underscore `_` convention               |
| Private                  | Double underscore `__` with name mangling      |
| Inheritance              | Reusing and extending another class            |
| `super()`                | Accesses the next implementation in the MRO    |
| Overriding               | Replacing inherited method behavior            |
| Polymorphism             | Same interface, different behavior             |
| Instance Method          | Uses `self`                                    |
| Class Method             | Uses `cls`                                     |
| Static Method            | Uses neither automatically                     |
| `list[str]`              | List of strings                                |
| `dict[str, int]`         | Dictionary with string keys and integer values |
| `str \| None`            | String or None                                 |
| `Student` as a Type Hint | Expected Student object                        |

---

# 19. Common Mistakes to Avoid

### 1. Forgetting `self`

Incorrect:

```python
def display_info():
    print(self.name)
```

Correct:

```python
def display_info(self):
    print(self.name)
```

### 2. Confusing Instance and Class Attributes

```python
self.count += 1
```

This modifies an instance attribute (or creates one if it does not exist).

```python
Student.count += 1
```

This modifies the class attribute.

### 3. Forgetting `@classmethod`

Incorrect:

```python
def change_name(cls, name):
    cls.name = name
```

Correct:

```python
@classmethod
def change_name(cls, name):
    cls.name = name
```

### 4. Using `self` in a Static Method

A static method does not receive `self` automatically.

### 5. Confusing Optional Types with Default Values

`str | None` describes allowed types.

`value=None` provides a default value.

### 6. Thinking Type Hints Enforce Types

Python does not automatically reject values that do not match type hints at runtime.

---

# 20. Final OOP Checklist

Before considering your Python OOP fundamentals complete, make sure you can:

- [ ] Create classes and objects.
- [ ] Use constructors and `self`.
- [ ] Define attributes and methods.
- [ ] Distinguish instance attributes from class attributes.
- [ ] Apply encapsulation using properties.
- [ ] Understand public, protected, and private naming conventions.
- [ ] Use inheritance and `super()`.
- [ ] Override inherited methods.
- [ ] Understand polymorphism.
- [ ] Choose between instance, class, and static methods.
- [ ] Write type hints for variables and functions.
- [ ] Write type hints for lists and dictionaries.
- [ ] Use optional types such as `str | None`.
- [ ] Use class names as type hints.
- [ ] Make different classes work together in one project.

**Final Reminder:** The goal of OOP is not just to know the syntax. It is to organize code into reusable, understandable, and maintainable classes that work together.
