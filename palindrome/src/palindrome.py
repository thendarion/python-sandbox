import math
import sys
import re
import os

def is_palindromeable(characters: dict) -> bool:
    """
    Check if a string with a wild card (?) can be rearranged to form a palindrome.
    """
    odd_count = sum(stats["odd"] for char, stats in characters.items() if char != '?')
    if odd_count > (characters['?']['count'] + 1) :
        return False
    return True

def get_characters(candidate: str) -> dict:
    """
    Create a map of characters that counts them and finds the odd ones.
    """
    characters = { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }
    for char in sorted(candidate):
        count = candidate.count(char)
        characters[char] = {
            "count" : count,
            "odd" : (count % 2)
        }

    return characters

def even_out_characters(characters: dict) -> dict:
    """
    Even out the character map by pairing odd characters with wildcards.
    """
    if characters["?"]["count"] > 0 and sum(stats["odd"] for char, stats in characters.items() if char != '?') > 0:
        for char, stats in characters.items():
            if stats["odd"] == 1:
                characters[char]["count"] += 1
                characters[char]["odd"] = 0
                characters["?"]["count"] -= 1
                characters["?"]["odd"] = characters["?"]["count"] % 2
                if characters["?"]["count"] == 0:
                    break

    return characters

def replace_remaining_wildcards(characters: dict) -> dict:
    """
    Replace remaining wildcards with 'a' to form a palindrome.
    """
    if characters["?"]["count"] > 0:
        characters["a"]["count"] += (characters["?"]["count"])
        characters["a"]["odd"] = (characters["a"]["count"] % 2)
    del characters["?"]

    return characters

def convert_characters_to_palindrome(characters: dict) -> str:
    """
    Convert the character map to a palindrome.
    """
    first_half = ''
    odd_char = ''
    for char, stats in characters.items():
        first_half += char * math.floor(stats["count"] // 2)
        odd_char += char * stats["odd"]

    palindrome = first_half + odd_char + first_half[::-1]

    return palindrome

def get_palindrome(characters: dict) -> str:
    """
    Rearrange the candidate to form a palindrome.
    """
    characters = even_out_characters(characters)
    characters = replace_remaining_wildcards(characters)
    palindrome   = convert_characters_to_palindrome(characters)

    return palindrome    

def palindrome(candidate: str):
    """
    Get a palindrome from the candidate string if possible.
    """
    characters = get_characters(candidate)

    if is_palindromeable(characters) == True:
        palindrome = get_palindrome(characters)
        print(f"Your palindrome is {palindrome}.")
    else:
        print(f"{candidate} cannot be a palindrome.")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not re.match('^[a-z?]+$', sys.argv[1]):
        print("Usage: python " + os.path.basename(__file__) + " <candidate>")
        print("Candidate must be a string of lowercase letters and wildcards (?)")
    else:
        palindrome(candidate=sys.argv[1])
