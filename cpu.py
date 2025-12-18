from byte import Byte

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
    
cpu = CPU(100, 256)
print(cpu)

byte = Byte(13)
print(byte)
print(repr(byte))
print(str(byte))
print(int(byte))