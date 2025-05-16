import math
import sys
import re

def is_palindromeable(char_map: dict) -> bool:
    """
    Check if a string with a wild card (?) can be rearranged to form a palindrome.
    """
    odd_count = sum(value["odd"] for key, value in char_map.items() if key != '?')
    if odd_count > (char_map['?']['count'] + 1) :
        return False
    return True

def generate_char_map(candidate: str) -> dict:
    """
    Create a map of characters that counts them and finds the odd ones.
    """
    char_map = { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }
    characters = sorted(candidate)
    for char in characters:
        count = candidate.count(char)
        char_map[char] = {
            "count" : count,
            "odd" : (count % 2)
        }

    return char_map

def even_out_char_map(char_map: dict) -> dict:
    """
    Even out the character map by pairing odd characters with wildcards.
    """
    if char_map["?"]["count"] > 0 and sum(value["odd"] for key, value in char_map.items() if key != '?') > 0:
        for char, value in char_map.items():
            if char != '?' and value["odd"] == 1:
                char_map[char]["count"] += 1
                char_map[char]["odd"] = 0
                char_map["?"]["count"] -= 1
                char_map["?"]["odd"] = char_map["?"]["count"] % 2
                if char_map["?"]["count"] == 0:
                    break

    return char_map

def replace_remaining_wildcards(char_map: dict) -> dict:
    """
    Replace remaining wildcards with 'a' to form a palindrome.
    """
    if char_map["?"]["count"] > 0:
        char_map["a"]["count"] += (char_map["?"]["count"])
        char_map["a"]["odd"] = (char_map["a"]["count"] % 2)
    del char_map["?"]

    return char_map

def convert_char_map_to_palindrome(char_map: dict) -> str:
    """
    Convert the character map to a palindrome.
    """
    first_half = ''
    odd_char = ''
    for char, value in char_map.items():
        first_half += char * math.floor(value["count"] // 2)
        odd_char += char * value["odd"]

    result = first_half + odd_char + first_half[::-1]

    return result

def process_candidate(char_map: dict) -> str:
    """
    Rearrange the candidate to form a palindrome.
    """
    char_map = even_out_char_map(char_map)
    char_map = replace_remaining_wildcards(char_map)
    result   = convert_char_map_to_palindrome(char_map)

    return result    

def get_palindrome(candidate: str):
    """
    Get a palindrome from the candidate string if possible.
    """
    char_map = generate_char_map(candidate)

    if is_palindromeable(char_map) == True:
        result = process_candidate(char_map)
        print(f"Your palindrome is {result}.")
    else:
        print(f"{candidate} cannot be a palindrome.")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not re.match('^[a-z?]+$', sys.argv[1]):
        print("Usage: python palindrome.py <candidate>")
        print("Candidate must be a string of lowercase letters and wildcards (?)")
    else:
        get_palindrome(candidate=sys.argv[1])