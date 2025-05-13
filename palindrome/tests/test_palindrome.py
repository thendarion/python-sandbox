import palindrome.get_palindrome as get_palindrome



def test_get_character_map_empty():
    candidate = ""
    assert get_palindrome.generate_char_map(candidate) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }
def test_get_character_map_simple():
    candidate = "a"
    assert get_palindrome.generate_char_map(candidate) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 1, "odd" : 1 } }
def test_get_character_map_simple_two():
    candidate = "aa"
    assert get_palindrome.generate_char_map(candidate) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 2, "odd" : 0 } }
def test_get_character_map_simple_three():
    candidate = "aaa"
    assert get_palindrome.generate_char_map(candidate) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 3, "odd" : 1 } }
def test_get_character_map_even():
    candidate = "aabb"
    assert get_palindrome.generate_char_map(candidate) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 2, "odd" : 0 }, 'b' : { "count" : 2, "odd" : 0 } }
def test_get_character_map_odd():
    candidate = "aabbc"
    assert get_palindrome.generate_char_map(candidate) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 2, "odd" : 0 }, 'b' : { "count" : 2, "odd" : 0 }, 'c' : { "count" : 1, "odd" : 1 } }
def test_get_character_map_wildcard():
    candidate = "a?b"
    assert get_palindrome.generate_char_map(candidate) == { '?' : { "count" : 1, "odd" : 1 }, 'a' : { "count" : 1, "odd" : 1 }, 'b' : { "count" : 1, "odd" : 1 } }
def test_get_character_map_wildcard_two():
    candidate = "a??b"
    assert get_palindrome.generate_char_map(candidate) == { '?' : { "count" : 2, "odd" : 0 }, 'a' : { "count" : 1, "odd" : 1 }, 'b' : { "count" : 1, "odd" : 1 } }

def test_is_palindromeable_simple():
    candidate = "a"
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.is_palindromeable(char_map) == True
def test_is_palindromeable_even():
    candidate = "abba"
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.is_palindromeable(char_map) == True
def test_is_palindromeable_odd():
    candidate = "racecar"
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.is_palindromeable(char_map) == True
def test_is_palindromeable_not():
    candidate = "hello"
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.is_palindromeable(char_map) == False
def test_is_palindromeable_empty():
    candidate = ""
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.is_palindromeable(char_map) == True
def test_is_palindromeable_wildcard_simple_two_odds():
    candidate = 'ab?'
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.is_palindromeable(char_map) == True
def test_is_palindromeable_wildcard_simple_one_odd_one_even():
    candidate = 'abb?'
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.is_palindromeable(char_map) == True
def test_is_palindromeable_wildcard_two_odds():
    candidate = 'abbb?'
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.is_palindromeable(char_map) == True
def test_is_palindromeable_wildcard_three_odds_two_wilds():
    candidate = 'abc??'
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.is_palindromeable(char_map) == True
def test_is_palindromeable_wildcard_four_odds_two_wilds():
    candidate = 'a?bc?d'
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.is_palindromeable(char_map) == False

def test_process_candidate_trivial():
    candidate = "a"
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.process_candidate(char_map) == "a"
def test_process_candidate_simple_rearrange():
    candidate = "aabb"
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.process_candidate(char_map) == "abba"
def test_process_candidate_rearrange_three_way():
    candidate = "caabb"
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.process_candidate(char_map) == "abcba"
def test_process_candidate_rearrange_many_ways():
    candidate = "cfbe?gdgaed?cgafbffb"
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.process_candidate(char_map) == "abbcdeffggggffedcbba"
def test_process_candidate_rearrange_wildcard():
    candidate = "a?b?c"
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.process_candidate(char_map) == "abcba"
def test_process_candidate_rearrange_wildcard_many():
    candidate = "b???"
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.process_candidate(char_map) == "abba"
def test_process_candidate_rearrange_wildcard_only():
    candidate = "????"
    char_map = get_palindrome.generate_char_map(candidate)
    assert get_palindrome.process_candidate(char_map) == "aaaa"


def test_even_out_char_map_simple():
    char_map = { '?' : { "count" : 1, "odd" : 1 }, 'a' : { "count" : 1, "odd" : 1 } }
    assert get_palindrome.even_out_char_map(char_map) == { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 2, "odd" : 0 } }
def test_even_out_char_map_simple_two():
    char_map = { '?' : { "count" : 1, "odd" : 1 }, 'a' : { "count" : 2, "odd" : 0 } }
    assert get_palindrome.even_out_char_map(char_map) == { '?' : { "count" : 1, "odd" : 1 }, 'a' : { "count" : 2, "odd" : 0 } }
def test_even_out_char_map_wildcard_only():
    char_map = { '?' : { "count" : 2, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }
    assert get_palindrome.even_out_char_map(char_map) == { '?' : { "count" : 2, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }

def test_replace_remaining_wildcards_simple():
    char_map = { '?' : { "count" : 1, "odd" : 1 }, 'a' : { "count" : 0, "odd" : 0 } }
    assert get_palindrome.replace_remaining_wildcards(char_map) == { 'a' : { "count" : 1, "odd" : 1 } }
def test_replace_remaining_wildcards_simple_two():
    char_map = { '?' : { "count" : 2, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }
    assert get_palindrome.replace_remaining_wildcards(char_map) == { 'a' : { "count" : 2, "odd" : 0 } }
def test_replace_remaining_wildcards_none():
    char_map = { '?' : { "count" : 0, "odd" : 0 }, 'a' : { "count" : 0, "odd" : 0 } }
    assert get_palindrome.replace_remaining_wildcards(char_map) == { 'a' : { "count" : 0, "odd" : 0 } }

def test_convert_char_map_to_palindrome_simple():
    char_map = { 'a' : { "count" : 2, "odd" : 0 } }
    assert get_palindrome.convert_char_map_to_palindrome(char_map) == "aa"
def test_convert_char_map_to_palindrome_simple_two():
    char_map = { 'a' : { "count" : 2, "odd" : 0 }, 'b' : { "count" : 2, "odd" : 0 } }
    assert get_palindrome.convert_char_map_to_palindrome(char_map) == "abba"
def test_convert_char_map_to_palindrome_odd():
    char_map = { 'a' : { "count" : 3, "odd" : 1 }, 'b' : { "count" : 2, "odd" : 0 } }
    assert get_palindrome.convert_char_map_to_palindrome(char_map) == "ababa"