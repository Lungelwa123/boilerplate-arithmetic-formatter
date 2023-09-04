def arithmetic_arranger(problems, show_answers=False):
    # Check the number of problems and the valid operators
    if len(problems) > 5:
        return "Error: Too many problems."
    valid_operators = ["+", "-"]

    # Initialize the lines for the arranged problems
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    # Loop through each problem and format it
    for problem in problems:
        # Split the problem into operands and operator
        left, op, right = problem.split()

        # Check if the operands are digits and have at most four digits
        if not (left.isdigit() and right.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Check if the operator is valid
        if op not in valid_operators:
            return "Error: Operator must be '+' or '-'."

        # Calculate the width of the problem and the answer
        width = max(len(left), len(right)) + 2
        if op == "+":
            answer = int(left) + int(right)
        else:
            answer = int(left) - int(right)

        # Align the operands and the operator to the right
        first_line += left.rjust(width) + "    "
        second_line += op + right.rjust(width - 1) + "    "

        # Add dashes to the third line
        third_line += "-" * width + "    "

        # Add the answer to the fourth line if required
        if show_answers:
            fourth_line += str(answer).rjust(width) + "    "

    # Remove the extra spaces at the end of each line
    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    third_line = third_line.rstrip()
    fourth_line = fourth_line.rstrip()

    # Return the arranged problems as a single string
    if show_answers:
        return "\n".join([first_line, second_line, third_line, fourth_line])
    else:
        return "\n".join([first_line, second_line, third_line])
