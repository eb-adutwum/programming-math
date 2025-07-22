"""CLI entry point for calculus operations"""

import argparse
import sys
from calculus import lim


def main():
    """
    Main function to handle command line interface for calculus operations.
    :return: None
    """
    parser = argparse.ArgumentParser(description="Calculus CLI: lim")

    parser.add_argument(
        "operation", choices=["lim"], help="calculus operation to perform"
    )

    parser.add_argument("expression", help="expression to be evaluated")

    args = parser.parse_args()

    result = None
    # Check the operation and call the appropriate function
    # and parse the expression based on the requirement
    if args.operation == "lim":
        expression, point, side = _parse_lim(args.expression)
        if expression:
            result = lim(expression, point, side=side)
        else:
            raise ArithmeticError(
                "Required: '<statement>,<value>,*<direction(+/-)>', *=optional"
            )

    print(result)


def _parse_lim(exp: str) -> list:
    """
    This function uses a string to parse the limit expression. It does this by
    splitting the string by commas. The first part is the expression, the second
    part is the value to which the limit is being taken, and the third part is
    the direction of the limit (optional, defaults to "+").
    :param exp: The limit expression as a string.
    :return: A list containing the expression, the value, and the direction.
    """
    arguments = exp.split(",")

    if len(arguments) < 2:
        raise ArithmeticError(
            "Required: '<statement>,<value>,*<direction(+/-)>', *=optional"
        )

    if _is_float(arguments[1]) or arguments[1] == "inf" or arguments[1] == "-inf":
        arguments[1] = float(arguments[1])

        if len(arguments) == 3:
            return arguments
        if len(arguments) == 2:
            return arguments + ["+"]
        raise ArithmeticError(
            "Required: '<statement>,<value>,*<direction(+/-)>', *=optional"
        )

    return [None, None, None]


def _is_float(s: str) -> bool:
    """
    Check if a string can be converted to a float.
    :param s: The string to check.
    :return: True if the string can be converted to a float, False otherwise.
    """
    return s.replace(".", "").isnumeric()


if __name__ == "__main__":
    # show usage if no arguments are provided
    if len(__import__("sys").argv) == 1:
        print("Usage: python -m calculus <operation> <expression>")
        print("Example: python -m calculus lim 'x**2 + 2*x + 1,1'")
        print(
            "Available operations: lim, "
            "expressions should be in quotes and arguments separated by commas"
        )
        sys.exit(1)
    main()
