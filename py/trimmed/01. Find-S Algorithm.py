# coding: utf-8
import random
import csv
print("\n The most general hypothesis :['?','?','?','?','?','?']\n")
print("\n The most specific hypothesis :['0','0','0','0','0','0']\n")
a = []
with open('datasets/enjoysport.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        a.append(row)
        print(row)
    csvFile.close()
num_attributes = len(a[0]) - 1
num_attributes
a
hypothesis = ['0'] * num_attributes
print('Initial Value of the hypothesis: ')
print(hypothesis)
for j in range(0, num_attributes):
    hypothesis[j] = a[1][j]
hypothesis
print('\nFind S: Finding Maximally specific hypothesis\n')
for i in range(1, len(a)):
    if a[i][num_attributes] == 'yes':
        for j in range(num_attributes):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
            else:
                hypothesis[j] = a[i][j]
    print("For training example no :{0} the hypothesis is".format(
        i), hypothesis)
print("\n The Maximally Specific Hypothesis for a given Training Examples:\n")
print(hypothesis)
