def main(the_input):
    vowels = "aeiou"
    output = ''
    for i in the_input:
        if i.lower() in vowels and i != "u":
            i = vowels[vowels.index(i)+1]
        elif i == "u":
            i = "a"
        output+=i
    print(output)
def convert(the_input):
    vowels = "aeiou"
    output = ''
    for i in the_input:
        if i.lower() in vowels and i != "a":
            i = vowels[vowels.index(i)-1]
        elif i == "a":
            i = "u"
        output+=i
    print(output)

            