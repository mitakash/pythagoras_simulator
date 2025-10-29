#!/usr/bin/env python3
"""
Visual demonstration of the Pythagorean Theorem
Generates images showing the theorem visually
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from visual_simulator import VisualPythagoreanSimulator


def main():
    """
    Generate visual demonstrations
    """
    print("Generating visual demonstrations...")
    
    simulator = VisualPythagoreanSimulator()
    
    # Example 1: Classic 3-4-5 triangle with squares
    print("Creating visualization 1: 3-4-5 triangle with squares")
    simulator.visualize_triangle(3, 4, show_squares=True, save_file='triangle_345_squares.png')
    
    # Example 2: 5-12-13 triangle
    print("Creating visualization 2: 5-12-13 triangle with squares")
    simulator.visualize_triangle(5, 12, show_squares=True, save_file='triangle_51213_squares.png')
    
    # Example 3: Simple triangle without squares
    print("Creating visualization 3: 3-4-5 triangle (simple)")
    simulator.visualize_triangle(3, 4, show_squares=False, save_file='triangle_345_simple.png')
    
    # Example 4: Visual proof
    print("Creating visualization 4: Visual proof of theorem")
    simulator.visualize_proof(3, 4, save_file='theorem_proof.png')
    
    print("\nAll visualizations created successfully!")
    print("Files created:")
    print("  - triangle_345_squares.png")
    print("  - triangle_51213_squares.png")
    print("  - triangle_345_simple.png")
    print("  - theorem_proof.png")


if __name__ == "__main__":
    main()
