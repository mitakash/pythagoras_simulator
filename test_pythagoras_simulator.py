#!/usr/bin/env python3
"""
Unit tests for the Pythagorean Theorem Simulator
"""

import unittest
import math
from pythagoras_simulator import PythagoreanSimulator


class TestPythagoreanSimulator(unittest.TestCase):
    """Test cases for the PythagoreanSimulator class"""
    
    def setUp(self):
        """Set up a fresh simulator instance for each test"""
        self.simulator = PythagoreanSimulator()
    
    def test_calculate_hypotenuse_basic(self):
        """Test basic hypotenuse calculation with 3-4-5 triangle"""
        result = self.simulator.calculate_hypotenuse(3, 4)
        self.assertAlmostEqual(result, 5.0, places=10)
    
    def test_calculate_hypotenuse_another(self):
        """Test hypotenuse calculation with 5-12-13 triangle"""
        result = self.simulator.calculate_hypotenuse(5, 12)
        self.assertAlmostEqual(result, 13.0, places=10)
    
    def test_calculate_hypotenuse_decimal(self):
        """Test hypotenuse calculation with decimal values"""
        result = self.simulator.calculate_hypotenuse(1.5, 2.0)
        expected = math.sqrt(1.5**2 + 2.0**2)
        self.assertAlmostEqual(result, expected, places=10)
    
    def test_calculate_hypotenuse_equal_sides(self):
        """Test hypotenuse calculation with equal sides (isosceles right triangle)"""
        result = self.simulator.calculate_hypotenuse(1, 1)
        self.assertAlmostEqual(result, math.sqrt(2), places=10)
    
    def test_calculate_hypotenuse_negative_a(self):
        """Test that negative value for side a raises ValueError"""
        with self.assertRaises(ValueError):
            self.simulator.calculate_hypotenuse(-3, 4)
    
    def test_calculate_hypotenuse_negative_b(self):
        """Test that negative value for side b raises ValueError"""
        with self.assertRaises(ValueError):
            self.simulator.calculate_hypotenuse(3, -4)
    
    def test_calculate_hypotenuse_zero(self):
        """Test that zero value raises ValueError"""
        with self.assertRaises(ValueError):
            self.simulator.calculate_hypotenuse(0, 4)
    
    def test_calculate_side_basic(self):
        """Test calculating a side from hypotenuse and another side"""
        result = self.simulator.calculate_side(5, 3)
        self.assertAlmostEqual(result, 4.0, places=10)
    
    def test_calculate_side_another(self):
        """Test calculating another side configuration"""
        result = self.simulator.calculate_side(13, 5)
        self.assertAlmostEqual(result, 12.0, places=10)
    
    def test_calculate_side_negative_hypotenuse(self):
        """Test that negative hypotenuse raises ValueError"""
        with self.assertRaises(ValueError):
            self.simulator.calculate_side(-5, 3)
    
    def test_calculate_side_negative_side(self):
        """Test that negative side raises ValueError"""
        with self.assertRaises(ValueError):
            self.simulator.calculate_side(5, -3)
    
    def test_calculate_side_side_larger_than_hypotenuse(self):
        """Test that side larger than hypotenuse raises ValueError"""
        with self.assertRaises(ValueError):
            self.simulator.calculate_side(5, 6)
    
    def test_calculate_side_side_equal_to_hypotenuse(self):
        """Test that side equal to hypotenuse raises ValueError"""
        with self.assertRaises(ValueError):
            self.simulator.calculate_side(5, 5)
    
    def test_verify_right_triangle_345(self):
        """Test verification of 3-4-5 right triangle"""
        result = self.simulator.verify_right_triangle(3, 4, 5)
        self.assertTrue(result)
    
    def test_verify_right_triangle_51213(self):
        """Test verification of 5-12-13 right triangle"""
        result = self.simulator.verify_right_triangle(5, 12, 13)
        self.assertTrue(result)
    
    def test_verify_right_triangle_order_independent(self):
        """Test that verification works regardless of side order"""
        # All permutations should work
        self.assertTrue(self.simulator.verify_right_triangle(3, 4, 5))
        self.assertTrue(self.simulator.verify_right_triangle(3, 5, 4))
        self.assertTrue(self.simulator.verify_right_triangle(4, 3, 5))
        self.assertTrue(self.simulator.verify_right_triangle(4, 5, 3))
        self.assertTrue(self.simulator.verify_right_triangle(5, 3, 4))
        self.assertTrue(self.simulator.verify_right_triangle(5, 4, 3))
    
    def test_verify_right_triangle_not_right(self):
        """Test that non-right triangle is correctly identified"""
        result = self.simulator.verify_right_triangle(2, 3, 4)
        self.assertFalse(result)
    
    def test_verify_right_triangle_negative_side(self):
        """Test that negative side raises ValueError"""
        with self.assertRaises(ValueError):
            self.simulator.verify_right_triangle(-3, 4, 5)
    
    def test_verify_right_triangle_zero_side(self):
        """Test that zero side raises ValueError"""
        with self.assertRaises(ValueError):
            self.simulator.verify_right_triangle(0, 4, 5)
    
    def test_explain_theorem(self):
        """Test that explanation method returns a string"""
        explanation = self.simulator.explain_theorem()
        self.assertIsInstance(explanation, str)
        self.assertIn("PYTHAGOREAN", explanation)
        self.assertIn("a² + b² = c²", explanation)


if __name__ == '__main__':
    unittest.main()
