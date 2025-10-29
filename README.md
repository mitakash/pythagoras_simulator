# Pythagorean Theorem Simulator

An educational tool to help understand the Pythagorean Theorem through interactive simulations and visual representations.

## What is the Pythagorean Theorem?

The Pythagorean Theorem states that in a right triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides.

**Formula:** `a² + b² = c²`

Where:
- `a` and `b` are the two shorter sides (legs)
- `c` is the longest side (hypotenuse)

## Features

- 📐 **Calculate Hypotenuse**: Given two sides, calculate the hypotenuse
- 📏 **Calculate Side**: Given the hypotenuse and one side, calculate the other side
- ✓ **Verify Right Triangle**: Check if three sides form a right triangle
- 📚 **Educational Explanations**: Learn about the theorem with clear explanations
- 🎨 **Visual Representations**: See the theorem in action with graphical visualizations

## Installation

1. Clone this repository:
```bash
git clone https://github.com/mitakash/pythagoras_simulator.git
cd pythagoras_simulator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Command-Line Simulator

Run the interactive simulator for a text-based experience:

```bash
python pythagoras_simulator.py
```

This will present you with a menu:
- Calculate hypotenuse from two sides
- Calculate a side given hypotenuse and another side
- Verify if three sides form a right triangle
- Learn about the Pythagorean theorem
- Exit

### Visual Simulator

Run the visual simulator to see graphical representations:

```bash
python visual_simulator.py
```

This will show visual proofs with squares drawn on each side of the triangle, demonstrating how `a² + b² = c²` works geometrically.

### Using in Your Code

```python
from pythagoras_simulator import PythagoreanSimulator

# Create a simulator instance
sim = PythagoreanSimulator()

# Calculate hypotenuse
c = sim.calculate_hypotenuse(3, 4)
print(f"Hypotenuse: {c}")  # Output: 5.0

# Calculate a side
b = sim.calculate_side(5, 3)
print(f"Side: {b}")  # Output: 4.0

# Verify right triangle
is_right = sim.verify_right_triangle(3, 4, 5)
print(f"Is right triangle: {is_right}")  # Output: True
```

### Visual Simulator in Code

```python
from visual_simulator import VisualPythagoreanSimulator

# Create a visual simulator
visual_sim = VisualPythagoreanSimulator()

# Visualize a 3-4-5 triangle with squares
visual_sim.visualize_triangle(3, 4, show_squares=True)

# Create a visual proof
visual_sim.visualize_proof(3, 4)
```

## Examples

### Classic Right Triangles

1. **3-4-5 Triangle**: `3² + 4² = 5²` → `9 + 16 = 25` ✓
2. **5-12-13 Triangle**: `5² + 12² = 13²` → `25 + 144 = 169` ✓
3. **8-15-17 Triangle**: `8² + 15² = 17²` → `64 + 225 = 289` ✓

## Running Tests

Run the unit tests to verify the implementation:

```bash
python -m unittest test_pythagoras_simulator.py
```

Or with verbose output:

```bash
python -m unittest test_pythagoras_simulator.py -v
```

## Educational Value

This simulator is designed to help students understand:
- The relationship between the sides of a right triangle
- How the theorem can be used to find unknown sides
- Visual proof of why the theorem works
- Practical applications of the Pythagorean Theorem

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Author

Created with ❤️ to help students understand mathematics better.
