import argparse

def main():
    parser = argparse.ArgumentParser(description="A script with flag-based options.", add_help=False)
    parser.add_argument('-h', '--help', action='store_true', help="Show help information.")
    parser.add_argument('-e', '--example', action='store_true', help="An example flag for future use.")

    args = parser.parse_args()

    if args.help:
        print("Usage:")
        print("  -h, --help    : Show this help message.")
        print("  -e, --example : An example flag for future implementation.")
        return

    if args.example:
        print("Example flag activated!")

if __name__ == "__main__":
    main()
