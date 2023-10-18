def calculate_grade(maths, physics, geo, chem):
    # Check for negative values or values greater than 100
    if any(mark < 0 or mark > 100 for mark in [maths, physics, geo, chem]):
        return "Unrecognized marks/avg"

    # Calculate the average
    avg = (maths + physics + geo + chem) / 4

    # Determine the grade based on the average
    if 0 <= avg <= 30:
        return 'D'
    elif 31 <= avg <= 50:
        return 'C'
    elif 51 <= avg <= 70:
        return 'B'
    elif 71 <= avg <= 100:
        return 'A'

    return "Unrecognized marks/avg"


# Input marks for each subject
maths = float(input("Enter math marks: "))
physics = float(input("Enter physics marks: "))
geo = float(input("Enter geography marks: "))
chem = float(input("Enter chemistry marks: "))

# Calculate and print the grade
result = calculate_grade(maths, physics, geo, chem)
print("Grade:", result)