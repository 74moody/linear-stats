from scipy.stats import pearsonr as p
from scipy.stats import linregress as lin

# function to read file values
def readFile():
    # arrays to store the values
    yAxis = []
    xAxis = []
    try:
        # this will open data.txt in read more
        with open("data.txt", "r") as f:
            for line_number, line in enumerate(f, start=0):
                try:
                    number = int(line.strip())
                    yAxis.append(number)
                    xAxis.append(line_number)  # Store line number as x-axis value
                except ValueError:
                    print("[-] Error: Non-integer value found in data.txt.")
                    print("Example:\n123\n123\n123\n123")
                    return None, None  # Return None if non-integer found
        
        if not yAxis:
            print("[-] Error: No valid integers found in data.txt.")
            print("Example:\n123\n123\n123\n123")
            return None, None  # Return None if no valid integers found
    
    except FileNotFoundError:
        print("Error: File 'data.txt' not found.")
        return None, None  # Return None if file not found
    
    return xAxis, yAxis

def calculate():
    # read x and y values from readFile function
    xAxis, yAxis = readFile()
    
    if xAxis is None or yAxis is None:
        return
    
     # Calculate Linear Regression Line
    slope, intercept, r_value, p_value, std_err = lin(xAxis, yAxis)
    LinearRegFormula = f"Linear Regression Line: y = {slope:.6f}x + {intercept:.6f}"
    print(LinearRegFormula)
    
    # Calculate Pearson correlation coefficient
    cc, _ = p(xAxis, yAxis)
    print(f"Pearson Correlation Coefficient: {cc:.10f}")

   
    
# Call calculate function
calculate()
