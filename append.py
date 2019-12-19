#APPENDING OPERATION ON LISTS
#appendig list as a element
print("\nAppending using list as a element:\n")
list_A = ['DIGITAL', 'SIGNAL'] 
print ("list_A before appendig",list_A )
list_A.append('PROCESSING')
print ("list_A after appendig",list_A ) 
#appending using two lists
print("\nAppending using two lists\n")
list1 = ['digital','signal','processing'] 
print("list1 before appendig:",list1)
list2 = ['-four periods per week'] 
print("list2 before appendig:",list2)
list1.append(list2) 
print("list after appendig:")
print (list1)
