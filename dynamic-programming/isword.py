def isWordPresent(letters, words):
    # empty list for storing whether the words in words-list exists in letters or not
    presents = []

    # generating list of words by concatenating all letters in each row
    rwords = ["".join(row) for row in letters]

    # empty list for storing words by concatenating all letters in each column
    cwords = []

    # iterating through columns of grid by indexing
    for col in range(len(letters[0])):
        # empty string for storing word in the column
        cword = ""
        # iterating through rows of grid by indexing
        for row in range(len(letters)):
            # adding each letter to gword
            cword += letters[row][col]

        # adding gword to cwords
        cwords.append(cword)

    # iterating through words list
    for word in words:
        # iterating through words in the rwords and cwords
        for gword in rwords + cwords:
            # if word exists in gword or reverse of gword, adding "Yes" to presents list
            if word in (gword, gword[::-1]): 
                presents.append("Yes")
                break

        # otherwise, adding "No" to presents list
        else:
            presents.append("No")

    return presents


def main():
    letters = []
    letters_rows, letters_col = map(int, input().split())
    for idx in range(letters_rows):
        letters.append(list(map(str, input().split())))

    words = []
    words_size = int(input())
    words = list(map(str, input().split()))

    result = isWordPresent(letters, words)
    print(" ".join([str(res) for res in result]))


if __name__ == "__main__":
    main()