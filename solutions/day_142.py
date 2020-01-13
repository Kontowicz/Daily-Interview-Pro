def create_palindrome(s):
    def is_palindrome(string):
        return string == string[::-1]
    def remove_character(string, character):
        to_return = ''
        for item in string:
            if item != character:
                to_return += item
        return to_return

    characters = list(set(list(s)))
    tmp = [is_palindrome(remove_character(s,x)) for x in characters]
    return True in tmp

assert create_palindrome("abcdcbea") == True
assert create_palindrome("abccba") == True
assert create_palindrome("abccaa") == False

print(create_palindrome("abcdcbea"))
print(create_palindrome("abccba"))
print(create_palindrome("abccaa"))

print('Test pass.')