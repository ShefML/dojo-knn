"""Train and use a simple k-nearest neighbour classifier"""
import csv
import random
import math

def load_dataset(dataset_location):
    with open(dataset_location, 'r') as csvfile:
        return list(csv.reader(csvfile))

def split(split_ratio, examples):
    """ Split a list of examples into a test and train set """
    train = []
    test = []
    for example in examples:
        if random.random() < split_ratio:
            train.append(example)
        else:
            test.append(example)
    return [train, test]

def euclidian_distance(a, b, features_count):
    distance = 0
    for index in range(features_count):
        distance += math.pow((float(b[index]) - float(a[index])), 2)
    return math.sqrt(distance)

def get_label(example):
    return example[4]

def head(lst):
    return lst[0]

def classify(example, model, k, features_count):
    distances = []
    for datum in model:
        distances.append([euclidian_distance(example, datum, features_count), get_label(datum)])
    topKByDistance = sorted(distances, key = head)[0:k]
    topKLabels = list(map(lambda x: x[1], topKByDistance))
    votes = {}
    for label in topKLabels:
        if label in votes:
            votes[label] += 1
        else:
            votes[label] = 1
    sortedVotes = sorted(votes, key=votes.get, reverse=True)
    return get_label(example) == head(sortedVotes)

def run_experiment(dataset_location, features_count, k = 3, split_ratio = 0.33):
    """
    Runs a train/test cycle on the provided data set.

    Args:
        dataset_location (str): local filesystem location of the csv-formatted dataset
        features_count (int): number of columns from the left that contain features
        k (int): number of neighbours to check for classification
        split_ratio (float in range 0..1): ratio of split between train and test sets
    """
    examples = load_dataset(dataset_location)
    [train, test] = split(split_ratio, examples)
    results = []
    for unseen in test:
        results.append(classify(unseen, train, k, features_count))
    correct = list(filter(lambda x: x == True, results));
    print(len(correct)/len(results) * 100)
