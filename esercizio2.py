def sum_list(list):
    if not list:
        return None
    else:
        totale=0

        for item in list:
          totale += item
        return totale 

#print (sum_list([2,4]))

def sum_csv(file_name):    
    if not file_name:
        return None
    else:
        values = []
    
        my_file = open('shampoo_sales.csv', 'r')
        for line in my_file:
            elements = line.split(',')
            if elements[0] != 'Date':
                date = elements[0]
                value = elements[1]
                values.append(float(value))
        my_file.close()

        totale=0

        #for item in values:
            #totale += item
        #return totale 
        return sum(values)
        
#print(sum_csv('shampoo_sales.csv'))