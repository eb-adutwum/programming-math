"""CLI for algebra operations: factor, simplify, expand expressions."""

import argparse
from algebra.algebra_utils import factor, simplify, expand


def main():
    """
    Main function to handle command line interface for algebra operations.
    :return: None
    """
    parser = argparse.ArgumentParser(
        description="Algebra CLI: factor, simplify, expand expressions."
    )

    parser.add_argument(
        "operation",
        choices=["factor", "simplify", "expand"],
        help="The operation to perform.",
    )
    parser.add_argument(
        "expression", help="The algebraic expression to process (in quotes)."
    )

    args = parser.parse_args()

    result = None
    if args.operation == "factor":
        result = factor(args.expression)
    elif args.operation == "simplify":
        result = simplify(args.expression)
    elif args.operation == "expand":
        result = expand(args.expression)

    print(result)


if __name__ == "__main__":
    main()
