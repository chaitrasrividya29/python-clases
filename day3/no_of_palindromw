def is_palindrome(word):
    lista=list(word)
    if len(lista)==1:
        return False
    if lista==lista[::-1]:
        return True
    return False

def normalize_spaces(sentence):
    words = sentence.split()
    normalized_sentence = " ".join(words)
    return normalized_sentence

sentence = input("Enter a sentence: ")
result = normalize_spaces(sentence)
list1=list(result.split())
count=0
for word in list1:
    if is_palindrome(word):
        print(word)
        count+=1
print(f"there are {count} palindromes in the sentence")
