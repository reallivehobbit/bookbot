def count(file_contents):

    words = file_contents.split()
    word_length = len(words)
    return word_length

def character_count(file_contents):
    lowered_string = file_contents.lower()
    letter_dic = {}
    for char in lowered_string:
        if char.isalpha():
            if char not in letter_dic:
                letter_dic[char] = 1
            else:
                letter_dic[char] +=1
    return letter_dic

def sort_on(letter_dic):
    return letter_dic["times_found"]

def book_report(word_length, letter_dic):
    print("*****Book Report on books/frankenstein.txt*****")
    print(f"This book had {word_length} words.")

    letter_list = []
    for letter, count in letter_dic.items():
        new_dict = {"character": letter, "times_found": count}
        letter_list.append(new_dict)
    letter_list.sort(reverse=True, key=sort_on)

    for character in letter_list:
         print(f"The '{character['character']}' character was found {character['times_found']} times")

    print("****End of Report on books/frankenstein.txt****")
    


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    word_length = count(file_contents)
    letter_dic = character_count(file_contents)
    book_report(word_length, letter_dic)

main()
