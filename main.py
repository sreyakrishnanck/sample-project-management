# main.py
# Simple Student Grade Calculator
# Author: Sreya Krishnan

def calculate_sgpa(grades, credits):
    """Calculate SGPA from given grades and credits."""
    total_points = 0
    total_credits = 0
    for g, c in zip(grades, credits):
        total_points += g * c
        total_credits += c
    return round(total_points / total_credits, 2)

def grade_to_point(grade):
    """Convert letter grade to grade point."""
    mapping = {
        'O': 10,  # Outstanding
        'A+': 9,
        'A': 8,
        'B+': 7,
        'B': 6,
        'C': 5,
        'F': 0   # Fail
    }
    return mapping.get(grade.upper(), 0)

def main():
    print("🎓 STUDENT GRADE CALCULATOR 🎓")
    n = int(input("Enter number of subjects: "))

    grades = []
    credits = []

    for i in range(n):
        print(f"\nSubject {i+1}")
        grade = input("Enter grade (O/A+/A/B+/B/C/F): ")
        credit = int(input("Enter credit for this subject: "))

        grades.append(grade_to_point(grade))
        credits.append(credit)

    sgpa = calculate_sgpa(grades, credits)
    percentage = round((sgpa - 0.75) * 10, 2)

    print("\n📊 RESULTS 📊")
    print(f"SGPA: {sgpa}")
    print(f"Percentage: {percentage}%")

if __name__ == "__main__":
    main()

