import argparse
from datetime import datetime
from pathlib import Path


def build_output_lines():
    return [
        "Hello Github",
        datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
    ]


def print_hello():
    output_lines = build_output_lines()

    for line in output_lines:
        print(line)

    return output_lines


def write_output_file(output_lines):
    output_path = Path(__file__).resolve().parent / "output.txt"
    output_path.write_text("\n".join(output_lines) + "\n", encoding="utf-8")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Gibt 'Hello Github' und das aktuelle Datum mit Uhrzeit aus.",
        epilog="Beispiel: python hello.py -o true",
    )
    parser.add_argument(
        "-o",
        "--output",
        choices=["true", "false"],
        default="false",
        help="Schreibt die Ausgabe zusaetzlich in output.txt. Standard: false",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    output_lines = print_hello()

    if args.output == "true":
        write_output_file(output_lines)


if __name__ == "__main__":
    main()
