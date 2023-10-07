def replace_in_list(my_list, idx, element):
 if idx >= len(my_list) or idx < 0:
   return my_list
 else :
      return my_list[:idx] + [element] + my_list[idx+1:] 
