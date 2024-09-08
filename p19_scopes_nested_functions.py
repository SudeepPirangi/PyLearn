"""
Demonstrates scopes with nested functions and also about "global" keyword
"""

print("\nScopes")

# global namespace
name = "global"

def manipulator():
    """Scope manipulator"""
    # enclosing namespace
    # name = "enclosing"

    def local_boy():
        """Local function"""
        # name = "local"
        print(f"I am from {name}")

    local_boy()

manipulator()

print("\nGlobal")

x = 50

def global_demo():
    """Demos global keyword"""
    global x
    print("Currently x is", x)
    x = "reassigned"
    print("x became", x)

global_demo()
print("Printing x from outside function as", x)
