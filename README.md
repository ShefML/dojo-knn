# k-Nearest Neighbours Dojo

Instructions and tips for kNN classifier dojo.
An example implementation is provided in Python 3, but you're encouraged to solve the problem yourself - that way, you learn more and have more fun.

## You will need...

* a laptop with a suitable programming language installed and working
* the data sets (provided with this repo)

## kNN Algorithm

Google "kNN" or "k nearest neighbour" for detailed explanations of the algorithm. [Wikipedia](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) has detailed information, other sources like [Machine Learning Mastery](http://machinelearningmastery.com/k-nearest-neighbors-for-machine-learning/) may be easier for a crash course.

Essentially, the naive kNN classifier considers data as points in a space - each point has co-ordinates and a label.
The dimensions of the co-ordinates are known as "features".
You can measure the distance between any two points in that space, and so you can find the "nearest neighbours" of any point.
The algorithm performs this calculation for an unlabelled datum and classifies the unlabelled point the same as the majority of its "k" nearest neighbours.

Simple!

## The Data

We'll use the classic "Iris" data set to build and test our algorithms.
It's provided by the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Iris) and it's a comma-separated table with rows like this:

`5.1,3.5,1.4,0.2,Iris-setosa`

The four numbers are features of the flower, things like petal width and stamen length.
The last string is a label - the row above is measurements of [Iris Setosa](https://en.wikipedia.org/wiki/Iris_setosa).

I suggest we use this dataset because:
* it's in plain old CSV format - so you don't need to waste time working out how to parse some a weird format
* it's well-studied and we know we should be able to get good predictive power from it with a kNN classifier
* it's small - 150 rows - so we can start with writing a completely naive classifier and focus on how it works, without worrying about performance too early.

## The Task

Your task, should you choose to accept it, is:
* to write a kNN classifier and the necessary scaffolding to run it against the Iris data set, using a simple split of the data to produce training and test sets.

The following is a suggested breakdown - feel free to completely ignore it!

* Parse the data set into numeric features and labels
* Write an algorithm to "train" your classifier that takes a value for k and a training dataset
* Write an algorithm to "test" your classifier that takes the output of your "train" algorithm and a test dataset, predicts the labels of the test dataset, and returns a % correct predictions

There's a quick (and dirty!) implementation I did in Python 3 included in this project, in the `./python` directory.
I provide it here in case you get completely stuck on something!
For an example of the kind of performance you should expect on the iris dataset using this implementation, the sample implementation typically gets 80-90% correct on the test runs, but variation on exact accuracy between runs.

There's also `./knn-template` which might be useful if you're new to Python or programming in general and you're not sure where to start. It has its own `README.md` to get you moving.

Now, try a larger dataset (I suggest the [Phishing Websites dataset](https://archive.ics.uci.edu/ml/datasets/Phishing+Websites), also included in the repo

## Next Steps

Once you have a working classifier, there's a whole bunch of things you can play with, for example:

* try swapping out your data structures for something faster to compute over. In Python, consider [pandas](https://pandas.pydata.org/pandas-docs/stable/)
* update your code to use [leave-one-out cross-validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics#Leave-one-out_cross-validation) to produce a mean correct predictions for a given value of k. (Leave-one-out cross-validation means split the randomised dataset up into k "folds", then for each fold f, train on the rest of the dataset and use f to test the classifier, then average the results)
* optimising for a larger dataset (I suggest the [Phishing Websites dataset](https://archive.ics.uci.edu/ml/datasets/Phishing+Websites), also included in the repo
* try out a real-world kNN implementation, for example in Python you might try [scikit-learn's kNN implementation](http://scikit-learn.org/stable/modules/neighbors.html)
* check out different distance functions and the effect they have on accuracy
* check out the impact of ignoring subsets of features
* supporting categorical data to try out data sets (remember the [Titanic survivors data set](https://www.kaggle.com/c/titanic) from last session?)

... or anything else you want to play with!

## Thinking Points

* Does it matter whether the value of k is odd or even?
* Do you get different answers between test runs? If so, why? What difficulties does that behaviour impose and how can they be addressed?
* Did you try cross-validation? Why do you think it's better than a simple split?
* Does your algorithm perform well on larger data sets? How could you improve performance?
* What kinds of data sets would a kNN classifier perform well on? Can you think of any that it would perform poorly on?
* What kinds of problems might we find with the train/test split method we're using? How could we improve it?
* Do you think your implementation is good for general use? How would you improve it to make it more flexible?
* Could a kNN classifier be used to perform regression?
* What advantages and disadvantages does the kNN classifier have in comparison to other classifiers you know about?

Copyright © 2018 Paul Brabban

Produced for the SheffieldML meetup, forked from original work produced for the (def shef) meetup.
Please feel free to copy, modify or otherwise reuse!

Distributed under the Eclipse Public License either version 1.0 or (at
your option) any later version.
