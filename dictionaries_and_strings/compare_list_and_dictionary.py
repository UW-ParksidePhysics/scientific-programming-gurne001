code_snippets = {"numbers = {}\nnumbers[0] = -5\nnumbers[1] = 10.5": 'This code works as the numbers item is initialized as a dictionary',
                 "other_numbers = []\nother_numbers[0] = -5\nother_numbers[1] = 10.5": 'This code fails as the other_numbers item is an empty list and thus has no valid elements to replace',
                 "other_numbers = []\nother_numbers.append(-5)\nother_numbers.append(10.5)": 'This code works as it is now appending values to empty list, not referencing non-existant values'}

for key in code_snippets:
    print(key)
    print(code_snippets[key])
    print("\n")