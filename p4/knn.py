import csv
import math
import operator
import matplotlib.pyplot as plt


# This fuvntion is loadin The train file and casting them from String to float
def loadData(file_name):
    with open(file_name, 'r') as csvFile:
        l = csv.reader(csvFile)
        Data_set = list(l)
        Data_set.pop(0)
        for column in range(len(Data_set)):
            for row in range(len(Data_set[0])):
                Data_set[column][row] = float(Data_set[column][row])
    return Data_set


def TheEclideanDistance(instance1, instance2, number_of_columns):
    d = 0
    for x in range(number_of_columns):
        d += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(d)


def getNeighbors(trainingSet, test_row, k):
    neighbors = []
    number_of_columns = len(test_row) - 1
    for x in range(len(trainingSet)):
        dist = TheEclideanDistance(test_row, trainingSet[x], number_of_columns)
        neighbors.append((trainingSet[x], dist))
    # sorting  the neighbors according to their distances
    neighbors.sort(key=operator.itemgetter(1))
    k_neighbors_price_range = []
    for i in range(k):
        k_neighbors_price_range.append(neighbors[i][0][20])
    return k_neighbors_price_range


def getResponse(neighbors):
    class_votes = {}
    for x in range(len(neighbors)):
        response = neighbors[x]
        if response in class_votes:
            class_votes[response] += 1
        else:
            class_votes[response] = 1
    sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes[0][0]


def getAccuracy(test_set, predictions):
    C = 0
    for x in range(len(test_set)):
        if test_set[x][-1] == predictions[x]:
            C += 1
    print("correct: ", C)
    return (C / float(len(test_set))) * 100


def main():
    # Preparing The Data
    train_file = 'train.csv'
    test_file = 'test.csv'
    training_set = loadData(train_file)
    test_set = loadData(test_file)
    print("\n\nTrain set: ", len(training_set))
    print("Test set: ", len(test_set))
    y_coordinate = []
    k = 10
    k_neighbors_price_ranges = []
    
    # get price range of k neighbors for each row(each test row)
    print("\n\nCalculating Euclidean Distance \nPlease wait...")
    for x in range(len(test_set)):
        k_neighbors_price_range = getNeighbors(training_set, test_set[x], k)
        k_neighbors_price_ranges.append(k_neighbors_price_range)
    print("\nEuclidean Distance calculations are done!\n\n")   
    for j in range(1, k + 1):
        predictions = []
        print("k: ", j)
        for i in range(len(k_neighbors_price_ranges)):
            result = getResponse(k_neighbors_price_ranges[i][0:j])
            predictions.append(result)
            # print('Predicted: ' + str(result) + "  >>  ", "Actual: " + str(test_set[i][-1]))
        accuracy = getAccuracy(test_set, predictions)
        print("Accuracy: " + str(accuracy) + "%\n")
        y_coordinate.append(accuracy)

    f = plt.figure()
    plt.plot(range(1, 11), y_coordinate)
    # plt.show()
    f.savefig("plot.pdf", bbox_inches='tight')


main()
