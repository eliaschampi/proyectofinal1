def listToDict(title: list, row: list) -> dict:
    book = {}
    for count, value in enumerate(title):
        book[f"{value.strip()}"] = f"{row[count].strip()}"
    return book