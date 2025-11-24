def safe_divide(numerator, denominator):
 
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        # Attempt to perform division
        result = num / den
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."