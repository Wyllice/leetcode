#17 Letter Combinations of a Phone Number
def letterCombinations(self, digits: str) -> List[str]:
    # Digit Map
    d = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl",
    '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
    # Trivial case
    if not digits:
        return []
    # Initialize list of all letter combinations
    combos = [""]
    # Iterates through each digit
    for digit in digits:
        #Get possible letters from map
        letters = d[digit]
        # Concatenates each possible letter for current digit to all possible prefixes
        # stored in combos and overwrites to combos all new possible combinations
        combos = [prefix+letter for prefix in combos for letter in letters]
    # Return list of all letter combinations
    return combos
