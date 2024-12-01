
day = "day1"

with open(f"{day}\\input.txt") as file:
    lines = file.readlines()

# print(lines)

def main():
    # Separate each column into a list
    list1 = []
    list2 = []
    for line in lines:
        split_line = line.split()
        list1.append(split_line[0])
        list2.append(split_line[1])
    
    
    # Loop through list1, and check how many times the value appears in list2
    similarity_score = 0
    for value in list1:
        appears = list2.count(value)
        # Multiply value by appearance count and add sum to similarity score
        similarity = int(value) * appears
        # Add absolute diff to difference count
        similarity_score += similarity
    
    print(f"Similarity score: {similarity_score}")
    

if __name__ == "__main__":
    main()
