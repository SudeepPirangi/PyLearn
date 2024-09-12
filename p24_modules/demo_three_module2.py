"""
This is a 2nd module

Run this file as "python demo_three_module2.py" from command line
"""

import demo_three_module1

demo_three_module1.mock_function()

def mock_function():
    """A mock function"""
    print("I'm mocking a 2nd module")

print("Demo 3 Module 2 top-level statement")

if __name__ == "__main__":
    print("demo_three_module2 is run directly")
else:
    print("demo_three_module2 is imported")
