import csv

header = ['Episodes', 'Rewards']
reward_csv = open('testing_csv.csv','w')
writer = csv.writer(reward_csv)
writer.writerow(header)
for line in range(1000):
    writer.writerow([line+1, (line+1)**1.6**3.2])
reward_csv.close()