from byte import Byte
from bit import Bit

class CPU:
    def __init__(self, frequency: int = 100, cache_size: int = 16):
        self.debug = []

        self.frequency = frequency
        self.cache_size = cache_size

        self.cache = []

    def __repr__(self):
        cls = type(self).__name__
        return (
            f"{cls}(frequency={self.frequency!r}, "
            f"cache_size={self.cache_size!r}, "
            f"cache_len={len(self.cache)})"
        )
    
cpu = CPU(100, 16)
print(cpu)

byte = Byte([Bit(0), Bit(0), Bit(0), Bit(0), Bit(1), Bit(1), Bit(0), Bit(1)])
print(byte)

byte = Byte("00001101")
print(byte)

byte = Byte(13)
print(byte)