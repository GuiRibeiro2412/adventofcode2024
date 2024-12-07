
with open(f"input.txt") as file:
    text = [[char for char in line.strip()] for line in file]

X = [[(-1,-1), (1,1)], [(-1,1), (1,-1)]]
ROWS = len(text)
COLS = len(text[0])
word = 'MAS'


def is_valid(row, col):
    return 0 <=row < ROWS and 0 <= col < COLS


def search_word(row, col, line) -> bool:
    if text[row][col] != word[1]:
        return False
    
    previous_row = row + line[0][0]
    previous_col = col + line[0][1]
    next_row = row + line[1][0]
    next_col = col + line[1][1]

    for r,c in [(previous_row, previous_col), (next_row, next_col)]:
        if not is_valid(r, c):
            return False
        
    if text[previous_row][previous_col] + text[row][col] + text[next_row][next_col] not in ["MAS", "SAM"]:
        return False

    return True


def main():
    word_count = 0

    for row in range(ROWS):
        for col in range(COLS):
            found = 0
            for line in X:
                if search_word(row, col, line):
                    found += 1
                if found == len(X):
                    word_count += 1


    print(f"Word count: {word_count}")


if __name__ == "__main__":
    main()