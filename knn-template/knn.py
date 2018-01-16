"""Train and use a simple k-nearest neighbour classifier"""
import csv # to load your data
import random # to randomly partition your data into test and training sets
import math # to calculate distances

def load_dataset(dataset_location):
    """ Read the CSV file at dataset_location, returning a list (the file) of lists (rows)"""
    with open(dataset_location, 'r') as csvfile:
        return list(csv.reader(csvfile))

def split(split_ratio, examples):
    """ Split a list of examples into a test and train set """
    pass

def euclidian_distance(a, b, features_count):
    """
    Calculate the distance between a and b, using Pythagoras' Theorem.

    Args:
        a (list of numbers): co-ordinates (features) of a data point
        b (list of numbers): co-ordinates (features) of another data point
        features_count: how many elements of each data point to use as features, counting from the left
    """
    pass

def classify(example, model, k, features_count):
    """
    Args:
        example (list of numbers or strings): features and label for the example to be classified
        model (list of examples): the training set
        k (number): of nearest neghbours to consider for classification
        features_count (number): how many elements of each example, counting from the left, are features
    """
    pass

def run_experiment(dataset_location, features_count, k = 3, split_ratio = 0.33):
    """
    Runs a train/test cycle on the provided data set.

    Takes a CSV file where each row is (feature, feature, ... , label)
    Example: 5.1,3.5,1.4,0.2,Iris-setosa

    Args:
        dataset_location (str): local filesystem location of the csv-formatted dataset
        features_count (int): number of columns from the left that contain features
        k (int): number of neighbours to check for classification
        split_ratio (float in range 0..1): ratio of split between train and test sets
    """
    pass
