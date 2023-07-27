import sys
import os
import re
import pypandoc

def align_vertical_bars_in_tables(adoc_content):
    # Regular expression for Asciidoc table lookup
    table_pattern = r'\|===([\s\S]*?)\|==='

    def process_table(match):
        # Get table contents from regular expression matching
        table = match.group(1)
        # Split the table into rows
        lines = table.strip().split('\n')

        # Determining the maximum number of symbols in each row
        max_lengths = [0] * len(lines[0].split('|'))
        new_lines = []

        for line in lines:
            # If there are no | symbols in the string, we skip it because it is an extra row
            if '|' not in line:
                continue
            cells = line.strip().split('|')
            if len(cells) != len(max_lengths):
                # If the number of '|' symbols in this row is not equal to the expected number of columns,
                # return the original table content without modifications.
                return match.group()
            for i, cell in enumerate(cells):
                # Find the maximum length for each cell
                max_lengths[i] = max(max_lengths[i], len(cell.strip()))
            # Save only rows with cells, excluding unnecessary rows
            new_lines.append(cells)

        aligned_lines = []
        for line in new_lines:
            # Align the symbols in each row
            aligned_cells = [cell.strip().ljust(max_lengths[i]) for i, cell in enumerate(line)]

            # Add spaces to the last element in every cell except empty cells
            max_length = max(max_lengths)
            aligned_cells = [cell[:-1] + ' ' + cell[-1] if cell and len(cell) < max_length else cell for cell in aligned_cells]

            # Add a space after the first | character in each line
            aligned_line = '| ' + ' | '.join(aligned_cells[1:])
            aligned_lines.append(aligned_line)

        # Generate the final result by enclosing it in the start and end markers of the Asciidoc table
        return '|===\n' + '\n'.join(aligned_lines) + '\n|==='

    # Apply the processing function to each table in the document
    aligned_adoc_content = re.sub(table_pattern, process_table, adoc_content)
    return aligned_adoc_content

def main():
    # Check if the number of command-line arguments is less than 2 (i.e., script name + at least one additional argument)
    if len(sys.argv) < 2:
        # If there are not enough arguments, print a usage message explaining how to use the script.
        print("Usage: python script.py input.adoc")
        # Return from the main function, terminating the script.
        return

    # Get the input filename from the command-line arguments.
    input_file = sys.argv[1]

    # Check if the input file exists in the current directory or the specified path.
    if not os.path.exists(input_file):
        # If the file does not exist, print an error message indicating that the file is not found.
        print(f"File '{input_file}' does not exist!")
        # Return from the main function, terminating the script.
        return

    # Open the input file and read its contents.
    with open(input_file, 'r', encoding='utf-8') as file:
        adoc_content = file.read()

    # Call the processing function and get the aligned table contents
    aligned_content = align_vertical_bars_in_tables(adoc_content)

    # Replace 'output.adoc' with the desired path to the file where the aligned result will be saved.
    output_file = 'output.adoc'
    # Open the output file in write mode and save the aligned content into it.
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(aligned_content)
    
    # Print a success message to inform the user that table prettify is completed and where the result is saved.
    print(f"Table prettify completed. Result saved in '{output_file}'.")

# Check if this script is being run as the main program.
if __name__ == "__main__":
    # If the script is being run, call the main function to start the table prettify process.
    main()
