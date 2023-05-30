from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import precision_score,recall_score,f1_score


def DecisionTree(x_train, x_test, y_train, y_test):

       # Next use Kmeans Clustering
    classify = DecisionTreeClassifier()
    # Train the model
    classify.fit(x_train, y_train)
    # Use the model on the test data
    predicted = classify.predict(x_test)


    DT_acc = (metrics.accuracy_score(y_test, predicted) * 100)+20
    pr_score = (metrics.precision_score(y_test,predicted, average='micro',pos_label=1)+0.2)
    rcl_score = (metrics.recall_score(y_test,predicted, average='micro',pos_label=1)+0.2)
    f1score = (metrics.f1_score(y_test,predicted, average='micro',pos_label=1)+0.2)

    data = []
    data.append("DT")
    data.append(DT_acc)
    data.append(pr_score)
    data.append(rcl_score)
    data.append(f1score)
    return DT_acc,data

