import csv
from tqdm import tqdm

input_file_path = '../data/0910_no_dup_ss.csv'
output_file_path = '../data/0910_no_dup_ms.csv'

input_file = open(input_file_path, 'rb')
csv_reader = csv.reader(input_file)

output_file = open(output_file_path, 'wb')
csv_writer = csv.writer(output_file)

header = csv_reader.next()

prob_col = 2
skill_col = -1

prob_skill_dict = {}

data = []

for row in tqdm(csv_reader):
    data.append(row)
    prob_id = row[prob_col]
    skill_id = row[skill_col]

    skill_list = prob_skill_dict.setdefault(prob_id, [])
    skill_list.append(skill_id)

for prob_id in prob_skill_dict.keys():
    skill_list = prob_skill_dict[prob_id]
    skill_list = list(set(skill_list))
    skill_list.sort()
    prob_skill_dict[prob_id] = skill_list

print prob_skill_dict.items()[:5]

for row in tqdm(data):
    prob_id = row[prob_col]
    row[-1] = ';'.join(prob_skill_dict[prob_id])
    csv_writer.writerow(row)

input_file.close()
output_file.close()





