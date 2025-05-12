# Example to explain closure in Python

def outer_function(outer_variable):
    
    def inner_function(inner_variable):
        return f"Outer Variable: {outer_variable}, Inner Variable: {inner_variable}"
    
    return inner_function

# Create a closure
closure_function = outer_function("Hello")

# Call the closure with an argument
result = closure_function("World")
print(result)

# Explanation:
# - `outer_function` defines a local variable `outer_variable`.
# - `inner_function` uses `outer_variable` from the enclosing scope.
# - When `outer_function` is called, it returns `inner_function`, which retains access to `outer_variable`.
# - This retained access to the enclosing scope's variable is called a closure.