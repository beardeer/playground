import csv

input_file = open('../data/builder_train.csv', 'rb')
output_file = open('../data/skill_difficulty.csv', 'wb')

reader = csv.reader(input_file)
writer = csv.writer(output_file)

num = None
ids = []
correct = []

diff_data = {}

for i in range(100):
	diff_data[i] = [0,0]

for i in reader:
	if num is None:
		num = i
		continue
	
	if len(ids) == 0:
		ids = map(int, i)
		continue
	
	if len(correct) == 0:
		correct = map(int, i)

		if len(ids) != len(correct):
			print 'no!!!'
			break

		for n, e in enumerate(ids):
			this_id = ids[n]
			this_correct = correct[n]

			c, n = diff_data[this_id]
			c = c + this_correct
			n = n + 1
			diff_data[this_id] = [c, n]

		num = None
		ids = []
		correct = []

for i in range(100):
	c, n = diff_data[i]
	writer.writerow([i, 1-float(c) / n])



input_file.close()
output_file.close()
