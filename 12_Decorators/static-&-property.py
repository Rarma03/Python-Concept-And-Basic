class Circle:
    def __init__(self, radius):
        self._radius = radius

    # Property to get the radius
    @property
    def radius(self):
        return self._radius

    # Setter to set a new radius
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius can't be negative.")
        self._radius = value

    # Deleter to delete the radius
    @radius.deleter
    def radius(self):
        print("Radius deleted")
        del self._radius

    # Static method to calculate area without needing an object
    @staticmethod
    def area_of_circle(radius):
        return 3.1416 * radius * radius

# with @property we can set a function to a property, and enable that no one can change some values
# we access things like a.radius instead of a.radius()

# ==== Driver Code ====
c = Circle(5)
print("Radius:", c.radius)              # Access property
c.radius = 10                           # Set property
print("Updated Radius:", c.radius)

print("Area using static method:", Circle.area_of_circle(7))  # Static method call

del c.radius                            # Delete property