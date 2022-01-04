#Palindrome problem overview
#Interview Question #2


def palindrome_review(s):
    
    #for string using string slicing

    if s == s[::-1]:
        return True
    else:
        return False  

#other method
def is_palindrome(s):
    orignal_string =s
    reversed_string = reverse(s)
    if orignal_string ==reversed_string:
        return True
    else:
        return False    


def reverse(data):
    #pointing to the first item
    low_index = 0
    #pointing to the last item
    high_index =len(data)-1

    while high_index > low_index:
        data=list(data)
        data[low_index], data[high_index] = data[high_index], data[low_index]
        low_index =low_index +1
        high_index= high_index-1
    return ''.join(data)

if __name__ == '__main__':
    print(is_palindrome('radar'))
          