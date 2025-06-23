my_var = input("Enter a sentence: ")
vowels = "aeiouAEIOU"

vowel_count = sum(my_var.count(v) for v in vowels)

print(f"Total vowels: {vowel_count}")
