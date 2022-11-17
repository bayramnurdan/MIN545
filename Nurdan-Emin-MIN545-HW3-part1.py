# MIN 545 HW3
# Code belongs to Nurdan Emin
# Write a recursive function that generates a list of all anagrams of a given string


def anagrams_of(s, accumulated="", anagrams=[]):
    s = [x for x in s]  # convert string into list so that copy and remove functions can be used
    if len(s) == 0:  # base case
        anagrams.append(accumulated)

    else:
        for item in s:
            new_s = s.copy()
            new_s.remove(item)
            anagrams_of(new_s, str(item + accumulated), anagrams)  # recursive case

    return anagrams
