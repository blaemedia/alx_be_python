def safe_divide(numerator, denominator):
    """
    Perform division with error handling for zero division and non-numeric inputs.
    
    Args:
        numerator: The number to be divided
        denominator: The number to divide by
    
    Returns:
        str: The division result message or error message
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        # Attempt to perform division
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."