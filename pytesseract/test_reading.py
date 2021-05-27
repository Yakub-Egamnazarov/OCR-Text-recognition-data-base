import os
from pprint import pprint
import re 

cwd = os.getcwd()
in_dir = os.path.join(cwd, 'output-txt')

files = os.listdir(in_dir)
files.sort()

file_1 = files[2]
file_1_path = os.path.join(in_dir, file_1)
file_1 = open(file_1_path, 'r')

def squiz_list(lst):
    new_lst = list(filter(None, lst))
    new_lst = new_lst[0:new_lst.index('CONTACT DETAILS')]
    return new_lst

def extract_company_name(lst):
    info_unit, data = 'Company Name', ''
    if info_unit in lst:
        i = lst.index(info_unit)
        if i == len(lst)-1: # this means the key word is last element in the list
            data = lst[-2]
        elif i == len(lst) - 2: # this means the key word is second to last el in the list 
            data = lst[-1]
        lst.pop()
        lst.pop()
    else:
        print('=> There is no info :', info_unit)
    return data, lst

def extract_company_address(lst):
    # some company addresses can be in several elementsin this list 
    # the address usually lies on between the delegate name and the last element
    key_a, key_b, data = 'Address', 'Delegate Name', ''
    
    if key_a in lst:
        index_a, index_b = lst.index(key_a), lst.index(key_b)
        new_lst = lst[:index_b+1]
        
        if index_a == len(lst) - 1: # the key word is last element in the list
            sublist = lst[index_b+1: index_a]
            
            if sublist[-1].endswith(','):
                sublist.reverse()
                data = ' '.join(sublist)
            else: 
                data = ', '.join(sublist)
            
            # print('=> adding the address...: ', data)
            
        elif index_a != len(lst) - 1: # the key word is not the first element in the list 
            sublist = lst[index_a + 1: ]
            # print('indexes:', index_a, index_b)
            if index_a - index_b > 2:
                sublist.append(lst[index_a-1])
                new_lst = lst[:index_b+2]
                
                # sublist.reverse()
            data = ', '.join(sublist)
            
            # print('=> adding add address... ', data)  
        
        return data, new_lst  
            
    else: 
        # print('=> There is no info:', key_a)
        return data, lst
    
def extract_delegate_name(lst):
    key_word = 'Delegate Name'
    data = ''
    
    if key_word in lst:
        print()
        if lst.index(key_word) == len(lst) - 1:
            data = lst[-2]
        elif lst.index(key_word) == len(lst) - 2:
            data = lst[-1]
        new_lst = lst[0: -2]
        return data, new_lst
    else: 
        print('=> There is not Delegate Name')
        return data, lst
    
    
    
#========================================================

# Downloaded the string and transformed to the list and unrelated data removed
raw_data = [line.strip() for line in file_1.readlines()]
raw_data = squiz_list(raw_data)


pprint(raw_data)
print('------------------------------------------')
data = {}

# Extract the company name and delete the related element from the base list 
data['company_name'], raw_data = extract_company_name(raw_data)
print('1. Extracted name:', data)
# pprint(raw_data)
print('------------------------------------------')

# Extract the address and delete the related element from the base list 
data['address'], raw_data = extract_company_address(raw_data)
print('2. Extracted address:', data)
pprint(raw_data)
print('------------------------------------------')

# extract the Delegate Name and delete the related element from the base list 
data['delegate name'], raw_data = extract_delegate_name(raw_data)
print('3. Extracted Delegate Name:', data)
pprint(raw_data)
print('------------------------------------------')

# TODO extract the Telephone and delete the related element from the base list 
# data['tel'], raw_data

# TODO if there is fax extract it and delete the related element from the base list 

# TODO extract website and delete the related information from the base list 

# TODO extract email and clear this email with the website acquired before 
