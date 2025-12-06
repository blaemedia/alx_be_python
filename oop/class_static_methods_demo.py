class Calculator:
    """
    A calculator class demonstrating class methods and static methods.
    
    Class methods are bound to the class and can access/modify class state.
    Static methods are utility functions that don't need access to class or instance.
    """
    
    # Class attribute - shared by all instances and accessible by class methods
    calculation_type = "Arithmetic Operations"
    
    def __init__(self, brand="Generic", model="Standard"):
        """
        Instance initialization method.
        
        Args:
            brand (str): The brand of the calculator
            model (str): The model of the calculator
        """
        self.brand = brand
        self.model = model
        self.memory = 0  # Instance attribute - unique to each instance
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """
        Static method to add two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        Class method to multiply two numbers.
        
        Note: The first parameter is 'cls' (the class, not an instance)
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
    @classmethod
    def change_calculation_type(cls, new_type: str):
        """
        Class method to modify class attribute.
        
        Args:
            new_type (str): New calculation type
        """
        previous_type = cls.calculation_type
        cls.calculation_type = new_type
        print(f"Calculation type changed from '{previous_type}' to '{new_type}'")


def demonstrate_basic_requirements():
    """
    Demonstrate the exact requirements from the task description.
    """
    print("=" * 60)
    print("DEMONSTRATING EXACT REQUIREMENTS")
    print("=" * 60)
    
    print("\n1. Class attribute:")
    print(f"   Calculator.calculation_type = '{Calculator.calculation_type}'")
    
    print("\n2. Static method - add(a, b):")
    result = Calculator.add(10, 20)
    print(f"   Calculator.add(10, 20) = {result}")
    
    print("\n3. Class method - multiply(cls, a, b):")
    print("   Note: This prints the calculation_type before returning result")
    result = Calculator.multiply(5, 6)
    print(f"   Calculator.multiply(5, 6) = {result}")
    
    # Create an instance to show methods work on instances too
    calc = Calculator()
    print("\n4. Using methods on an instance:")
    print(f"   calc.add(15, 25) = {calc.add(15, 25)}")
    print(f"   calc.multiply(7, 8) = {calc.multiply(7, 8)}")


def show_method_signatures():
    """
    Show the actual method signatures.
    """
    print("\n" + "=" * 60)
    print("METHOD SIGNATURES")
    print("=" * 60)
    
    print("\nClass method signature:")
    print("  @classmethod")
    print("  def multiply(cls, a, b):")
    print("      print(f\"Calculation type: {cls.calculation_type}\")")
    print("      return a * b")
    
    print("\nStatic method signature:")
    print("  @staticmethod")
    print("  def add(a, b):")
    print("      return a + b")


def test_correct_implementation():
    """
    Test that the implementation meets all requirements.
    """
    print("\n" + "=" * 60)
    print("TESTING IMPLEMENTATION")
    print("=" * 60)
    
    tests_passed = 0
    total_tests = 5
    
    # Test 1: Check class attribute exists
    try:
        if hasattr(Calculator, 'calculation_type'):
            print("✓ Test 1: Class attribute 'calculation_type' exists")
            tests_passed += 1
        else:
            print("✗ Test 1: Missing class attribute 'calculation_type'")
    except:
        print("✗ Test 1: Error checking class attribute")
    
    # Test 2: Check static method signature
    try:
        import inspect
        sig = inspect.signature(Calculator.add)
        params = list(sig.parameters.keys())
        if len(params) == 2 and params == ['a', 'b']:
            print("✓ Test 2: Static method 'add' has correct signature (a, b)")
            tests_passed += 1
        else:
            print(f"✗ Test 2: Static method 'add' has incorrect signature: {params}")
    except:
        print("✗ Test 2: Error checking static method signature")
    
    # Test 3: Check class method signature
    try:
        import inspect
        sig = inspect.signature(Calculator.multiply)
        params = list(sig.parameters.keys())
        if len(params) == 3 and params == ['cls', 'a', 'b']:
            print("✓ Test 3: Class method 'multiply' has correct signature (cls, a, b)")
            tests_passed += 1
        else:
            print(f"✗ Test 3: Class method 'multiply' has incorrect signature: {params}")
    except:
        print("✗ Test 3: Error checking class method signature")
    
    # Test 4: Test static method functionality
    try:
        result = Calculator.add(3, 4)
        if result == 7:
            print("✓ Test 4: Static method 'add' works correctly (3 + 4 = 7)")
            tests_passed += 1
        else:
            print(f"✗ Test 4: Static method 'add' returned {result}, expected 7")
    except:
        print("✗ Test 4: Error testing static method functionality")
    
    # Test 5: Test class method functionality
    try:
        # Capture print output
        import io
        import sys
        
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        
        result = Calculator.multiply(5, 6)
        
        sys.stdout = old_stdout
        output = buffer.getvalue().strip()
        
        if result == 30 and "Calculation type: Arithmetic Operations" in output:
            print("✓ Test 5: Class method 'multiply' works correctly")
            print(f"  Output: {output}")
            print(f"  Result: 5 * 6 = {result}")
            tests_passed += 1
        else:
            print(f"✗ Test 5: Class method issues")
            print(f"  Output: {output}")
            print(f"  Result: {result}, expected 30")
    except:
        print("✗ Test 5: Error testing class method functionality")
    
    print(f"\n{'='*60}")
    print(f"RESULTS: {tests_passed}/{total_tests} tests passed")
    print(f"{'='*60}")
    
    return tests_passed == total_tests


def interactive_examples():
    """
    Interactive examples to demonstrate the methods.
    """
    print("\n" + "=" * 60)
    print("INTERACTIVE EXAMPLES")
    print("=" * 60)
    
    while True:
        print("\nOptions:")
        print("1. Use Calculator.add(a, b)")
        print("2. Use Calculator.multiply(a, b)")
        print("3. Change calculation_type")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = Calculator.add(a, b)
                print(f"\nCalculator.add({a}, {b}) = {result}")
                print(f"Note: This is a static method - no access to cls or self")
            except ValueError:
                print("Please enter valid numbers.")
        
        elif choice == "2":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"\nCalling Calculator.multiply({a}, {b}):")
                result = Calculator.multiply(a, b)
                print(f"Result: {a} * {b} = {result}")
                print(f"Note: This is a class method - can access cls.calculation_type")
            except ValueError:
                print("Please enter valid numbers.")
        
        elif choice == "3":
            print(f"\nCurrent calculation_type: '{Calculator.calculation_type}'")
            new_type = input("Enter new calculation_type: ").strip()
            if new_type:
                Calculator.calculation_type = new_type
                print(f"Updated calculation_type to: '{Calculator.calculation_type}'")
                
                # Demonstrate that multiply now uses the new type
                print("\nTesting multiply with new calculation_type:")
                Calculator.multiply(2, 3)
            else:
                print("Calculation type cannot be empty.")
        
        elif choice == "4":
            print("\nFinal state:")
            print(f"Calculator.calculation_type = '{Calculator.calculation_type}'")
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


def main():
    """
    Main function to run all demonstrations.
    """
    print("\n" + "=" * 60)
    print("CLASS METHODS AND STATIC METHODS DEMONSTRATION")
    print("=" * 60)
    
    print("\nThis program demonstrates:")
    print("1. A static method: add(a, b)")
    print("2. A class method: multiply(cls, a, b)")
    print("3. A class attribute: calculation_type")
    
    # Show basic requirements
    demonstrate_basic_requirements()
    
    # Show method signatures
    show_method_signatures()
    
    # Run tests
    all_passed = test_correct_implementation()
    
    if all_passed:
        print("\n" + "=" * 60)
        print("ALL REQUIREMENTS MET!")
        print("=" * 60)
        
        # Run interactive examples
        run_interactive = input("\nRun interactive examples? (y/n): ").strip().lower()
        if run_interactive == 'y':
            interactive_examples()
        else:
            print("\nDemonstration complete!")
    else:
        print("\nSome requirements not met. Please fix the issues.")
    
    # Final summary
    print("\n" + "=" * 60)
    print("QUICK REFERENCE")
    print("=" * 60)
    print("\nClass Method (multiply):")
    print("  • First parameter: cls (the class)")
    print("  • Can access class attributes: cls.calculation_type")
    print("  • Called as: Calculator.multiply(a, b) or instance.multiply(a, b)")
    
    print("\nStatic Method (add):")
    print("  • No cls or self parameter")
    print("  • Cannot access class or instance attributes")
    print("  • Called as: Calculator.add(a, b) or instance.add(a, b)")
    
    print("\nExample usage:")
    print(f"  Calculator.add(5, 3) = {Calculator.add(5, 3)}")
    print(f"  Calculator.multiply(4, 5) = ", end="")
    Calculator.multiply(4, 5)


if __name__ == "__main__":
    main()