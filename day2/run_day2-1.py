
with open(f"input.txt") as file:
    lines = file.readlines()


def is_decreasing(lst):
    return all(a > b for a, b in zip(lst, lst[1:]))

def is_increasing(lst):
    return all(a < b for a, b in zip(lst, lst[1:]))

def check_differences(lst):
    return all(1 <= abs(a - b) <= 3 for a, b in zip(lst, lst[1:]))


def main():
    safe_count = 0
    for line in lines:
        split_line = list(map(int, line.split()))
        if (is_decreasing(split_line) or is_increasing(split_line)):
            if check_differences(split_line):
                safe_count += 1
    print(f"Count of safe reports: {safe_count}")


if __name__ == "__main__":
    main()
