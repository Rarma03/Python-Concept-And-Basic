# Global Scope
x = 10  # This variable is in the global scope

def outer_function():
    # Enclosing Scope
    y = 20  # This variable is in the enclosing scope of inner_function

    def inner_function():
        # Local Scope
        z = 30  # This variable is in the local scope of inner_function
        print("Inside inner_function:")
        print(f"z (local): {z}")
        print(f"y (enclosing): {y}")
        print(f"x (global): {x}")

    inner_function()
    print("\nInside outer_function:")
    print(f"y (enclosing): {y}")
    print(f"x (global): {x}")

# Accessing global variable
print("In global scope:")
print(f"x (global): {x}\n")

# Call the outer function
outer_function()

# Demonstrating the LEGB rule
def test_legb():
    # local variable have more priority over global variable if same variable is used
    x = 50  # Local variable
    print("\nInside test_legb:")
    print(f"x (local): {x}")  # Local x takes precedence over global x

test_legb()
print("\nBack in global scope:")
print(f"x (global): {x}")