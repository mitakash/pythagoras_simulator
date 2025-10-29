#!/usr/bin/env python3
"""
Visual Pythagorean Theorem Simulator
Creates visual representations of right triangles and the Pythagorean theorem
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from pythagoras_simulator import PythagoreanSimulator


class VisualPythagoreanSimulator(PythagoreanSimulator):
    """
    Extended simulator that creates visual representations of the theorem
    """
    
    def visualize_triangle(self, a, b, show_squares=True, save_file=None):
        """
        Visualize a right triangle with optional squares on each side
        to demonstrate the Pythagorean theorem visually
        """
        c = self.calculate_hypotenuse(a, b)
        
        # Create figure with larger size for better visibility
        fig, ax = plt.subplots(1, 1, figsize=(12, 10))
        
        # Define triangle vertices (right angle at origin)
        triangle = np.array([[0, 0], [a, 0], [a, b], [0, 0]])
        
        # Plot the triangle
        ax.plot(triangle[:, 0], triangle[:, 1], 'b-', linewidth=3, label='Triangle')
        
        # Add labels to sides
        ax.text(a/2, -0.3, f'a = {a}', ha='center', fontsize=14, fontweight='bold', color='blue')
        ax.text(a + 0.3, b/2, f'b = {b}', va='center', fontsize=14, fontweight='bold', color='green')
        ax.text(a/2 - 0.5, b/2 + 0.5, f'c = {c:.2f}', ha='center', fontsize=14, fontweight='bold', color='red')
        
        # Mark the right angle
        square_size = min(a, b) * 0.1
        right_angle = patches.Rectangle((a - square_size, 0), square_size, square_size, 
                                       linewidth=2, edgecolor='black', facecolor='none')
        ax.add_patch(right_angle)
        
        if show_squares:
            # Draw squares on each side to visualize a² + b² = c²
            
            # Square on side a (below the triangle)
            square_a = patches.Rectangle((0, -a), a, a, linewidth=2, 
                                        edgecolor='blue', facecolor='lightblue', alpha=0.3)
            ax.add_patch(square_a)
            ax.text(a/2, -a/2, f'a² = {a**2:.2f}', ha='center', va='center', 
                   fontsize=12, fontweight='bold', color='darkblue')
            
            # Square on side b (to the right of the triangle)
            square_b = patches.Rectangle((a, 0), b, b, linewidth=2, 
                                        edgecolor='green', facecolor='lightgreen', alpha=0.3)
            ax.add_patch(square_b)
            ax.text(a + b/2, b/2, f'b² = {b**2:.2f}', ha='center', va='center', 
                   fontsize=12, fontweight='bold', color='darkgreen')
            
            # Square on hypotenuse (rotated)
            # Calculate the angle of the hypotenuse
            angle = np.arctan2(b, a)
            
            # Create square on hypotenuse
            # Starting point is at (a, b)
            # Direction perpendicular to hypotenuse
            perp_angle = angle + np.pi/2
            
            # Four corners of the square on hypotenuse
            corner1 = np.array([a, b])
            corner2 = corner1 + c * np.array([np.cos(angle - np.pi), np.sin(angle - np.pi)])
            corner3 = corner2 + c * np.array([np.cos(perp_angle), np.sin(perp_angle)])
            corner4 = corner1 + c * np.array([np.cos(perp_angle), np.sin(perp_angle)])
            
            square_c = np.array([corner1, corner2, corner3, corner4, corner1])
            ax.fill(square_c[:, 0], square_c[:, 1], color='lightcoral', alpha=0.3, 
                   edgecolor='red', linewidth=2)
            
            # Place text in center of square
            center_x = (corner1[0] + corner2[0] + corner3[0] + corner4[0]) / 4
            center_y = (corner1[1] + corner2[1] + corner3[1] + corner4[1]) / 4
            ax.text(center_x, center_y, f'c² = {c**2:.2f}', ha='center', va='center', 
                   fontsize=12, fontweight='bold', color='darkred')
        
        # Set equal aspect ratio and adjust limits
        ax.set_aspect('equal')
        if show_squares:
            margin = 0.5
            ax.set_xlim(-margin, max(a + b, a) + margin)
            ax.set_ylim(-a - margin, max(b, c * np.sin(np.arctan2(b, a)) + c) + margin)
        else:
            margin = 0.5
            ax.set_xlim(-margin, a + margin)
            ax.set_ylim(-margin, b + margin)
        
        # Add title and equation
        title = f'Pythagorean Theorem: a² + b² = c²'
        if show_squares:
            title += f'\n{a}² + {b}² = {c:.2f}²'
            title += f'\n{a**2:.2f} + {b**2:.2f} = {c**2:.2f}'
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('X', fontsize=12)
        ax.set_ylabel('Y', fontsize=12)
        
        plt.tight_layout()
        
        if save_file:
            plt.savefig(save_file, dpi=150, bbox_inches='tight')
            print(f"Visualization saved to {save_file}")
        
        plt.show()
        
        return fig, ax
    
    def visualize_proof(self, a, b, save_file=None):
        """
        Create a visual proof of the Pythagorean theorem
        Shows how the squares relate to each other
        """
        c = self.calculate_hypotenuse(a, b)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # Left plot: Triangle with individual squares
        ax1.set_title('Individual Squares', fontsize=14, fontweight='bold')
        
        # Draw triangle
        triangle = np.array([[0, 0], [a, 0], [a, b], [0, 0]])
        ax1.plot(triangle[:, 0], triangle[:, 1], 'k-', linewidth=3)
        
        # Squares on sides a and b
        square_a = patches.Rectangle((0, -a), a, a, linewidth=2, 
                                    edgecolor='blue', facecolor='lightblue', alpha=0.5)
        ax1.add_patch(square_a)
        ax1.text(a/2, -a/2, f'a² = {a**2:.2f}', ha='center', va='center', 
                fontsize=14, fontweight='bold')
        
        square_b = patches.Rectangle((a, 0), b, b, linewidth=2, 
                                    edgecolor='green', facecolor='lightgreen', alpha=0.5)
        ax1.add_patch(square_b)
        ax1.text(a + b/2, b/2, f'b² = {b**2:.2f}', ha='center', va='center', 
                fontsize=14, fontweight='bold')
        
        ax1.set_aspect('equal')
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim(-0.5, a + b + 0.5)
        ax1.set_ylim(-a - 0.5, b + 0.5)
        
        # Right plot: Triangle with hypotenuse square
        ax2.set_title('Hypotenuse Square', fontsize=14, fontweight='bold')
        
        # Draw triangle
        ax2.plot(triangle[:, 0], triangle[:, 1], 'k-', linewidth=3)
        
        # Square on hypotenuse
        angle = np.arctan2(b, a)
        perp_angle = angle + np.pi/2
        
        corner1 = np.array([a, b])
        corner2 = corner1 + c * np.array([np.cos(angle - np.pi), np.sin(angle - np.pi)])
        corner3 = corner2 + c * np.array([np.cos(perp_angle), np.sin(perp_angle)])
        corner4 = corner1 + c * np.array([np.cos(perp_angle), np.sin(perp_angle)])
        
        square_c = np.array([corner1, corner2, corner3, corner4, corner1])
        ax2.fill(square_c[:, 0], square_c[:, 1], color='lightcoral', alpha=0.5, 
                edgecolor='red', linewidth=2)
        
        center_x = (corner1[0] + corner2[0] + corner3[0] + corner4[0]) / 4
        center_y = (corner1[1] + corner2[1] + corner3[1] + corner4[1]) / 4
        ax2.text(center_x, center_y, f'c² = {c**2:.2f}', ha='center', va='center', 
                fontsize=14, fontweight='bold')
        
        ax2.set_aspect('equal')
        ax2.grid(True, alpha=0.3)
        ax2.set_xlim(-0.5, a + 0.5)
        ax2.set_ylim(-0.5, max(b, corner3[1]) + 0.5)
        
        # Add main title
        fig.suptitle(f'Pythagorean Theorem Proof: {a}² + {b}² = {c:.2f}²  →  {a**2:.2f} + {b**2:.2f} = {c**2:.2f}', 
                    fontsize=16, fontweight='bold')
        
        plt.tight_layout()
        
        if save_file:
            plt.savefig(save_file, dpi=150, bbox_inches='tight')
            print(f"Proof visualization saved to {save_file}")
        
        plt.show()
        
        return fig, (ax1, ax2)


def main():
    """
    Demonstrate the visual simulator
    """
    print("\n" + "="*60)
    print("  VISUAL PYTHAGOREAN THEOREM SIMULATOR")
    print("="*60)
    
    simulator = VisualPythagoreanSimulator()
    
    # Example 1: Classic 3-4-5 triangle
    print("\nExample 1: The classic 3-4-5 right triangle")
    simulator.visualize_triangle(3, 4, show_squares=True)
    
    # Example 2: Another common triangle
    print("\nExample 2: The 5-12-13 right triangle")
    simulator.visualize_triangle(5, 12, show_squares=True)
    
    # Example 3: Visual proof
    print("\nExample 3: Visual proof of the Pythagorean theorem")
    simulator.visualize_proof(3, 4)


if __name__ == "__main__":
    main()
