class Bit(int):
    def __new__(cls, value: int | bool | str):
        if isinstance(value, bool):
            v = 1 if value else 0
        elif isinstance(value, int):
            if value not in (0, 1):
                raise ValueError("int bit must be 0 or 1")
            v = value
        elif isinstance(value, str):
            if value not in ("0", "1"):
                raise ValueError("str bit must be '0' or '1'")
            v = int(value)
        else:
            raise TypeError("value must be an int, bool, or '0'/'1' string")

        return int.__new__(cls, v)

    def __repr__(self):
        cls = type(self).__name__
        return f"{cls}({int(self)})"