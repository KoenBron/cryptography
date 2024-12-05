def convert_char_to_integers(char_array):
    return_list = []
    base = ord('a')
    for l in char_array:
        if l.isalpha():
            return_list.append(ord(l) - base)
        else:
            return_list.append(l)
    return return_list

def produce_plain_text(offset, array_original):
    array = array_original.copy()
    base = ord('a')
    for i, value in enumerate(array):
        if isinstance(value, int):
            offset_value = (value + offset)%26
            # Return to character
            array[i] = chr(offset_value + base)
    print("\nOffset: ", offset)
    for letter in array:
        print(letter, end="")
    return array

if __name__ == "__main__": 
    cypher = open("ceasar_cypher.txt", "r")
    # cypher = open("assignment_cypher1.txt")
    solutions = open("ceasar_solutions.txt", "w")

    char_array = [char for char in cypher.read().lower()]
    converted_chars = convert_char_to_integers(char_array)


    # Brute force it
    for i in range(26):
        # print(produce_plain_text(i, converted_chars))
        produce_plain_text(i, converted_chars)
        pass
