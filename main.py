def de_none(lst):
    return [x for x in lst if x is not None]
lst = [None, None, 1, [], (), {}, None]
result = de_none(lst)
print(result)




def list_insert(ref_list, start, num, rep):
    return ref_list[:start] + [num] * rep + ref_list[start:] if start <= len(ref_list) else -1
ref_list1 = [0, 1, 2, 3, 4, 5]
start1 = 4
num1 = 40
rep1 = 2
result1 = list_insert(ref_list1, start1, num1, rep1)
print(result1)




def get_elem(d, k):
    return d.get(k, None)
d1 = {'a': 1, 'b': None, 'c': [1, 2]}
k1 = 'a'
result1 = get_elem(d1, k1)
print(result1)