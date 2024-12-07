
with open(f"input.txt") as file:
    text = file.read()

    split_text = text.split("\n\n")
    rules = split_text[0].split()
    updates = split_text[1].split()


def get_applicable_rules(update) -> list[str, str]:
    applicable = []
    for rule in rules:
        rule_nums = rule.split("|")
        if all(page in update for page in rule_nums):
            applicable.append(rule_nums)
    return applicable


def follows_rule(update, rule) -> bool:
    update_iter = iter(update)
    return all(any(num == page for page in update_iter) for num in rule)


def get_middle_number(update: list[str]) -> int:
    return int(update[int(len(update)/2)])


def main():
    middle_sum = 0

    for update in updates:
        correct = True
        update = update.split(",")
        for rule in get_applicable_rules(update):
            if not follows_rule(update, rule):
                correct = False
        if correct:
            middle_sum += get_middle_number(update)

    print(f"Sum of middle page numbers: {middle_sum}")
    # Too high: 860337
    # Too high: 10705


if __name__ == "__main__":
    main()