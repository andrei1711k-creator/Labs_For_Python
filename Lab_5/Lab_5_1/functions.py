
def count_words(sentence: str) :
    if not sentence.strip():
        return 0
    return len(sentence.split())


def find_unique(items):
    return [x for x in items if items.count(x) == 1]



def is_palindrome(value) :
    s = str(value)
    return s == s[::-1]



def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1.replace(" ", "")) == sorted(s2.replace(" ", ""))



def merge_dicts(dict_a: dict, dict_b: dict) -> dict:
    for key, value in dict_b.items():
        if key in dict_a:

    
            if isinstance(dict_a[key], dict) and isinstance(value, dict):
                merge_dicts(dict_a[key], value)


            elif isinstance(dict_a[key], list) and isinstance(value, list):
                dict_a[key].extend(value)


            elif isinstance(dict_a[key], set) and isinstance(value, set):
                dict_a[key].update(value)


            elif isinstance(dict_a[key], tuple) and isinstance(value, tuple):
                dict_a[key] = dict_a[key] + value


            else:
                dict_a[key] = value
        else:
            dict_a[key] = value

    return dict_a
