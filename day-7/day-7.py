with open("terminal.txt") as f:
    lines = f.read().splitlines()

# Create dictionary of directories to store file sizes in
directories = {"/": 0}
file_path = "/"  # top file path

# loop through file to find commands
for line in lines:
    if line[0] == "$":
        if line[2:4] == "cd":
            if line[5] == "/":
                file_path = "/"
            elif line[5:7] == "..":
                file_path = file_path[0:file_path.rindex("/")]  # find the latest occurrence of / to locate parent directory
            else:
                file_path = file_path + "/" + line[5:]  # if command isn't home or move out, it's a new directory
                directories.update({file_path: 0})
        elif line[2:4] == "ls":
            pass    # we don't care about listing
    elif line[0:3] == "dir":
        pass    # we don't care about listing
    else:
        directory = file_path   # if it's not a command or a list, then it's a file - we want to access file sizes
        file_size = int(line[0:line.index(" ")])    # file size is at the start of the line, split from file name with a space
        for dir in range(directory.count("/")): # every "/" is a new directory. Directory size includes contained directories.
            directories[directory] += file_size # add file size to each containing directory
            directory = directory[0:directory.rindex("/")]  # find latest occurrence of "/" to move out a directory

total_size_p1 = 0
for dir in directories:
    if directories[dir] <= 100000:
        total_size_p1 += directories[dir]   # running total for all directories in dictionary
print(f"Sum of directories less than 100000: {total_size_p1}")

system_size = directories["/"]  # total system size is the size of the top directory
free_space = 70000000 - system_size     # total capacity of device is 70000000
delete_space = 30000000 - free_space    # we need at least 30000000 free

delete_candidates = []  # initialise list of directories that would free up enough space
for dir in directories:
    if directories[dir] > delete_space:
        delete_candidates.append(directories[dir])  # append to list if greater than size of space we need to free

print(f"Delete: {min(delete_candidates)}")  # find the smallest directory of the directories big enough to free enough space
