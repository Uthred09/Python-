def vowel(word):
    new = word.lower()
    v_count = 0
    c_count = 0
    for char in new:
        if char in ['a', 'e', 'i', 'o','u']:
            v_count += 1
        else:
            c_count +=1
    return v_count, c_count

# v_count, c_count = vowel("Susan")
# print(v_count)
# print(c_count)

def sumOfString(number):
    sum_ = 0
    for num in number:
        pri

def splitWord():
    input_String = 'dell,razor,$1500,20,i7 11 gen, gtx 3050'
    word = input_String.split(",")
    return word
