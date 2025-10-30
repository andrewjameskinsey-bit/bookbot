def get_words(text):
    words = text.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    return wordcount

def lett_count(text):
    new_text = text.lower().split()
    text_dict = {}
    for lett in list(''.join(new_text)):
        if lett in text_dict:
            text_dict[lett] += 1
        elif lett not in text_dict:
            text_dict[lett] = 1
    return text_dict

def sort_on(text_dict):
    return text_dict["num"]

def build_sorted_list(text_dict):
    result = []
    for char, count in text_dict.items():
        if char.isalpha():
            result.append({"char" : char, "num" : count })
    result.sort(key = sort_on , reverse = True)
    return result
