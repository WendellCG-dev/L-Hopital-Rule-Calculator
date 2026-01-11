# L'Hôpital's Rule Calculator

A Python-based graphical calculator that automates **L'Hôpital's Rule** to find the limits of indeterminate forms ($0/0$ or $\infty/\infty$).

Built using **Tkinter** for the interface and **SymPy** for symbolic mathematics.

---

## Preview

---

## Features

- **Symbolic Differentiation:** Calculates actual derivatives of functions.
- **Support for Constants:** Handles $e$ (Euler's number), $\pi$ (pi), and $\infty$ (infinity as `oo`).
- **Timing:** Displays exactly how long the math evaluation took in seconds.

## Installation

1. Clone this repository or download the files.
2. Install the necessary dependencies:
   ```
   pip install -r requirements.txt
   ```

Math Syntax Guide To Ensure The Calculator Understands Your Input, Use Standard Python Math Notation:

| Concept            | Syntax                    | Example             |
| :----------------- | :------------------------ | :------------------ |
| **Exponents**      | `**`                      | `x**2` for $x^2$    |
| **Multiplication** | `*`                       | `2*x` for $2x$      |
| **Trig Functions** | `sin()`, `cos()`, `tan()` | `sin(x)`            |
| **Exponentials**   | `exp(x)` or `e**x`        | $e^x$               |
| **Infinity**       | `oo`                      | Represents $\infty$ |

How It Works: The program follows the formal definition of L'Hôpital's Rule:It takes the string input for $f(x)$ (numerator) and $g(x)$ (denominator).It uses sympy.diff() to find $f'(x)$ and $g'(x)$.It then calculates the limit of $\frac{f'(x)}{g'(x)}$ as $x \to c$ using sympy.limit().

Project Background: Developed This Project During High School For A School Project, To Connect My Math Class And My Interest In Python. It Was A Great Way To Learn About Symbolic Math Libraries And GUI Development.
