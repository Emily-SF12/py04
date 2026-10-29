def secure_archive(name: str, action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "write":
            with open(name, "w") as handle:
                handle.write(content)
            return (True, "Content sucessfully written to file")
        with open(name) as handle:
            return (True, handle.read())
    except OSError as e:
        return (False, f"{e}")


"""
def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    ok, texto = secure_archive("ancient_fragment.txt")
    print((ok, texto))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("copia.txt", "write", texto))


if __name__ == "__main__":
    main()
"""
