import search

rack = ""
patt = "hi?e"

matches = search.search(rack, patt)

if not matches:
    print("None found")
else:
    for match in matches:
        print(match)
