"""Train and use a simple k-nearest neighbour classifier"""
import csv
import random
import math

def load_dataset(dataset_location) :
    with open(dataset_location, 'r') as csvfile:
        return list(csv.reader(csvfile))

def split(split_ratio, examples) :
    """ Split a list of examples into a test and train set """
    pass

def euclidian_distance(a, b, features_count) :
    pass

def get_label(example) :
    pass

def head(lst) :
    pass

def classify(example, model, k, features_count) :
    pass

def run_experiment(dataset_location, features_count, k = 3, split_ratio = 0.33) :
    """
    Runs a train/test cycle on the provided data set.

    Args:
        dataset_location (str): local filesystem location of the csv-formatted dataset
        features_count (int): number of columns from the left that contain features
        k (int): number of neighbours to check for classification
        split_ratio (float in range 0..1): ratio of split between train and test sets
    """
    pass
