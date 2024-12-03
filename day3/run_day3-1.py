import re

with open(f"input.txt") as file:
    lines = file.readlines()


def main():
    result = 0

    for line in lines:
        valid_list = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
        for valid in valid_list:
            nums = re.findall(r'\d{1,3}', valid)
            result += int(nums[0]) * int(nums[1])

    print(f"Sum of results: {result}")


if __name__ == "__main__":
    main()