def introduce(name, age=None):
    if age is not None:
        print(f"My name is {name}. I am {age} years old.")
    else:
        print(f"My name is {name}. My age is secret.")
introduce("John", 20)
introduce("John")
