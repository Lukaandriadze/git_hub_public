def is_polindrome(word):
    length = len(word)
    first = 0
    last = length -1 
    status = 1
    while(first<last):
        if(word[first]==word[last]):
            first+=1
            last-=1
        else:
            status = 0
            break
        return int(status)  

word = input("სიტყვა:")             
status= is_polindrome(word)
if(status):
    print("პალინდრომია")
else:
    print("არ აროს პალინდრომი")               
