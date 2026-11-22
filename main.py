LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def writeFile(Filename: str, Content: str) -> None:
    with open(Filename, 'w', encoding="UTF-8") as File:
        File.write(Content)
    return None


def askRows() -> str:
    Rows: str = ""
    print("Collecting plain text rows for ciphering.")
    while True:
        Row = input("Insert row(empty stops): ")
        if Row == "":
            break
        Rows += Row + "\n"
    return Rows


def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    Index = Alphabets.index(Character)
    NewIndex = (Index + Shift) % len(Alphabets)
    return Alphabets[NewIndex]


def rot13(Content: str) -> str:
    Ciphered: str = ""
    for Character in Content:
        if Character in LOWER_ALPHABETS:
            Ciphered += shiftCharacter(Character, LOWER_ALPHABETS)
        elif Character in UPPER_ALPHABETS:
            Ciphered += shiftCharacter(Character, UPPER_ALPHABETS)
        else:
            Ciphered += Character
    return Ciphered


def main() -> None:
    print("Program starting.")
    print()
    PlainText = askRows()
    CipheredText = rot13(PlainText)
    print()
    print("#### Ciphered text ####")
    print(CipheredText)
    print("#### Ciphered text ####")
    Filename = input("Insert filename to save: ")
    if Filename == "":
        print("File name not defined.")
        print("Aborting save operation.")
    else:
        writeFile(Filename, CipheredText)
        print("Ciphered text saved!")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
