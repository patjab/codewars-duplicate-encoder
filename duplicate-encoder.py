def duplicate_encode(word):
    letter_count = {}
    for c in word.lower():
        letter_count[c] = letter_count[c]+1 if c in letter_count else 1

    encoded_arr = map(lambda x: "(" if letter_count[x] == 1 else ")" , word.lower())
    return ''.join(str(x) for x in encoded_arr)
