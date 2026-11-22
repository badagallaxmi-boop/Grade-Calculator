def average(marks):
    return sum(marks) / len(marks)


def grade(avg):
    if avg >= 90:
        return "A+"
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 40:
        return "D"
    return "F"


def is_pass(marks):
    return all(m >= 40 for m in marks)


marks = [76, 89, 90]

avg = average(marks)
print("Marks  :", marks)
print(f"Average: {avg:.2f}")
print("Grade  :", grade(avg))
print("Result :", "PASS" if is_pass(marks) else "FAIL") 
