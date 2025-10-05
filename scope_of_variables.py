#!/usr/bin/env python3
# Created by: Shem
# Created on: 10/4/2025

# Global variable
VARIABLE_x = 25


def local_variable() -> None:
    """The local_variable() function creates local variables, return to None."""
    VARIABLE_x = 15
    VARIABLE_y = 17

    VARIABLE_x = VARIABLE_x + 1
    VARIABLE_z = VARIABLE_x + VARIABLE_y

    print(f"Local variable: {VARIABLE_x} + {VARIABLE_y} = {VARIABLE_z}")


def global_variable() -> None:
    """The global_variable() function uses the global variable."""
    global VARIABLE_x  # Correct way to refer to global variable
    VARIABLE_y = 17

    VARIABLE_x = VARIABLE_x + 1
    VARIABLE_z = VARIABLE_x + VARIABLE_y

    print(f"Global variable: {VARIABLE_x} + {VARIABLE_y} = {VARIABLE_z}")


def main() -> None:
    """The main() function runs the variable functions."""
    local_variable()
    global_variable()
    print("\nDone.")


if __name__ == "__main__":
    main()
