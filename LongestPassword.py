# https://app.codility.com/programmers/trainings/1/longest_password/

'''
You would like to set a password for a bank account. However, there are three restrictions on the format of the password:
        it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
        there should be an even number of letters;
        there should be an odd number of digits.

You are given a string S consisting of N characters. String S can be divided into words by splitting it at, and removing, the spaces.
The goal is to choose the longest word that is a valid password.
You can assume that if there are K spaces in string S then there are exactly K + 1 words.
'''

# For example, given "test 5 a0A pass007 ?xy1",
S = "test 5 a0A pass007 ?xy1"
# there are five words
words = S.split()
print("\n Words: ", words)
print("\n Length: ", len(words))

def contains_alphanumerical(word: str):
    return word.isalnum()

def even_len_characters(word: str):
    return (sum(c.isalpha() for c in word) % 2 == 0)

def odd_len_digits(word: str):
    return (sum(c.isdigit() for c in word) % 2 != 0)

# and three of them are valid passwords:
valid_passwords = [word for word in words if (contains_alphanumerical(word)) and (even_len_characters(word)) and (odd_len_digits(word))]
print("\n Valid Passwords: ", valid_passwords)

# Longest password:
print("\n Longest password: ", max(valid_passwords, key=len))

def solution(S):
    if (S!='') and (len(S)>=1) and (len(S)<=200):
        words = S.split()

        def contains_alphanumerical(word: str):
            return word.isalnum()

        def even_len_characters(word: str):
            return (sum(c.isalpha() for c in word) % 2 == 0)

        def odd_len_digits(word: str):
            return (sum(c.isdigit() for c in word) % 2 != 0)

        valid_passwords = [word for word in words if
                           (contains_alphanumerical(word)) and (even_len_characters(word)) and (odd_len_digits(word))]

        longest = max(valid_passwords, key=len)

        return len(longest)
    else:
        return -1

print("\n Solution: ", solution(S))
