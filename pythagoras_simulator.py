#!/usr/bin/env python3
"""
Pythagorean Theorem Simulator
A simple educational tool to help understand the Pythagorean theorem: a² + b² = c²
"""

import math
import sys


class PythagoreanSimulator:
    """
    A simulator for the Pythagorean theorem that can:
    - Calculate the hypotenuse given two sides
    - Calculate a side given the hypotenuse and another side
    - Verify if three sides form a right triangle
    """
    
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
    
    def calculate_hypotenuse(self, a, b):
        """
        Calculate the hypotenuse (c) given the two other sides (a and b)
        c = √(a² + b²)
        """
        if a <= 0 or b <= 0:
            raise ValueError("Sides must be positive numbers")
        
        self.a = a
        self.b = b
        self.c = math.sqrt(a**2 + b**2)
        return self.c
    
    def calculate_side(self, c, side):
        """
        Calculate a side given the hypotenuse and another side
        If we have c and a, then b = √(c² - a²)
        If we have c and b, then a = √(c² - b²)
        """
        if c <= 0 or side <= 0:
            raise ValueError("Sides must be positive numbers")
        
        if side >= c:
            raise ValueError("The hypotenuse must be the longest side")
        
        result = math.sqrt(c**2 - side**2)
        return result
    
    def verify_right_triangle(self, a, b, c):
        """
        Verify if three sides form a right triangle
        Returns True if a² + b² = c² (within a small tolerance for floating point)
        """
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive numbers")
        
        # Sort to ensure c is the largest
        sides = sorted([a, b, c])
        a, b, c = sides[0], sides[1], sides[2]
        
        # Check if a² + b² = c² (with tolerance for floating point errors)
        tolerance = 1e-10
        return abs(a**2 + b**2 - c**2) < tolerance
    
    def explain_theorem(self):
        """
        Return an explanation of the Pythagorean theorem
        """
        explanation = """
        ╔══════════════════════════════════════════════════════════════╗
        ║           THE PYTHAGOREAN THEOREM                           ║
        ╚══════════════════════════════════════════════════════════════╝
        
        In a right triangle, the square of the length of the hypotenuse 
        (the side opposite the right angle) is equal to the sum of the 
        squares of the lengths of the other two sides.
        
        Formula: a² + b² = c²
        
        Where:
          • a and b are the two shorter sides (legs)
          • c is the longest side (hypotenuse)
        
        Example:
          If a = 3 and b = 4, then:
          c = √(3² + 4²) = √(9 + 16) = √25 = 5
          
          This forms a 3-4-5 right triangle!
        """
        return explanation


def main():
    """
    Interactive command-line interface for the Pythagorean Theorem Simulator
    """
    simulator = PythagoreanSimulator()
    
    print("\n" + "="*60)
    print("  PYTHAGOREAN THEOREM SIMULATOR")
    print("  Learn about right triangles!")
    print("="*60)
    
    while True:
        print("\nWhat would you like to do?")
        print("  1. Calculate hypotenuse (c) from two sides (a, b)")
        print("  2. Calculate a side given hypotenuse and another side")
        print("  3. Verify if three sides form a right triangle")
        print("  4. Learn about the Pythagorean theorem")
        print("  5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            try:
                a = float(input("Enter side a: "))
                b = float(input("Enter side b: "))
                c = simulator.calculate_hypotenuse(a, b)
                
                print(f"\n✓ Result: The hypotenuse c = {c:.4f}")
                print(f"\nExplanation:")
                print(f"  a² + b² = c²")
                print(f"  {a}² + {b}² = {c}²")
                print(f"  {a**2:.4f} + {b**2:.4f} = {c**2:.4f}")
                
            except ValueError as e:
                print(f"\n✗ Error: {e}")
            except Exception as e:
                print(f"\n✗ Error: Invalid input. Please enter numbers.")
        
        elif choice == '2':
            try:
                c = float(input("Enter the hypotenuse (c): "))
                side = float(input("Enter the known side: "))
                result = simulator.calculate_side(c, side)
                
                print(f"\n✓ Result: The unknown side = {result:.4f}")
                print(f"\nExplanation:")
                print(f"  c² - side² = unknown²")
                print(f"  {c}² - {side}² = {result}²")
                print(f"  {c**2:.4f} - {side**2:.4f} = {result**2:.4f}")
                
            except ValueError as e:
                print(f"\n✗ Error: {e}")
            except Exception as e:
                print(f"\n✗ Error: Invalid input. Please enter numbers.")
        
        elif choice == '3':
            try:
                a = float(input("Enter side a: "))
                b = float(input("Enter side b: "))
                c = float(input("Enter side c: "))
                
                is_right = simulator.verify_right_triangle(a, b, c)
                
                sides = sorted([a, b, c])
                print(f"\n{'✓' if is_right else '✗'} Result: ", end="")
                
                if is_right:
                    print(f"YES! These sides form a right triangle.")
                    print(f"\nVerification:")
                    print(f"  {sides[0]}² + {sides[1]}² = {sides[2]}²")
                    print(f"  {sides[0]**2:.4f} + {sides[1]**2:.4f} = {sides[2]**2:.4f}")
                else:
                    print(f"NO. These sides do NOT form a right triangle.")
                    print(f"\nVerification:")
                    print(f"  {sides[0]}² + {sides[1]}² ≠ {sides[2]}²")
                    print(f"  {sides[0]**2:.4f} + {sides[1]**2:.4f} ≠ {sides[2]**2:.4f}")
                
            except ValueError as e:
                print(f"\n✗ Error: {e}")
            except Exception as e:
                print(f"\n✗ Error: Invalid input. Please enter numbers.")
        
        elif choice == '4':
            print(simulator.explain_theorem())
        
        elif choice == '5':
            print("\nThank you for using the Pythagorean Theorem Simulator!")
            print("Keep learning! 📐\n")
            break
        
        else:
            print("\n✗ Invalid choice. Please enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
