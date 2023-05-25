def input_to_list(input, args) -> list:
    inp_list = [substring.strip() for substring in input.split(",")]
    if args != len(inp_list):
        raise ValueError("Incorrect amount of arguments!")
    return inp_list

def input_to_int(input) -> list:
    try:
        return list(int(value) for value in input)
    except Exception as e:
        raise ValueError("Input contains string characters, integer expected!")
def format_data(columns, rows):
    form_data = ""

    # Calculate the maximum width for each column
    max_widths = []
    for i in range(len(columns)):
        max_width = max(len(str(column[i])) for column in rows + [columns])
        max_widths.append(max_width)

    # Format and append the column headers
    for i in range(len(columns)):
        if i == len(columns) - 1:
            form_data += str(columns[i]).ljust(max_widths[i])
            break
        form_data += str(columns[i]).ljust(max_widths[i]) + " | "
    form_data += "\n"

    # Append separator line
    form_data += "-" * (sum(max_widths) + 3 * (len(columns) - 1)) + "\n"

    # Format and append the data rows
    for row in rows:
        for i in range(len(row)):
            if i == len(row) - 1:
                form_data += str(row[i]).ljust(max_widths[i])
                break
            form_data += str(row[i]).ljust(max_widths[i]) + " | "
        form_data += "\n"

    return form_data



