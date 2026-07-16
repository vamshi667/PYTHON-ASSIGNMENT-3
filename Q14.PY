# 14(a) Print all content
with open("student.txt", "r") as f:
    content = f.read()
    print(content)

# 14(b) Print line-by-line
with open("student.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"Line {i}: {line.strip()}")
