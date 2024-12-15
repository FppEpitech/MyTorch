import os
import random

def shuffle_lines_in_files(input_files, output_file, lines_per_file):
    """
    Reads a specified number of lines from multiple input files, shuffles them randomly, and writes them to a single output file.

    :param input_files: List of file paths to read lines from.
    :param output_file: Path to the output file to write shuffled lines to.
    :param lines_per_file: Number of lines to read from each file.
    """
    all_lines = []

    # Read a specific number of lines from each file
    for file_path in input_files:
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for _ in range(lines_per_file):
                    line = file.readline()
                    if not line:
                        break
                    all_lines.append(line)
        else:
            print(f"Warning: {file_path} is not a valid file and will be skipped.")

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
    output_file = "shuffled_output.txt"

    # Number of lines to read from each file
    lines_per_file = 50

    # Call the function
    shuffle_lines_in_files(input_files, output_file, lines_per_file)
