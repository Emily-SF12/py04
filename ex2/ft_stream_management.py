import sys
from typing import IO


def creat_new_file(new_content: str) -> None:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    target: str = sys.stdin.readline().strip()
    if target == "":
        print("Data not saved.")
        return
    print(f"saving data to '{target}'")
    try:
        out: IO[str] = open(target, "w")
    except OSError as e:
        print(f"Error opening file '{target}': {e}")
        print("Data not saved")
        return
    out.write(new_content)
    out.close()
    print(f"File '{target}' closed. Data saved.")


def content_transform(old_content: str) -> str:
    lines: list[str] = old_content.split("\n")
    new_content: str = ""
    for line in lines:
        if line != "":
            new_content = new_content + line + "#\n"
    print("\nTransform data:")
    print("---\n")
    print(new_content)
    print("---")
    return new_content


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
        sys.stderr.write(f"[STERR] Error opening file: '{filename}': {e}\n")
        return
    content: str = handle.read()
    print("---\n")
    print(content)
    print("\n---")
    handle.close()
    print(f"File '{filename}' closed.")
    creat_new_file(content_transform(content))


if __name__ == "__main__":
    main()
