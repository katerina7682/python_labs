def min_max(nums: list[float|int]):
    mx=nums[0]
    mn=nums[0]
    for i in nums:
        if i>mx:
            mx=i
        if i<mn:
            mn=i
    return ((mn,mx))
print(min_max([2,6,4.5,8.7,3,10,89,90]))

def unique_sorted(nums: list[float|int]):
    nums=set(nums)
    nums=list(nums)
    return nums
print(unique_sorted([1,5,7,4,2,9,8,2,2,5]))

def flatten(mat: list[list|tuple]):
    array=[]
    for i in mat:
        if type(i)==list or type(i)==tuple:
            for j in i:
                array.append(j)
        else:
            return 'TypeError'
    return array
print(flatten([[2,5],[7,6],[34,80,96,57]]))
             
