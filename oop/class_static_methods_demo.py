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
        
        Static methods:
        - Don't have access to 'self' or 'cls'
        - Don't modify class or instance state
        - Are essentially utility functions bound to the class namespace
        - Can be called on the class or instance
        
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
        
        Class methods:
        - Have access to 'cls' (the class, not instance)
        - Can access and modify class attributes
        - Can be used as alternative constructors
        - Can be called on the class or instance
        
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
        
        This demonstrates how class methods can modify class state.
        
        Args:
            new_type (str): New calculation type
        """
        previous_type = cls.calculation_type
        cls.calculation_type = new_type
        print(f"Calculation type changed from '{previous_type}' to '{new_type}'")
    
    @classmethod
    def create_scientific_calculator(cls):
        """
        Alternative constructor - class method as factory method.
        
        This is a common use of class methods: creating instances
        with predefined configurations.
        
        Returns:
            Calculator: A scientific calculator instance
        """
        calc = cls(brand="Scientific", model="Pro-X")
        calc.calculation_type = "Scientific Operations"  # Instance-specific, not class-wide
        return calc
    
    @staticmethod
    def calculate_average(numbers: list) -> float:
        """
        Another static method example.
        
        This doesn't need access to class or instance state.
        It's just a utility function related to calculations.
        
        Args:
            numbers (list): List of numbers
            
        Returns:
            float: Average of the numbers
            
        Raises:
            ValueError: If the list is empty
        """
        if not numbers:
            raise ValueError("Cannot calculate average of empty list")
        
        return sum(numbers) / len(numbers)
    
    @staticmethod
    def is_even(number: int) -> bool:
        """
        Static method that doesn't require instance or class context.
        
        Args:
            number (int): Number to check
            
        Returns:
            bool: True if number is even, False otherwise
        """
        return number % 2 == 0
    
    def instance_method_example(self):
        """
        Instance method for comparison.
        
        Instance methods:
        - Have access to 'self' (the instance)
        - Can access and modify instance attributes
        - Can access class attributes via self.class or type(self)
        """
        print(f"\nInstance Method Example:")
        print(f"  Brand: {self.brand}")
        print(f"  Model: {self.model}")
        print(f"  Memory: {self.memory}")
        print(f"  Calculation Type (via instance): {self.calculation_type}")
        print(f"  Calculation Type (via class): {Calculator.calculation_type}")


def demonstrate_usage():
    """
    Demonstrate the usage of class methods and static methods.
    """
    print("=" * 70)
    print("CLASS METHODS vs STATIC METHODS DEMONSTRATION")
    print("=" * 70)
    
    # 1. Using static methods
    print("\n1. USING STATIC METHODS (No instance or class state needed):")
    print("-" * 60)
    
    # Calling static method on class
    result1 = Calculator.add(10, 5)
    print(f"Calculator.add(10, 5) = {result1}")
    
    # Calling static method on instance
    calc1 = Calculator()
    result2 = calc1.add(20, 30)
    print(f"calc1.add(20, 30) = {result2}")
    
    # More static method examples
    numbers = [1, 2, 3, 4, 5]
    average = Calculator.calculate_average(numbers)
    print(f"Calculator.calculate_average({numbers}) = {average}")
    
    print(f"Calculator.is_even(10) = {Calculator.is_even(10)}")
    print(f"Calculator.is_even(7) = {Calculator.is_even(7)}")
    
    # 2. Using class methods
    print("\n\n2. USING CLASS METHODS (Access to class state):")
    print("-" * 60)
    
    # Calling class method on class
    result3 = Calculator.multiply(6, 7)
    print(f"Calculator.multiply(6, 7) = {result3}")
    
    # Calling class method on instance
    calc2 = Calculator()
    result4 = calc2.multiply(8, 9)
    print(f"calc2.multiply(8, 9) = {result4}")
    
    # 3. Demonstrating class attribute access/modification
    print("\n\n3. CLASS ATTRIBUTE MANIPULATION:")
    print("-" * 60)
    
    print(f"Original calculation_type: {Calculator.calculation_type}")
    
    # Modify using class method
    Calculator.change_calculation_type("Advanced Arithmetic")
    print(f"After change: {Calculator.calculation_type}")
    
    # Check that change affects all instances
    calc3 = Calculator()
    print(f"Instance calc3 sees: {calc3.calculation_type}")
    
    # 4. Class method as alternative constructor
    print("\n\n4. CLASS METHOD AS ALTERNATIVE CONSTRUCTOR:")
    print("-" * 60)
    
    scientific_calc = Calculator.create_scientific_calculator()
    print(f"Created scientific calculator: {scientific_calc.brand} {scientific_calc.model}")
    
    # Note: The instance-specific calculation_type doesn't affect the class
    print(f"Instance calculation_type: {scientific_calc.calculation_type}")
    print(f"Class calculation_type: {Calculator.calculation_type}")
    
    # 5. Instance method comparison
    print("\n\n5. INSTANCE METHOD COMPARISON:")
    print("-" * 60)
    
    my_calc = Calculator(brand="Texas Instruments", model="TI-84")
    my_calc.memory = 100
    my_calc.instance_method_example()


def demonstrate_differences():
    """
    Clearly explain the differences between method types.
    """
    print("\n" + "=" * 70)
    print("KEY DIFFERENCES SUMMARY")
    print("=" * 70)
    
    print("\n┌─────────────────────────────────────────────────────────────┐")
    print("│                    METHOD TYPE COMPARISON                   │")
    print("├────────────────┬────────────────┬───────────────────────────┤")
    print("│   Instance     │    Class       │        Static            │")
    print("│    Method      │    Method      │        Method            │")
    print("├────────────────┼────────────────┼───────────────────────────┤")
    print("│ def method(self)│ @classmethod  │ @staticmethod            │")
    print("│                │ def method(cls)│ def method()             │")
    print("├────────────────┼────────────────┼───────────────────────────┤")
    print("│ Accesses       │ Accesses       │ No access to             │")
    print("│ instance (self)│ class (cls)    │ self or cls              │")
    print("├────────────────┼────────────────┼───────────────────────────┤")
    print("│ Modifies       │ Modifies       │ Cannot modify            │")
    print("│ instance state │ class state    │ instance/class state     │")
    print("├────────────────┼────────────────┼───────────────────────────┤")
    print("│ Called on      │ Can be called  │ Can be called            │")
    print("│ instance       │ on class or    │ on class or              │")
    print("│                │ instance       │ instance                 │")
    print("├────────────────┼────────────────┼───────────────────────────┤")
    print("│ Example:       │ Example:       │ Example:                 │")
    print("│ self.save()    │ cls.create()   │ Calculator.add(1, 2)     │")
    print("└────────────────┴────────────────┴───────────────────────────┘")
    
    print("\n\nWHEN TO USE EACH:")
    print("1. Instance Methods: When you need to work with instance data")
    print("2. Class Methods: When you need to work with class-level data or")
    print("   create alternative constructors")
    print("3. Static Methods: For utility functions that don't need access")
    print("   to class or instance state")


def interactive_demo():
    """
    Interactive demonstration of class and static methods.
    """
    print("\n" + "=" * 70)
    print("INTERACTIVE DEMONSTRATION")
    print("=" * 70)
    
    while True:
        print("\nOptions:")
        print("1. Use static method: add two numbers")
        print("2. Use class method: multiply two numbers")
        print("3. Change calculation type (class method)")
        print("4. Create a scientific calculator (class method)")
        print("5. Calculate average (static method)")
        print("6. Check if number is even (static method)")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = Calculator.add(a, b)
                print(f"Result: {a} + {b} = {result}")
            except ValueError:
                print("Please enter valid numbers.")
        
        elif choice == "2":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = Calculator.multiply(a, b)
                print(f"Result: {a} × {b} = {result}")
            except ValueError:
                print("Please enter valid numbers.")
        
        elif choice == "3":
            new_type = input("Enter new calculation type: ").strip()
            if new_type:
                Calculator.change_calculation_type(new_type)
            else:
                print("Calculation type cannot be empty.")
        
        elif choice == "4":
            scientific_calc = Calculator.create_scientific_calculator()
            print(f"Created: {scientific_calc.brand} {scientific_calc.model}")
            scientific_calc.instance_method_example()
        
        elif choice == "5":
            numbers_input = input("Enter numbers separated by spaces: ").strip()
            try:
                numbers = [float(x) for x in numbers_input.split()]
                average = Calculator.calculate_average(numbers)
                print(f"Average of {numbers} = {average:.2f}")
            except ValueError:
                print("Please enter valid numbers.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "6":
            try:
                number = int(input("Enter an integer: "))
                if Calculator.is_even(number):
                    print(f"{number} is even")
                else:
                    print(f"{number} is odd")
            except ValueError:
                print("Please enter a valid integer.")
        
        elif choice == "7":
            print("\nFinal state:")
            print(f"Calculation type: {Calculator.calculation_type}")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("DEMONSTRATING CLASS METHODS AND STATIC METHODS IN PYTHON")
    print("=" * 70)
    
    # Demonstrate usage
    demonstrate_usage()
    
    # Show differences
    demonstrate_differences()
    
    # Interactive demo
    run_interactive = input("\nRun interactive demo? (y/n): ").strip().lower()
    if run_interactive == 'y':
        interactive_demo()
    else:
        print("\nDemo complete!")
        
        # Final summary
        print("\n" + "=" * 70)
        print("QUICK REFERENCE EXAMPLES")
        print("=" * 70)
        print("\nStatic Method Call: Calculator.add(5, 3) =", Calculator.add(5, 3))
        print("Class Method Call: Calculator.multiply(4, 6) =", Calculator.multiply(4, 6))
        print(f"Class Attribute: Calculator.calculation_type = '{Calculator.calculation_type}'")