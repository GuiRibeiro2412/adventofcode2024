
with open(f"input.txt") as file:
    lines = file.readlines()



def is_safe(split_line) -> bool:
    if split_line == sorted(split_line, reverse=True) or split_line == sorted(split_line):
        if all(1 <= abs(a - b) <= 3 for a, b in zip(split_line, split_line[1:])):
            return True
    return False


def main():
    safe_count = 0
    for line in lines:
        split_line = list(map(int, line.split()))
        if is_safe(split_line):
            safe_count += 1
    print(f"Count of safe reports: {safe_count}")


if __name__ == "__main__":
    main()
