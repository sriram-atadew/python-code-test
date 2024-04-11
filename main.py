def get_subtext_positions(text_to_search, subtext):
    if not isinstance(text_to_search, str) or not isinstance(subtext, str):
        raise TypeError("Both text_to_search and subtext must be strings")

    if not text_to_search or not subtext:
        return "<No Output>"

    positions = []

    # Iterate over the text to find all occurrences of the subtext
    for i in range(len(text_to_search) - len(subtext) + 1):

        if text_to_search[i:i + len(subtext)].casefold() == subtext.casefold():
            positions.append(str(i+1))

    return subtext + " " + ", ".join(positions) if positions else subtext + " <No Output>"


# Sample usage
text_to_search = "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!"
subtexts = ["Peter", "peter", "pick", "pi", "z", "Peterz"]

for subtext in subtexts:
    print(f"{get_subtext_positions(text_to_search, subtext)}")
