#Anagram problem overview
#Interview Question #4

#Construct an algorithm to check whether two words (or phrases) are anagrams or not!

def is_anagram(s1,s2):
    #if the length differ, then it is not anagram
    if len(s1) != len(s2):
        return False
    
    #we have to sort the letters of the string and then wehave to compare same indexes
    s1 = sorted(s1)
    s2=sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True   

if __name__ == '__main__':
    str1 = ['f','l','u','s','t','e','r']
    str2=  ['r','e','s','t','f','u','l']
    print (is_anagram(str1,str2))