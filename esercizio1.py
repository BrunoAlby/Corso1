def sum_list(list):
    if not list:
        return None
    else:
        totale=0
    
        for item in list:
          totale += item
        return totale 
    
print (sum_list([2,4]))
