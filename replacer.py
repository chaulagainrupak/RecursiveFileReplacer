import os

# Capture the output of the find command
dirs_output = os.popen("find . -mindepth 1 -type d -print0").read()

# Split the output into lines to get a list of directories
dirs = dirs_output.split('\0')[:-1]  # Split by null character, excluding the last empty element

# Iterate over the directories
for dir in dirs:
    print(dir)
    # Remove existing index.html files
    os.system(f"rm -f '{dir}/index.html'")
    # Create a symbolic link to dirindex.html
    os.system(f"cp dirindex.html '{dir}/index.html'")
