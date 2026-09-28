print("=" * 70)
print("Example 2: str to int")
print("=" * 70)
print()

age_txt = input("Enter your age ")
print(f"Type of age txt:===== {type(age_txt)}")
print(f"Value of age txt:==== '{age_txt}'")
print()

age = int(age_txt)
print(f"Type of age:========= {type(age)}")
print(f"Value of age:======== {age}")
print()

next_year_age = age + 1
print(f"Next year you will be: {next_year_age}")