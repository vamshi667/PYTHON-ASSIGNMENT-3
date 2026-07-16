try:
    with open("student.txt", "x") as f:
        f.write("Python is easy to learn.\n")
        f.write("File handling is important.\n")
        f.write("Practice makes perfect.\n")
    print("File created and written successfully.")
except FileExistsError:
    print("Error: student.txt already exists.")
except Exception as e:
    print(f"An error occurred: {e}")
