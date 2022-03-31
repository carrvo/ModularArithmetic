"""
"""

class Congruence(object):
    """
    """

    def __init__(self, value, modulus):
        modulus = abs(modulus)
        self.remainder = value % modulus
        self.modulus = modulus

    def __repr__(self):
        return repr(tuple([self.remainder, self.modulus]))

    def __str__(self):
        return f'{self.remainder} (mod {self.modulus})'

    def value(self, q):
        """
        x = q * m + r
        """
        return q * self.modulus + self.remainder

    def __eq__(self, other):
        if not isinstance(other, Congruence):
            other = Congruence(other, self.modulus)
        return (self.modulus == other.modulus and
                self.remainder == other.remainder)

    def __add__(self, other):
        if not isinstance(other, Congruence):
            other = Congruence(other, self.modulus)
        if other.modulus == self.modulus:
            return Congruence(self.remainder + other.remainder, self.modulus)
        else:
            raise ValueError(f"modulus {other.modulus} from {type(other)}" +
                             f"differs against {self.modulus} from {type(self)}")

    __radd__ = __add__

    def __sub__(self, other):
        if not isinstance(other, Congruence):
            other = Congruence(other, self.modulus)
        if other.modulus == self.modulus:
            return Congruence(self.remainder - other.remainder, self.modulus)
        else:
            raise ValueError(f"modulus {other.modulus} from {type(other)}" +
                             f"differs against {self.modulus} from {type(self)}")

    __rsub__ = __sub__

    def __mul__(self, other):
        if not isinstance(other, Congruence):
            other = Congruence(other, self.modulus)
        if other.modulus == self.modulus:
            return Congruence(self.remainder * other.remainder, self.modulus)
        else:
            raise ValueError(f"modulus {other.modulus} from {type(other)}" +
                             f"differs against {self.modulus} from {type(self)}")

    __rmul__ = __mul__

    @property
    def Reflexive(self):
        return True

    @property
    def Symmetrical(self):
        return True

    @property
    def Transitive(self):
        return True
