from main import grade_to_point, calculate_sgpa


assert grade_to_point('O') == 10
assert grade_to_point('A+') == 9
assert grade_to_point('A') == 8
assert grade_to_point('B+') == 7
assert grade_to_point('B') == 6
assert grade_to_point('C') == 5
assert grade_to_point('F') == 0
assert grade_to_point('Invalid') == 0  # Test invalid input


grades = [10, 9, 8]
credits = [3, 3, 4]
assert calculate_sgpa(grades, credits) == 8.9


grades = [7, 8, 10]
credits = [2, 2, 4]
assert calculate_sgpa(grades, credits) == 8.5

print("✅ All tests passed successfully!")
