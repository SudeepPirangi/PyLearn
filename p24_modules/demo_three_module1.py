"""
This is a 1st module

Run this file as "python demo_three_module1.py" from command line
"""

def mock_function():
    """A mock function"""
    print("I'm mocking a module")

print("Demo 3 Module 1 top-level statement")

if __name__ == "__main__":
    print("demo_three_module1 is run directly")
else:
    print("demo_three_module1 is imported")
