from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

try:
    user_input = input("Enter your choice of 'red', 'blue' or 'green': ")
    color = Color[user_input.upper()]
    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")
except KeyError:
    print("Invalid choice. Please enter 'red', 'blue', or 'green'.")
