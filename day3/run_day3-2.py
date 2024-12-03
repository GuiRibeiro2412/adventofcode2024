import re

with open(f"input.txt") as file:
    text = file.read().replace("\n", "")


def main():
    result = 0

    pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'

    instructions = re.findall(pattern, text)
    
    ignore = False
    for instruction in instructions:
        if instruction == "do()":
            ignore = False
        elif instruction == "don't()":
            ignore = True
        elif not ignore:
            nums = re.findall(r'\d{1,3}', instruction)
            print(f"{nums[0]} times {nums[1]}")
            result += int(nums[0])* int(nums[1])

    print(f"Sum of results: {result}")


if __name__ == "__main__":
    main()