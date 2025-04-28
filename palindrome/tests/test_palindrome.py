import palindrome.get_palindrome as get_palindrome

def test_is_palindromeable_simple():
    candidate = "a"
    assert get_palindrome.is_palindromeable(candidate) == True

def test_is_palindromeable_even():
    candidate = "abba"
    assert get_palindrome.is_palindromeable(candidate) == True
def test_is_palindromeable_odd():
    candidate = "racecar"
    assert get_palindrome.is_palindromeable(candidate) == True
def test_is_palindromeable_not():
    candidate = "hello"
    assert get_palindrome.is_palindromeable(candidate) == False
def test_is_palindromeable_empty():
    candidate = ""
    assert get_palindrome.is_palindromeable(candidate) == True
def test_is_palindromeable_wildcard_simple_two_odds():
    candidate = 'ab?'
    assert get_palindrome.is_palindromeable(candidate) == True
def test_is_palindromeable_wildcard_simple_one_odd_one_even():
    candidate = 'abb?'
    assert get_palindrome.is_palindromeable(candidate) == True
def test_is_palindromeable_wildcard_two_odds():
    candidate = 'abbb?'
    assert get_palindrome.is_palindromeable(candidate) == True
def test_is_palindromeable_wildcard_three_odds_two_wilds():
    candidate = 'abc??'
    assert get_palindrome.is_palindromeable(candidate) == True
def test_is_palindromeable_wildcard_four_odds_two_wilds():
    candidate = 'a?bc?d'
    assert get_palindrome.is_palindromeable(candidate) == False

def test_process_candidate_trivial():
    candidate = "a"
    assert get_palindrome.process_candidate(candidate) == "a"
def test_process_candidate_simple_rearrange():
    candidate = "aabb"
    assert get_palindrome.process_candidate(candidate) == "abba"
def test_process_candidate_rearrange_three_way():
    candidate = "caabb"
    assert get_palindrome.process_candidate(candidate) == "abcba"
def test_process_candidate_rearrange_many_ways():
    candidate = "cfbe?gdgaed?cgafbffb"
    assert get_palindrome.process_candidate(candidate) == "abbcdeffggggffedcbba"
