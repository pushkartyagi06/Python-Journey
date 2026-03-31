marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
    print("Excellent 🔥")
elif marks >= 75:
    print("Grade: A")
    print("Very Good 👍")
elif marks >= 60:
    print("Grade: B")
    print("Good 🙂")
elif marks >= 50:
    print("Grade: C")
    print("Average 😐")
else:
    print("Grade: F")
    print("Fail ❌")