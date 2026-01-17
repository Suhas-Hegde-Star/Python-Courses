class RomanConverter:
    """Class to convert integers to Roman numerals"""

    def to_roman(self, num):
        """
        Convert an integer to its Roman numeral equivalent

        Args:
            num (int): Integer value to convert (1-3999)

        Returns:
            str: Roman numeral representation
        """
        if not isinstance(num, int) or num <= 0 or num >= 4000:
            raise ValueError("Input must be an integer between 1 and 3999")

        value_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        roman = ""
        for value, numeral in value_map:
            count = num // value
            if count:
                roman += numeral * count
                num -= value * count

        return roman

if __name__ == "__main__":
    converter = RomanConverter()

    try:
        number = int(input("Enter an integer (1-3999): "))
        result = converter.to_roman(number)
        print(f"Roman numeral equivalent: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Invalid input: {e}")