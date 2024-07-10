def roman_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    roman = roman.upper()
    for char in roman:
        if char not in roman_dict:
            return "Invalid Roman numeral"
        current_value = roman_dict[char]
        if current_value > prev_value:
            total = total - 2 * prev_value + current_value
        else:
            total += current_value
        prev_value = current_value
    return total

roman_numeral = input("Enter a Roman numeral: ")
result = roman_to_int(roman_numeral)
print(f"The integer value of '{roman_numeral}' is: {result}")
