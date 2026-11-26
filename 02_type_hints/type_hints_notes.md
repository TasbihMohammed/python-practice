# Type Hints in Python

## 1. What are Type Hints?

Type Hints are optional annotations that specify the expected data types of variables, function parameters, and return values.

They make code more readable, understandable, and easier to maintain.

**Important:**
- Type Hints do not enforce types at runtime.
- Python does not prevent passing values of unexpected types just because type hints are present.
- They help developers and tools detect potential type-related errors.

## 2. Variable Annotations

We can specify the expected type of a variable using a type annotation.

```python
name: str = "Alice"
age: int = 20
height: float = 1.65
is_student: bool = True
```

## 3. Function Parameters and Return Types

We can specify the expected type of each parameter and the return type of a function.

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

- `price: float` specifies the expected type of the first parameter.
- `quantity: int` specifies the expected type of the second parameter.
- `-> float` specifies the expected return type.

## 4. Common Built-in Types

| Type | Example |
|---|---|
| `int` | `age: int = 20` |
| `float` | `price: float = 15.5` |
| `str` | `name: str = "Ali"` |
| `bool` | `is_active: bool = True` |
| `list` | `numbers: list[int] = [1, 2, 3]` |
| `tuple` | `point: tuple[int, int] = (10, 20)` |
| `dict` | `scores: dict[str, int] = {"Ali": 90}` |
| `set` | `ids: set[int] = {1, 2, 3}` |

## 5. Type Hints with Collections

We can specify the type of elements inside a collection.

```python
names: list[str] = ["Ali", "Sara"]

scores: dict[str, int] = {
    "Ali": 90,
    "Sara": 85
}

def calculate_average(scores: list[float]) -> float:
    return sum(scores) / len(scores)
```

## 6. Optional Values

Sometimes a variable or parameter can contain a value of a specific type or `None`.

We can use the `|` operator (Python 3.10+) to represent multiple possible types.

```python
def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Alice"

    return None
```

Here, the function can return either a `str` or `None`.

## 7. Type Hints with Classes

We can also use class names as type hints.

```python
class Student:
    def __init__(self, name: str):
        self.name = name

def display_student(student: Student) -> None:
    print(student.name)
```

`Student` indicates that the function expects an object created from the `Student` class.

`None` indicates that the function does not return a value.

## Key Takeaways

- Type Hints improve code readability and maintainability.
- They are optional and are not enforced by Python at runtime.
- We can annotate variables, parameters, and return values.
- We can specify collection element types.
- We can use `|` to indicate multiple possible types.
- Class names can be used as type hints.