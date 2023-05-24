import sys  # Provides access to system-specific parameters and functions.

def solution(threshold, limit):
    accumulator = 0.0  # Cumulative sum of output values
    output_line = []  # List to store the transformed output values

    for input_line in sys.stdin:
        if (accumulator > limit):   
            output_line.append(0.0)  # If cumulative sum exceeds limit, append 0.0 and continue
            continue
        
        if (float(input_line) < threshold):
            output_line.append(0.0)  # If input value is less than threshold, append 0.0
        else:
            temp_output = float(input_line) - threshold  # Compute the transformed output value
            accumulator += temp_output  # Add the transformed output to the cumulative sum
            if (accumulator > limit):   
                output_line.append(temp_output - (accumulator - limit))  # Adjust output value to respect the limit
            else:
                output_line.append(temp_output)  # Append the transformed output value

    output_line.append(limit if accumulator > limit else accumulator)  # Append the cumulative sum respecting the limit
    return output_line

if __name__ == "__main__":
    arguments = sys.argv
    if (len(arguments) != 3):   # Check if exactly three command-line arguments (including the script name) are provided
        print("Command: compute.py <threshold> <limit>")
        sys.exit(1)
    
    threshold = float(sys.argv[1])  # Read the threshold value from command line argument
    limit = float(sys.argv[2])  # Read the limit value from command line argument

    output_line = solution(threshold, limit)  # Call the solution function to obtain the transformed output values
    
    for output in output_line:
        print(output)  # Print each output value on a new line