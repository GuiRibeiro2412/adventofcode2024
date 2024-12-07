
with open(f"input.txt") as file:
    text = [[char for char in line.strip()] for line in file]

directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
ROWS = len(text)
COLS = len(text[0])
word = 'XMAS'


def is_valid(row, col):
    return 0 <=row < ROWS and 0 <= col < COLS


def search_word(row, col, direction) -> bool:
    if text[row][col] != word[0]:
        return False
    
    for i in range(1, len(word)):
        next_row = row + direction[0] * i
        next_col = col + direction[1] * i

        if not is_valid(next_row, next_col):
            return False
        
        if text[next_row][next_col] != word[i]:
            return False
    
    return True


def main():
    word_count = 0

    for row in range(ROWS):
        for col in range(COLS):
            for direction in directions:
                if search_word(row, col, direction):
                    word_count += 1


    print(f"Word count: {word_count}")


if __name__ == "__main__":
    main()