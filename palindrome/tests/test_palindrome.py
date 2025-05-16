import src.palindrome as palindrome



def test_get_character_map_empty():
    candidate = ""
    assert palindrome.get_characters(candidate) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }
def test_get_character_map_simple():
    candidate = "a"
    assert palindrome.get_characters(candidate) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 1, "odd" : 1 } }
def test_get_character_map_simple_two():
    candidate = "aa"
    assert palindrome.get_characters(candidate) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 2, "odd" : 0 } }
def test_get_character_map_simple_three():
    candidate = "aaa"
    assert palindrome.get_characters(candidate) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 3, "odd" : 1 } }
def test_get_character_map_even():
    candidate = "aabb"
    assert palindrome.get_characters(candidate) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 2, "odd" : 0 }, 'b' : { "count" : 2, "odd" : 0 } }
def test_get_character_map_odd():
    candidate = "aabbc"
    assert palindrome.get_characters(candidate) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 2, "odd" : 0 }, 'b' : { "count" : 2, "odd" : 0 }, 'c' : { "count" : 1, "odd" : 1 } }
def test_get_character_map_wildcard():
    candidate = "a?b"
    assert palindrome.get_characters(candidate) == { '?' : { "count" : 1, "odd" : 1 }, 'a' : { "count" : 1, "odd" : 1 }, 'b' : { "count" : 1, "odd" : 1 } }
def test_get_character_map_wildcard_two():
    candidate = "a??b"
    assert palindrome.get_characters(candidate) == { '?' : { "count" : 2, "odd" : 0 }, 'a' : { "count" : 1, "odd" : 1 }, 'b' : { "count" : 1, "odd" : 1 } }

def test_is_palindromeable_simple():
    candidate = "a"
    characters = palindrome.get_characters(candidate)
    assert palindrome.is_palindromeable(characters) == True
def test_is_palindromeable_even():
    candidate = "abba"
    characters = palindrome.get_characters(candidate)
    assert palindrome.is_palindromeable(characters) == True
def test_is_palindromeable_odd():
    candidate = "racecar"
    characters = palindrome.get_characters(candidate)
    assert palindrome.is_palindromeable(characters) == True
def test_is_palindromeable_not():
    candidate = "hello"
    characters = palindrome.get_characters(candidate)
    assert palindrome.is_palindromeable(characters) == False
def test_is_palindromeable_empty():
    candidate = ""
    characters = palindrome.get_characters(candidate)
    assert palindrome.is_palindromeable(characters) == True
def test_is_palindromeable_wildcard_simple_two_odds():
    candidate = 'ab?'
    characters = palindrome.get_characters(candidate)
    assert palindrome.is_palindromeable(characters) == True
def test_is_palindromeable_wildcard_simple_one_odd_one_even():
    candidate = 'abb?'
    characters = palindrome.get_characters(candidate)
    assert palindrome.is_palindromeable(characters) == True
def test_is_palindromeable_wildcard_two_odds():
    candidate = 'abbb?'
    characters = palindrome.get_characters(candidate)
    assert palindrome.is_palindromeable(characters) == True
def test_is_palindromeable_wildcard_three_odds_two_wilds():
    candidate = 'abc??'
    characters = palindrome.get_characters(candidate)
    assert palindrome.is_palindromeable(characters) == True
def test_is_palindromeable_wildcard_four_odds_two_wilds():
    candidate = 'a?bc?d'
    characters = palindrome.get_characters(candidate)
    assert palindrome.is_palindromeable(characters) == False

def test_get_palindrome_trivial():
    candidate = "a"
    characters = palindrome.get_characters(candidate)
    assert palindrome.get_palindrome(characters) == "a"
def test_get_palindrome_simple_rearrange():
    candidate = "aabb"
    characters = palindrome.get_characters(candidate)
    assert palindrome.get_palindrome(characters) == "abba"
def test_get_palindrome_rearrange_three_way():
    candidate = "caabb"
    characters = palindrome.get_characters(candidate)
    assert palindrome.get_palindrome(characters) == "abcba"
def test_get_palindrome_rearrange_many_ways():
    candidate = "cfbe?gdgaed?cgafbffb"
    characters = palindrome.get_characters(candidate)
    assert palindrome.get_palindrome(characters) == "abbcdeffggggffedcbba"
def test_get_palindrome_rearrange_wildcard():
    candidate = "a?b?c"
    characters = palindrome.get_characters(candidate)
    assert palindrome.get_palindrome(characters) == "abcba"
def test_get_palindrome_rearrange_wildcard_many():
    candidate = "b???"
    characters = palindrome.get_characters(candidate)
    assert palindrome.get_palindrome(characters) == "abba"
def test_get_palindrome_rearrange_wildcard_only():
    candidate = "????"
    characters = palindrome.get_characters(candidate)
    assert palindrome.get_palindrome(characters) == "aaaa"


def test_even_out_characters_simple():
    characters = { '?' : { "count" : 1, "odd" : 1 }, 'a' : { "count" : 1, "odd" : 1 } }
    assert palindrome.even_out_characters(characters) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 2, "odd" : 0 } }
def test_even_out_characters_simple_two():
    characters = { '?' : { "count" : 1, "odd" : 1 }, 'a' : { "count" : 2, "odd" : 0 } }
    assert palindrome.even_out_characters(characters) == { '?' : { "count" : 1, "odd" : 1 }, 'a' : { "count" : 2, "odd" : 0 } }
def test_even_out_characters_wildcard_only():
    characters = { '?' : { "count" : 2, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }
    assert palindrome.even_out_characters(characters) == { '?' : { "count" : 2, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }

def test_replace_remaining_wildcards_simple():
    characters = { '?' : { "count" : 1, "odd" : 1 }, 'a' : { "count" : 0, "odd" : 0 } }
    assert palindrome.replace_remaining_wildcards(characters) == { 'a' : { "count" : 1, "odd" : 1 } }
def test_replace_remaining_wildcards_simple_two():
    characters = { '?' : { "count" : 2, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }
    assert palindrome.replace_remaining_wildcards(characters) == { 'a' : { "count" : 2, "odd" : 0 } }
def test_replace_remaining_wildcards_none():
    characters = { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }
    assert palindrome.replace_remaining_wildcards(characters) == { 'a' : { "count" : 0, "odd" : 0 } }

def test_convert_characters_to_palindrome_simple():
    characters = { 'a' : { "count" : 2, "odd" : 0 } }
    assert palindrome.convert_characters_to_palindrome(characters) == "aa"
def test_convert_characters_to_palindrome_simple_two():
    characters = { 'a' : { "count" : 2, "odd" : 0 }, 'b' : { "count" : 2, "odd" : 0 } }
    assert palindrome.convert_characters_to_palindrome(characters) == "abba"
def test_convert_characters_to_palindrome_odd():
    characters = { 'a' : { "count" : 3, "odd" : 1 }, 'b' : { "count" : 2, "odd" : 0 } }
    assert palindrome.convert_characters_to_palindrome(characters) == "ababa"