
with open(f"input.txt") as file:
    lines = file.readlines()


def is_safe(lst) -> bool:
    


def main():
    safe_count = 0
    for line in lines:
        split_line = list(map(int, line.split()))
        if split_line != sorted(split_line) or split_line != sorted(split_line, reverse=True)
        
        for a, b in zip(split_line, split_line[1:]):
            if not(a > b)
        
        if (is_decreasing(split_line) or is_increasing(split_line)):
            for a, b in zip(split_line, split_line[1:]):
                if  not(1 <= abs (a - b) <= 3):
                    tolerate += 1
            if tolerate < 2 and is_safe:
                safe_count += 1
    print(f"Count of safe reports: {safe_count}")


if __name__ == "__main__":
    main()
