import sys
import string
import argparse
import urllib.error

import quantum_sg


class BooleanOptionalAction(argparse.Action):
    def __init__(self, option_strings, dest, default=None, required=False, help=None):
        _option_strings = []
        for option_string in option_strings:
            _option_strings.append(option_string)
            if option_string.startswith('--'):
                _option_strings.append('--no-' + option_string[2:])
        super().__init__(
            option_strings=_option_strings,
            dest=dest,
            nargs=0,
            default=default,
            required=required,
            help=help,
        )

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, not option_string.startswith('--no-'))

    def format_usage(self):
        return ' | '.join(self.option_strings)


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
        action=BooleanOptionalAction,
        help="include digits in the generated secrets (default is True)",
    )

    parser.add_argument(
        "-wl",
        "--lowercase",
        default=True,
        action=BooleanOptionalAction,
        help="include lowercase characters in the generated secrets (default is True)",
    )

    parser.add_argument(
        "-wu",
        "--uppercase",
        default=True,
        action=BooleanOptionalAction,
        help="include uppercase characters in the generated secrets (default is True)",
    )

    parser.add_argument(
        "-wp",
        "--punctuation",
        default=False,
        action=BooleanOptionalAction,
        help="include punctuation characters in the generated secrets (default is False)",
    )

    args = parser.parse_args()

    if args.length <= 0 or args.length > quantum_sg.MAX_LENGTH:
        parser.error(
            f"length must be a positive integer less than or equal to {quantum_sg.MAX_LENGTH}"
        )

    if args.number <= 0 or args.number > quantum_sg.MAX_NUMBER:
        parser.error(
            f"number must be a positive integer less than or equal to {quantum_sg.MAX_NUMBER}"
        )

    population = ""

    if args.digits:
        population += string.digits

    if args.lowercase:
        population += string.ascii_lowercase

    if args.uppercase:
        population += string.ascii_uppercase

    if args.punctuation:
        population += string.punctuation

    if not population:
        parser.error("at least one character set must be enabled")

    try:
        secrets = quantum_sg.rand(
            population=population,
            number=args.number,
            length=args.length,
        )
    except urllib.error.URLError as error:
        sys.stderr.write(
            f"Failed to fetch quantum data from the ANU QRNG service: {error}\n"
        )
        return 1

    for phrase in secrets:
        sys.stdout.write(phrase + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
