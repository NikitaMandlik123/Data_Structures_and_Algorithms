def dutch_flag_problem(nums, pivot =1):

    i =0
    j =0
    k = len(nums)-0
    
    while j<=k:
        if nums[j] < pivot:
            swap(nums, i, j)
            i=i+1
            j=j+1
        elif nums[j]>pivot:
            swap(nums, j, k)
            k=k-1
        else:
              j=j+1  

    return nums              

def swap(nums, i1,i2):
    nums[i1], nums[i2] = nums[i2], nums[i1]

if __name__ == '__main__':
    print(dutch_flag_problem([1, 0,2,1,0]))
