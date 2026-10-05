def min_max(nums: list[float|int]):
    ''' Вычисляет максимум и минимум в списке

    Args: 
        nums: Список чисел (целых и вещественных)

    Returns:
        Кортеж (минимум, максимум)

    Raises:
        ValueError: Если список пустой
    '''
    if not nums:
        return 'ValueError'
    mx=nums[0]
    mn=nums[0]
    for i in nums:
        if i>mx:
            mx=i
        elif i<mn:
            mn=i
    return ((mn,mx))

def unique_sorted(nums: list[float|int]):
     
    '''Возвращает отсортированный список уникальных значений

    Args:
        nums: Список чисел (целых и вещественных)

    Returns:
        Отсортированный список
    '''
    nums=set(nums)
    nums=list(nums)
    return nums

def flatten(mat: list[list|tuple]):
    '''Переводит матрицу в вектор

    Args:
        mat: Список, в котором содержатся списки и кортежи
    
    Returns:
        array: Список
    
    Raises:
        TypeError: Если передана не матрица
    '''
    array=[]
    for i in mat:
        if type(i)==list or type(i)==tuple:
            for j in i:
                array.append(j)
        else:
            return 'TypeError'
    return array
             
print(min_max([3,-1,5,5,0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([]))
print(min_max([1.5,2,2.0,-3.1]))
print()
print(unique_sorted([3,1,2,1,3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print()
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))

