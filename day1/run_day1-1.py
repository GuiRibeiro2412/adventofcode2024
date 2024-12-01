
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
    
    # Sort both lists
    list1.sort()
    list2.sort()
    
    # Loop through both lists, get absolute difference between numbers
    total_distance = 0
    for i in range(len(list1)):
        diff = abs(int(list1[i]) - int(list2[i]))
        # Add absolute diff to difference count
        total_distance += diff
    
    print(f"Total distance: {total_distance}")
    

if __name__ == "__main__":
    main()
