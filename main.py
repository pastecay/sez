 lst = [None, None, 1, [], (), {}, None]
 def de_none(lst):
     new_lst = [item for item in lst if item is not None]
     return new_lst
 print(new_lst)


ref_list = [0,1,2,3,4]
 new_lst = []
 start = int(input())
 num = int(input())
 rep = int(input())

 newlst = ref_list.copy()
 for i in range(rep):
  newlst.insert(start, num)
 return newlst

def get_elem(d,k):
     try:
         return d[k]
     except:
         return None
