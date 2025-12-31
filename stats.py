def word_count(text):
    words = (text.split()) 
    return len(words)

def char_count(text):
    d = {}
    text = text.lower()
    for char in text:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    #print(d)
    sorted = dict_sort(d)
    return sorted
    
def dict_sort(dicts):
    l = []
    for k,v in dicts.items():
        #print(k)
        if k.isalpha():
            new_dict = {}
            #print(k,v)
            new_dict["char"] = k
            new_dict["num"] = v
            #print(new_dict)
            l.append(new_dict)
    l.sort(reverse=True,key=sort_on)
    #print(l)
    return l
    
def sort_on(items):
    return items["num"]