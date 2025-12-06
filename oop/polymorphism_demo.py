import math

class Shape:
    """
    Base class for all shapes.
    This class demonstrates polymorphism through method overriding.
    """
    
    def area(self):
        """
        Calculate the area of the shape.
        
        Returns:
            float: The area of the shape
            
        Raises:
            NotImplementedError: This method should be overridden by derived classes
        """
        raise NotImplementedError("Subclasses must implement the area() method")
    
    def __str__(self):
        """String representation of the shape"""
        return f"Shape"


class Rectangle(Shape):
    """
    Derived class for rectangles.
    Overrides the area() method to calculate rectangle area.
    """
    
    def __init__(self, length: float, width: float):
        """
        Initialize a rectangle with length and width.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers")
        
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width)
        """
        return self.length * self.width
    
    def __str__(self):
        """String representation of the rectangle"""
        return f"Rectangle(length={self.length}, width={self.width})"


class Circle(Shape):
    """
    Derived class for circles.
    Overrides the area() method to calculate circle area.
    """
    
    def __init__(self, radius: float):
        """
        Initialize a circle with a radius.
        
        Args:
            radius (float): The radius of the circle
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²)
        """
        return math.pi * (self.radius ** 2)
    
    def __str__(self):
        """String representation of the circle"""
        return f"Circle(radius={self.radius})"


def demonstrate_polymorphism():
    """
    Demonstrate polymorphism with shapes.
    
    This function shows how different shape objects can be treated uniformly
    through the common Shape interface, while each provides its own
    implementation of the area() method.
    """
    print("=" * 60)
    print("POLYMORPHISM DEMONSTRATION")
    print("=" * 60)
    
    # Create a list of different shapes
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Rectangle(7, 2),
        Circle(2.5),
        Rectangle(10, 6)
    ]
    
    print("\nCreated shapes:")
    for i, shape in enumerate(shapes, 1):
        print(f"{i}. {shape}")
    
    print("\n" + "=" * 60)
    print("CALCULATING AREAS (Polymorphic Behavior)")
    print("=" * 60)
    
    # Demonstrate polymorphic behavior
    total_area = 0
    
    for i, shape in enumerate(shapes, 1):
        # Even though we call the same method name 'area()',
        # each object uses its own implementation
        area = shape.area()
        total_area += area
        
        print(f"\nShape {i}: {shape}")
        print(f"  Type: {type(shape).__name__}")
        print(f"  Area: {area:.2f}")
        
        # Additional type-specific information
        if isinstance(shape, Rectangle):
            print(f"  Dimensions: {shape.length} × {shape.width}")
        elif isinstance(shape, Circle):
            print(f"  Radius: {shape.radius}")
            print(f"  Circumference: {2 * math.pi * shape.radius:.2f}")
    
    print(f"\n" + "=" * 60)
    print(f"Total area of all shapes: {total_area:.2f}")
    print("=" * 60)
    
    return shapes


def test_shape_base_class():
    """
    Test that the base Shape class properly raises NotImplementedError.
    """
    print("\n" + "=" * 60)
    print("TESTING BASE SHAPE CLASS")
    print("=" * 60)
    
    try:
        # Attempt to create a generic Shape and call area()
        shape = Shape()
        area = shape.area()
        print("ERROR: Should have raised NotImplementedError!")
    except NotImplementedError as e:
        print(f"✓ Correctly raised NotImplementedError: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {type(e).__name__}: {e}")


def calculate_area(shape: Shape) -> float:
    """
    Function that demonstrates polymorphism by accepting any Shape object.
    
    Args:
        shape (Shape): Any object that inherits from Shape
        
    Returns:
        float: The area of the shape
    """
    return shape.area()


def run_interactive_demo():
    """
    Interactive demonstration of polymorphism.
    """
    print("\n" + "=" * 60)
    print("INTERACTIVE POLYMORPHISM DEMO")
    print("=" * 60)
    
    shapes = []
    
    while True:
        print("\nOptions:")
        print("1. Add a Rectangle")
        print("2. Add a Circle")
        print("3. Calculate areas of all shapes")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            try:
                length = float(input("Enter rectangle length: "))
                width = float(input("Enter rectangle width: "))
                rectangle = Rectangle(length, width)
                shapes.append(rectangle)
                print(f"✓ Added: {rectangle}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            try:
                radius = float(input("Enter circle radius: "))
                circle = Circle(radius)
                shapes.append(circle)
                print(f"✓ Added: {circle}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            if not shapes:
                print("No shapes added yet.")
                continue
            
            print(f"\nCalculating areas for {len(shapes)} shape(s):")
            print("-" * 40)
            
            for i, shape in enumerate(shapes, 1):
                area = shape.area()  # Polymorphic call - works for all shapes!
                print(f"{i}. {shape}")
                print(f"   Area: {area:.2f}")
            
            total_area = sum(shape.area() for shape in shapes)
            print(f"\nTotal area: {total_area:.2f}")
        
        elif choice == "4":
            print("\nFinal summary:")
            if shapes:
                print(f"Created {len(shapes)} shape(s)")
                for i, shape in enumerate(shapes, 1):
                    print(f"{i}. {shape} - Area: {shape.area():.2f}")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Run all demonstrations
    print("Demonstrating Polymorphism in Python")
    print("-" * 40)
    
    # Test the base class
    test_shape_base_class()
    
    # Demonstrate polymorphism
    shapes = demonstrate_polymorphism()
    
    # Demonstrate polymorphic function
    print("\n" + "=" * 60)
    print("DEMONSTRATING POLYMORPHIC FUNCTION")
    print("=" * 60)
    
    # Show that calculate_area() works with any Shape
    if shapes:
        print(f"\nUsing calculate_area() function on each shape:")
        for i, shape in enumerate(shapes, 1):
            area = calculate_area(shape)
            print(f"{i}. {shape}: {area:.2f}")
    
    # Ask if user wants interactive demo
    run_interactive = input("\n\nRun interactive demo? (y/n): ").strip().lower()
    if run_interactive == 'y':
        run_interactive_demo()
    else:
        print("\nPolymorphism demonstration complete!")
        print("\nKey concepts demonstrated:")
        print("1. Method overriding (each shape implements its own area() method)")
        print("2. Polymorphic behavior (treating different shapes uniformly)")
        print("3. Liskov Substitution Principle (derived classes can replace base class)")