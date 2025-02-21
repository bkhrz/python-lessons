import math

class Vector:
    def __init__(self, *args):
        """Initializes vector with any number of dimensions"""
        if not args:
            raise ValueError('You did not enter any components!')
        self.components = list(args)

    def __repr__(self):
        """Represents vector in string format"""
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        """Adds vectors"""
        if len(self.components) != len(other.components):
            raise ValueError('Each vector must have same number of components')
        return Vector(*(a+b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        """Subtracts vectors"""
        if len(self.components) != len(other.components):
            raise ValueError('Each vector must have same number of components')
        return Vector(*(a-b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        """Multiplies vectors"""
        if isinstance(other, Vector):    # Dot product
            if len(self.components) != len(other.components):
                raise ValueError('Each vector must have same number of components')
            return sum(a*b for a,b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):  #Scalar product
            return Vector(*(a*other for a in self.components))
        else:
            raise TypeError('Multiplication is only supported with vectors and scalars')

    def __rmul__(self, other):
        """Handles scalar multp when the scalar is on the left"""
        return self.__mul__(other)

    def magnitude(self):
        """Calculates magnitude of the vector"""
        return math.sqrt(sum(a**2 for a in self.components))

    def normalize(self):
        """Normalizes the vector"""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError('Zero vector cannot be normalized')
        return Vector(*(a/mag for a in self.components))

# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)

# Addition
v3 = v1 + v2
print(v3)

# Subtraction
v4 = v2 - v1
print(v4)

# Dot product
dot_product = v1 * v2
print(dot_product)

# Scalar multiplication
v5 = 3 * v1
print(v5)

# Magnitude
print(v1.magnitude())

# Normalization
v_unit = v1.normalize()
print(v_unit)