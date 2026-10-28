import sys
from typing import IO


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        handle: IO[str] = open(filename)
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return
    content: str = handle.read()
    print("---\n")
    print(content)
    print("\n---")
    handle.close()
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
