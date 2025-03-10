s="hello12333@"
count_vowels=count_consonants=count_digits=count_special=0
for i in s:
    if i.isalpha():
        if i in "aeiouAEIOU":
            count_vowels+=1
        else:
            count_consonants+=+1
    elif i.isdigit():
       count_digits+=1
    else:
        count_special+=1
print("vowels : " ,count_vowels)
print("consonanats : ",count_consonants)
print("count of digits : " ,count_digits)
print("other symbols : ",count_special)
        
           

    