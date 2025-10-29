#!/usr/bin/env python3
"""
Example usage of the Pythagorean Theorem Simulator
Demonstrates various ways to use the simulator
"""

from pythagoras_simulator import PythagoreanSimulator


def main():
    """
    Demonstrate example usage of the simulator
    """
    print("\n" + "="*60)
    print("  PYTHAGOREAN THEOREM SIMULATOR - EXAMPLES")
    print("="*60 + "\n")
    
    # Create a simulator instance
    sim = PythagoreanSimulator()
    
    # Example 1: Calculate hypotenuse
    print("Example 1: Calculate the hypotenuse of a triangle")
    print("-" * 60)
    a, b = 3, 4
    c = sim.calculate_hypotenuse(a, b)
    print(f"Given sides a = {a} and b = {b}")
    print(f"The hypotenuse c = {c}")
    print(f"Verification: {a}² + {b}² = {c}²")
    print(f"              {a**2} + {b**2} = {c**2}\n")
    
    # Example 2: Another classic triangle
    print("Example 2: The 5-12-13 triangle")
    print("-" * 60)
    a, b = 5, 12
    c = sim.calculate_hypotenuse(a, b)
    print(f"Given sides a = {a} and b = {b}")
    print(f"The hypotenuse c = {c}")
    print(f"This is another famous Pythagorean triple!\n")
    
    # Example 3: Calculate a side
    print("Example 3: Calculate a side given hypotenuse and one side")
    print("-" * 60)
    c, a = 10, 6
    b = sim.calculate_side(c, a)
    print(f"Given hypotenuse c = {c} and side a = {a}")
    print(f"The other side b = {b}")
    print(f"Verification: {a}² + {b}² = {c}²")
    print(f"              {a**2} + {b**2} = {c**2}\n")
    
    # Example 4: Verify a right triangle
    print("Example 4: Verify if sides form a right triangle")
    print("-" * 60)
    sides = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (2, 3, 4)]
    
    for a, b, c in sides:
        is_right = sim.verify_right_triangle(a, b, c)
        result = "✓ IS" if is_right else "✗ is NOT"
        print(f"Triangle ({a}, {b}, {c}) {result} a right triangle")
    
    print("\n" + "="*60)
    print("  Common Pythagorean Triples (right triangles)")
    print("="*60)
    
    triples = [
        (3, 4, 5),
        (5, 12, 13),
        (8, 15, 17),
        (7, 24, 25),
        (20, 21, 29),
        (9, 40, 41),
        (12, 35, 37),
        (11, 60, 61),
        (13, 84, 85),
        (36, 77, 85)
    ]
    
    print("\nHere are some famous Pythagorean triples:")
    print("\n{:<15} {:<20} {:<15}".format("Sides (a, b, c)", "Equation", "Result"))
    print("-" * 60)
    
    for a, b, c in triples:
        equation = f"{a}² + {b}² = {c}²"
        result = f"{a**2} + {b**2} = {c**2}"
        print("{:<15} {:<20} {:<15}".format(f"({a}, {b}, {c})", equation, result))
    
    print("\nThese are just a few examples! There are infinitely many Pythagorean triples.\n")


if __name__ == "__main__":
    main()
