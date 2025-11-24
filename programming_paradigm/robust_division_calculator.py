def safe_divide(numerator, denominator):
    
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Both arguments must be numbers"
    
    try:
        # Attempt to perform division
        result = num / den
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"