#Reversing an array in-place overview
#Interview Question #1

#The problem is that we want to reverse a T[] array in O(N) linear time complexity and we want the algorithm to be in-place as well - so no additional memory can be used!

#For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

def reverse_array(num):
    
    #pointers to the low and high indices
    low_index = 0
    high_index = len(num)-1

    while high_index > low_index :
        #swap the items
        num[low_index] , num[high_index] = num[high_index] , num[low_index]
        low_index = low_index+1
        high_index = high_index-1

#main function
if __name__== '__main__' :
     
     n = [1,2,3,4,5]
     reverse_array(n)
print(n)     


