# Python OOP: Temperature Converter Utility

A clean, modular Python utility showcasing Object-Oriented Programming (OOP) design patterns with **Static Methods (`@staticmethod`)**, stateless architectural design, and string formatting techniques.

---

## 📌 Project Overview

In software design, utility functions often operate independently of instance-specific state. This project models a **Temperature Converter** engine designed to handle multi-directional conversions across **Celsius**, **Fahrenheit**, and **Kelvin** temperature scales.

By leveraging Python's `@staticmethod` decorator, this design avoids unnecessary object instantiation overhead while keeping conversion domain logic encapsulated within a unified namespace.

### Key Highlights:
* **Stateless Design:** No instance attributes (`self`) or class-level mutations (`cls`) required.
* **Encapsulation via Class Namespace:** Logical grouping prevents global namespace pollution.
* **Precise Output Formatting:** Implementation of Python f-string format specifiers (`:.0f`) for readable terminal presentation.

---

## 📐 Mathematical Formulation

The converter implements standard thermodynamic conversion formulas:

| Conversion | Mathematical Formula |
| :--- | :--- |
| **Celsius to Fahrenheit** | $$F = \left(C \times \frac{9}{5}\right) + 32$$ |
| **Fahrenheit to Celsius** | $$C = (F - 32) \times \frac{5}{9}$$ |
| **Celsius to Kelvin** | $$K = C + 273.15$$ |
| **Kelvin to Celsius** | $$C = K - 273.15$$ |

---

## 🚀 Source Code Implementation

```python
class TemperatureConverter:
    """A stateless utility class for converting temperatures between 

    Celsius, Fahrenheit, and Kelvin scales.
    """

    @staticmethod
    def celcius_to_fahrenheit(celcius: float) -> float:
        """Convert temperature from Celsius to Fahrenheit."""
        return (celcius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celcius(fahrenheit: float) -> float:
        """Convert temperature from Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def celcius_to_kelvin(celcius: float) -> float:
        """Convert temperature from Celsius to Kelvin."""
        return celcius + 273.15

    @staticmethod
    def kelvin_to_celcius(kelvin: float) -> float:
        """Convert temperature from Kelvin to Celsius."""
        return kelvin - 273.15


if __name__ == "__main__":
    # Test executions with formatted outputs
    print(f"{TemperatureConverter.celcius_to_fahrenheit(100):.0f}")  # 212
    print(f"{TemperatureConverter.fahrenheit_to_celcius(50):.0f}")   # 10
    print(f"{TemperatureConverter.celcius_to_kelvin(300):.0f}")     # 573
    print(f"{TemperatureConverter.kelvin_to_celcius(200):.0f}")     # -73
```

---

## 🧪 Expected Output

Running the script directly yields the following formatted values:

```text
212
10
573
-73
```

---

## 💡 Architectural Insights for Recruiters

### Why Use `@staticmethod` Instead of Regular Methods or Top-Level Functions?

1. **Memory & Performance Efficiency:**
   * Calling a static method does not require instantiating an object via `tc = TemperatureConverter()`.
   * Python avoids binding an instance reference (`self`) during runtime dispatch.

2. **Domain-Driven Organization (Namespace Management):**
   * Keeping these mathematical routines inside `TemperatureConverter` provides clear semantic context.
   * Prevents collision with third-party libraries or internal modules that might define generic names like `to_celsius()`.

3. **Comparison Matrix:**

| Method Type | First Parameter | Access Scope | Best Use Case |
| :--- | :--- | :--- | :--- |
| **Instance Method** | `self` | Instance-level data (`self.x`) | State-dependent actions |
| **Class Method** | `cls` | Class-level state (`cls.counter`) | Factory patterns, class mutations |
| **Static Method (`@staticmethod`)** | *None* | Arguments passed directly | Pure utility/helper functions |

---

## 🛠️ How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Execute with Python 3:

```bash
python temperature_converter.py
```
