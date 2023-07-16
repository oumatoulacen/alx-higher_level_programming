import sys

# Initialize variables for metrics
total_file_size = 0
status_counts = {}

try:
    line_count = 0

    for line in sys.stdin:
        line_count += 1

        # Split the input line into individual fields
        fields = line.split(' ')

        # Extract the file size from the input line
        file_size = int(fields[-1])

        # Update the total file size
        total_file_size += file_size

        # Extract the status code from the input line
        status_code = fields[-2]

        # Update the status counts dictionary
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print("Total file size:", total_file_size)

            # Print status code counts in ascending order
            for code in sorted(status_counts.keys()):
                print(code + ":", status_counts[code])

except KeyboardInterrupt:
    # Print final statistics upon keyboard interruption
    print("Total file size:", total_file_size)

    # Print status code counts in ascending order
    for code in sorted(status_counts.keys()):
        print(code + ":", status_counts[code])
