
def main():
    book_path = ("/Users/oskarikrook/workplace/github.com/okrook/bookbot/books/frankenstein.txt")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dictionary = count_char(text)
    sorted_list = chars_dict_to_sorted_list(character_dictionary)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in this document")
    
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")



    

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
        return d["num"]



def count_char(text):
    lowcasestring = text.lower()
    char_count = {}

    for char in lowcasestring:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def get_num_words(text):
    words = text.split()
    return len(words)
   

def get_book_text(path):
    with open(path) as f:
        return (f.read())

main()