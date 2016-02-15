# -*- coding: utf-8 -*-
"""
Created on Wed Jan 06 22:05:44 2016

@author: BearDeer
"""

import csv

print 'start'


input_file = open('..\data\skill_builder_data_good_m.csv', 'rb')
output_file = open('..\data\dkt_input.txt', 'w')
output_file_2 = open('..\data\dkt_input_2.txt', 'w')
csv_reader = csv.reader(input_file)
print csv_reader.next()

user_id_col = 1
correct_col = 2
skill_id_col = 4
skill_count = 123
csv_data = []
skill_skill_mapping = {}
current_str = ''
current_str_2 = ''
current_skill_count = -1

current_user_id = None

for row in csv_reader:
    user_id = row[user_id_col]
    correct = int(row[correct_col])
    skill_id = row[skill_id_col]
    current_coding = ['0'] * (skill_count * 2)
    
    if skill_skill_mapping.has_key(skill_id) == False:
        current_skill_count += 1
        skill_skill_mapping[skill_id] = current_skill_count
    skill_id = skill_skill_mapping[skill_id]
    
    
    skill_coding = correct * skill_count + skill_id
    current_coding[skill_coding] = '1'
    
    if user_id != current_user_id and current_user_id != None:
        current_str = current_str[:-1] + '\n'
        output_file.write(current_str)

        current_str_2 = current_str_2[:-1] + '\n'
        output_file_2.write(current_str_2)
        
        current_str = ''
        current_str_2 = ''
        
    current_str = current_str + ''.join(current_coding) + ','
    current_str_2 = current_str_2 + str(skill_coding) + ','
    
    current_user_id = user_id


current_str = current_str[:-1] + '\n'
current_str_2 = current_str_2[:-1] + '\n'

output_file.write(current_str)
output_file_2.write(current_str_2)

input_file.close()
output_file.close()

print current_skill_count



        
    
    

