def count_and_sort_chairs(file_path):
    """
    Reads a file representing an apartment floor plan and counts the different types of chairs.
    Outputs the total number of each chair type for the whole apartment and per room, sorted alphabetically by room names.

    :param file_path: Path to the floor plan file.
    :return: A string representation of the chair counts formatted as per requirements.
    """

    chair_types = {'P': 'plastic chair', 'W': 'wooden chair', 'S': 'sofa', 'C': 'china chair'}
    total_counts = {v: 0 for v in chair_types.values()}
    room_counts = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_room = None
    for line in lines:
        if '(' in line and ')' in line:
            current_room = line[line.find('(')+1 : line.find(')')]
            if current_room not in room_counts:
                room_counts[current_room] = {v: 0 for v in chair_types.values()}
        
        for char, chair_type in chair_types.items():
            count = line.count(char)
            if count > 0:
                total_counts[chair_type] += count
                if current_room:
                    room_counts[current_room][chair_type] += count

    # Format the output
    output = "total:\n"
    output += ', '.join([f"{chair[0]}: {count}" for chair, count in total_counts.items()]) + "\n"

    for room in sorted(room_counts.keys()):
        output += f"{room}:\n"
        output += ', '.join([f"{chair[0]}: {count}" for chair, count in room_counts[room].items()]) + "\n"

    return output

# Test the function with the provided file
file_path = 'rooms.txt'
output = count_and_sort_chairs(file_path)

print(output)


