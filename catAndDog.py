# Return True if the string "cat" and "dog" appear the same number of times in the given string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(s):
    cat_counter = 0
    dog_counter = 0

    if len(s) < 6:
        return False

    for i in range(len(s)-2):
        if s[i:i+3] == 'cat':
            cat_counter += 1
        elif s[i:i+3] == 'dog':
            dog_counter += 1

    return cat_counter == dog_counter


print(cat_dog('catdog'))
print(cat_dog('catcat'))