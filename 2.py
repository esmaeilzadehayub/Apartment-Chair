def parse_floor_plan(file_path):
    """
    Parses the floor plan from the file and counts the different types of chairs.
    Outputs the total number of each chair type for the whole apartment and per room.

    :param file_path: Path to the floor plan file.
    :return: A string representation of the chair counts.
    """
    # Define chair types and initialize counts
    chair_types = {'W': 'wooden chair', 'P': 'plastic chair', 'S': 'sofa', 'C': 'china chair'}
    total_counts = {chair: 0 for chair in chair_types.values()}
    room_counts = {}

    # Read the file and process each line
    with open(file_path, 'r') as file:
        lines = file.readlines()

    current_room = ""
    for line in lines:
        if '(' in line and ')' in line:
            # Extract the room name
            current_room = line[line.find('(') + 1:line.find(')')].strip()
            if current_room not in room_counts:
                room_counts[current_room] = {chair: 0 for chair in chair_types.values()}
        
        # Count each type of chair in the line
        for char, chair in chair_types.items():
            count = line.count(char)
            total_counts[chair] += count
            if current_room:
                room_counts[current_room][chair] += count

    return total_counts, room_counts

# Testing the revised function with the provided file
file_path = 'rooms.txt'
total_counts, room_counts = parse_floor_plan(file_path)

# Formatting the output
output = "total:\n" + ', '.join([f"{k[0]}: {v}" for k, v in total_counts.items()]) + "\n"
for room in sorted(room_counts.keys()):
    output += f"{room}:\n" + ', '.join([f"{k[0]}: {v}" for k, v in room_counts[room].items()]) + "\n"

output


