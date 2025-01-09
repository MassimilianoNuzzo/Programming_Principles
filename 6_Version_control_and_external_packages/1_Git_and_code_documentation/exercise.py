"""Define Person class."""


class Person:
    """A class representing a person with a name, age, and address.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        address (str): The address of the person.

    """

    def __init__(self, name: str, age: int) -> None:
        """Initialize a new Person object with a name and age.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.

        """
        self.name = name
        self.age = age
        self._address = ""

    def set_address(self, address: str) -> None:
        """Set the address of the person.

        Args:
            address (str): The address to be set.

        """
        self._address = address

    def get_address(self) -> str:
        """Retrieve the address of the person.

        Returns:
            str: The address of the person.

        """
        return self._address

    def greet(self) -> str:
        """Return a greeting message with the person's name and age."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def set_age(self, new_age: int) -> None:
        """Set a new age for the person, ensuring it is positive.

        Args:
            new_age (int): The new age to set.

        Raises:
            ValueError: If the new age is less than or equal to zero.

        """
        if new_age > 0:
            self.age = new_age
        else:
            message = "Age cannot be negative or zero."
            raise ValueError(message)

    def calculate_years_until_100(self) -> int:
        """Calculate how many years are left until the person turns 100.

        Returns:
            int: The number of years remaining until the person turns 100.

        """
        return 100 - self.age
