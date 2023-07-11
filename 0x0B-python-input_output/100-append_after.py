#!/usr/bin/python3
'''Write a function that inserts a line of text to a file,
after each line containing a specific string '''


def append_after(filename="", search_string="", new_string=""):
    '''inserts a line of text to a file
    after each line containing a specific string'''
    temp_filename = filename + ".tmp"
    with open(filename, 'r') as file_in, open(temp_filename, 'a') as file_out:
        for line in file_in:
            file_out.write(line)

            if search_string in line:
                file_out.write(new_string)

    with open(temp_filename, 'r') as temp_file:
        file_data = temp_file.read()
    with open(filename, 'w') as file:
        file.write(file_data)
