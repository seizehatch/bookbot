def main():
    book_path = "books/frankenstein.txt"
    content = get_content(book_path)
    word_count = get_word_count(content)
    #print(f"{word_count} words in document")
    chars_count = get_char_occurrence(content)
    #print(chars_count)
    dicts_list = convert_to_dict_list(chars_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    for i in dicts_list:
        print(f"The {i['char']} was found {i['count']} times")
    
    print("--- End report ---")

def get_content(path):
    with open(path) as f:
        return f.read()

def get_word_count(content):
    words = content.split()
    return len(words)

def get_char_occurrence(content):
    lower_case_content = content.lower()
    used_chars = {}
    for i in lower_case_content:
        if i.isalpha():
            if i not in used_chars:
                used_chars[i] = 1
            else:
                used_chars[i] += 1
    return used_chars

def convert_to_dict_list(chars_count):
    chars_list = []
    for i in chars_count:
        dict = {"char" : i, "count" : chars_count[i] }
        chars_list.append(dict)
    chars_list.sort(reverse=True, key=sort_on)
    return(chars_list)

def sort_on(dicts_list):
    return dicts_list["count"]

main()