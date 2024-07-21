def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    chars_dict = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    

def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count


def count_characters(text):
    character_num = {}
    for character in text:
        lower = character.lower()
        if lower in character_num:
            character_num[lower] +=1
        else:
            character_num[lower] = 1
    return character_num


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
        

main()
