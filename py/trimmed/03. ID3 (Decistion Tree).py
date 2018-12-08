# coding: utf-8
import csv
import math
def major_class(attributes, data, target):
    freq = {}
    index = attributes.index(target)
    for t in data:
        if t[index] in freq:
            freq[t[index]] += 1
        else:
            freq[t[index]] = 1
    m = 0
    major = ""
    for key in freq.keys():
        if freq[key] > m:
            m = freq[key]
            major = key
    return major
def entropy(attributes, data, targetAttr):
    freq = {}
    data_entropy = 0.0
    i = 0
    for entry in attributes:
        if targetAttr == entry:
            break
        i += 1
    for entry in data:
        if entry[i] == 'PlayTennis':
            pass
        else:
            if entry[i] in freq:
                freq[entry[i]] += 1.0
            else:
                freq[entry[i]] = 1.0
    for f in freq.values():
        data_entropy += (-f/len(data)) * math.log(f/len(data), 2)
    return data_entropy
def info_gain(attributes, data, attr, targetAttr):
    freq = {}
    subset_entropy = 0.0
    i = attributes.index(attr)
    for entry in data:
        if entry[i] == attr:
            pass
        else:
            if entry[i] in freq:
                freq[entry[i]] += 1.0
            else:
                freq[entry[i]] = 1
    for val in freq.keys():
        p = sum(freq.values())
        val_prob = freq[val] / (p)
        data_subset = [entry for entry in data if entry[i] == val]
        subset_entropy += val_prob * entropy(attributes, data_subset, targetAttr)
    data_subset = [entry for entry in data if entry[0] != 'Outlook']
    return (entropy(attributes, data_subset, targetAttr) - subset_entropy)
def attr_choose(data, attributes, target):
    best = attributes[0]
    max_gain = 0
    for attr in attributes:
        if attr != target:
            new_gain = info_gain(attributes, data, attr, target)
            if new_gain > max_gain:
                max_gain = new_gain
                best = attr
    return best
def get_values(data, attributes, attr):
    i = attributes.index(attr)
    values = []
    for entry in data:
        if entry[i] == attr:
            pass
        else:
            if entry[i] not in values:
                values.append(entry[i])
    return values
def get_data(data, attributes, best, val):
    new_data = [[]]
    i = attributes.index(best)
    for entry in data:
        if entry[i] == val:
            new_entry = []
            for j in range(len(entry)):
                if j != i:
                    new_entry.append(entry[j])
            new_data.append(new_entry)
    new_data.remove([])
    return new_data
def build_tree(data, attributes, target):
    print(data)
    print(attributes)
    print(target)
    data = data[:]
    print(attributes.index(target))
    vals = [record[attributes.index(target)] for record in data]
    print(vals)
    default = major_class(attributes, data, target)
    if not data or (len(attributes) - 1) <= 0:
        return default
    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    else:
        best = attr_choose(data, attributes, target)
        tree = {best: {}}
        for val in get_values(data, attributes, best):
            new_data = get_data(data, attributes, best, val)
            new_attr = attributes[:]
            new_attr.remove(best)
            subtree = build_tree(new_data, new_attr, target)
            tree[best][val] = subtree
    return tree
def test(attributes, instance, tree):
    attribute = next(iter(tree))
    i = attributes.index(attribute)
    if instance[i] in tree[attribute].keys():
        result = tree[attribute][instance[i]]
        if isinstance(result, dict):
            return test(attributes, instance, result)
        else:
            return result
    else:
        return 'NULL'
def execute_decision_tree():
    data = []
    with open('datasets/PlayTennis.csv') as tsv:
        for line in csv.reader(tsv):
            data.append(tuple(line))
        print('Number of records: ', len(data))
    
    attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis']
    target = attributes[-1]
    training_set = [x for i, x in enumerate(data)]
    print(training_set)
    tree = build_tree(training_set, attributes, target)
    print('Decision Tree is as below: \n')
    print(tree)
    instance = ['Rain', 'Mild', 'High', 'Strong']
    print('Testing instance is: ', instance)
    result = test(attributes, instance, tree)
    print('The Target value for the testing instance is: ')
    print(result)
execute_decision_tree()
