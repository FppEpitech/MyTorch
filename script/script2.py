import os
import random

def shuffle_lines_in_files(input_files, output_file, quotas):
    """
    Reads a specified number of lines from multiple input files based on quotas, shuffles them randomly,
    and writes them to a single output file.

    :param input_files: List of file paths to read lines from.
    :param output_file: Path to the output file to write shuffled lines to.
    :param quotas: Dictionary mapping file patterns to the number of lines to read from matching files.
    """
    all_lines = []

    # Process each input file based on its quota
    for file_path in input_files:
        lines_to_read = 0

        # Determine quota based on file path
        for pattern, quota in quotas.items():
            if pattern in file_path:
                lines_to_read = quota
                break

        # Read lines from the file
        if lines_to_read > 0 and os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for _ in range(lines_to_read):
                    line = file.readline()
                    if not line:
                        break
                    all_lines.append(line)
        else:
            print(f"Warning: {file_path} does not match any pattern or is not a valid file.")

    # Shuffle the lines randomly
    random.shuffle(all_lines)

    # Write the shuffled lines to the output file
    with open(output_file, 'w', encoding='utf-8') as output:
        output.writelines(all_lines)

    print(f"Shuffled lines written to {output_file}")

# Example usage
if __name__ == "__main__":
    # List of input file paths
    input_files = [
        "tests/datasets/check/10_pieces.txt",
        "tests/datasets/check/20_pieces.txt",
        "tests/datasets/check/many_pieces.txt",
        "tests/datasets/checkmate/10_pieces.txt",
        "tests/datasets/checkmate/20_pieces.txt",
        "tests/datasets/checkmate/many_pieces.txt",
        "tests/datasets/nothing/10_pieces.txt",
        "tests/datasets/nothing/20_pieces.txt",
        "tests/datasets/nothing/many_pieces.txt",
        "tests/datasets/stalemate/10_pieces.txt",
        "tests/datasets/stalemate/20_pieces.txt",
        "tests/datasets/stalemate/many_pieces.txt"
    ]

    # Path to the output file
    output_file = "shuffled_output2.txt"

    # Quotas for file groups
    quotas = {
        "tests/datasets/checkmate/": 100,      # 100 lines from check files
        "tests/datasets/stalemate/": 80,   # 100 lines from nothing files
        "tests/datasets/nothing": 80,             # 20 lines from all other files
        "tests/datasets/check": 20             # 20 lines from all other files
    }

    # Call the function
    shuffle_lines_in_files(input_files, output_file, quotas)
