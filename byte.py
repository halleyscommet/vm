from bit import Bit

class Byte:
    def __init__(self, bits: list[Bit] | int | str):
        if isinstance(bits, list):
            for bit in bits:
                if not isinstance(bit, Bit):
                    raise TypeError("list must be only bits")
            if len(bits) != 8:
                raise ValueError("a list of bits must have a length of 8")
            # b = bits
            b = bits.copy()
        elif isinstance(bits, int):
            if bits < 0 or bits > 255:
                raise ValueError("out of range for a byte")
            b = []
            while bits > 0:
                b.append(Bit(bits & 1))
                bits //= 2
            while len(b) != 8:
                b.append(Bit(0))
            b.reverse()
        elif isinstance(bits, str):
            if len(bits) != 8:
                raise ValueError("a string containing bits must have a length of 8")
            for char in bits:
                if char != '0' and char != '1':
                    raise ValueError("string must contain only '0' or '1'")
            b = []
            for bit in bits:
                b.append(Bit(int(bit)))
        else:
            raise TypeError("a byte can only be represented as a list of bits, an int, or a string")

        self.bits: list[Bit] = b

    def __repr__(self):
        cls = type(self).__name__
        return f"{cls}(bits={self.bits!r})"