import sys
import string
import argparse
import quantum_sg

BLOCK_SIZE = 128
MAX_LENGTH = 1024


def main():
    parser = argparse.ArgumentParser(
        description="A command line tool that generates a cryptographically "
                    "secure quantum-level secrets using ANU QRNG."
    )

    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1,
        help="The number of secrets to be generated (default is 1)",
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=24,
        help="the length of each generated secret (default is 24)",
    )

    parser.add_argument(
        "-wd",
        "--digits",
        default=True,
        action=argparse.BooleanOptionalAction,
        help="include digits in the generated secrets (default is True)",
    )

    parser.add_argument(
        "-wl",
        "--lowercase",
        default=True,
        action=argparse.BooleanOptionalAction,
        help="include lowercase characters in the generated secrets (default is True)",
    )

    parser.add_argument(
        "-wu",
        "--uppercase",
        default=True,
        action=argparse.BooleanOptionalAction,
        help="include uppercase characters in the generated secrets (default is True)",
    )

    parser.add_argument(
        "-wp",
        "--punctuation",
        default=False,
        action=argparse.BooleanOptionalAction,
        help="include punctuation characters in the generated secrets (default is False)",
    )

    args = parser.parse_args()
    if args.length > MAX_LENGTH or args.length <= 0:
        sys.stdout.write(f'Length must be a non-negative integer and less than or equal to {MAX_LENGTH} \n')
        return

    population = ""

    if args.digits:
        population += string.digits

    if args.lowercase:
        population += string.ascii_lowercase

    if args.uppercase:
        population += string.ascii_uppercase

    if args.punctuation:
        population += string.punctuation

    for phrase in quantum_sg.rand(population=population, number=args.number, length=args.length):
        sys.stdout.write(phrase + "\n")


if __name__ == "__main__":
    main()
