import math
import sys

def is_palindromeable(candidate: str) -> bool:
    """
    Check if a string with a wild card (?) can be rearranged to form a palindrome.
    """
    char_map = { '?' : { "count" : 0, "odd" : 0 } }
    characters = sorted(candidate)
    for char in characters:
        count = candidate.count(char)
        char_map[char] = {
            "count" : count,
            "odd" : (count % 2)
        }
    odd_count = sum(value["odd"] for key, value in char_map.items() if key != '?')
    if odd_count > (char_map['?']['count'] + 1) :
        return False
    return True

def process_candidate(candidate: str) -> str:
    """
    Rearrange the string to form a palindrome.
    """
    char_map = { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }
    characters = sorted(candidate)
    for char in characters:
        count = candidate.count(char)
        char_map[char] = {
            "count" : count,
            "odd" : (count % 2)
        }

    for char, value in char_map.items():
        if char != '?' and value["odd"] == 1:
            if char_map["?"]["count"] > 0:
                char_map[char]["count"] += 1
                char_map[char]["odd"] = 0
                char_map["?"]["count"] -= 1

    if char_map["?"]["count"] > 0:
        char_map["a"]["count"] += (char_map["?"]["count"])
        char_map["a"]["odd"] = (char_map["a"]["count"] % 2)
        char_map["?"]["count"] = 0
        char_map["?"]["odd"] = 0

    result = ''
    print(char_map)
    for char, value in char_map.items():
        if value["count"] > 0:
            result += char * math.floor(value["count"] // 2)

    odd_char = ''
    for char, value in char_map.items():
        if value["odd"] == 1:
            odd_char = char
            break
    result = result + odd_char + result[::-1]

    return result    

def get_palindrome(candidate: str):
    if is_palindromeable(candidate) == True:
        result = process_candidate(candidate)
        print(f"Your palindrome is {result}.")
    else:
        print(f"{candidate} cannot be a palindrome.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_palindrome.py <candidate>")
    else:
        get_palindrome(candidate=sys.argv[1])