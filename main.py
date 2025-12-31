from stats import word_count, char_count
import sys

def get_book_text(path):
    #takes path and returns string
    with open(path) as f:
        contents = f.read()
    return str(contents)
    
    
 

def main():
    print(len(sys.argv))
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    input = sys.argv[1]
    s = get_book_text(input)
    print(s)
    count = word_count(s)
    print(f"Found {count} total words")
    letters = char_count(s)
    #print(letters)
    for item in letters:
        print(item['char']+": "+str(item['num']))
    
main()