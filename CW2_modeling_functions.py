import time
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, ConfusionMatrixDisplay

# library for modeling
def modeling_pipeline_classification(list_models, X_train, y_train, X_test, y_test):
    '''
    Generate prediction of 1 dataset from many models. This function help to collect performance of multiple models, hence support in the model's
    performance comparison process.

    Input:
        - list_models: list of classification models, usually sklearn models
        - X_train, y_train: data use for training - X_train columns need to all be in numeric type
        - X_test: data use for prediction - columns need to be in numeric type
        - y_test: outcome column of hold-out set, use in calculating error metrics
    Output:
        - error_info: a list include many sublist, each sublist contain information of performance of 1 model and its execution time
            + sublist: [algo_name, accuracy, precision, recall, f1, cm, exc_time]
    '''
    error_info = []

    for algo_name, model in list_models.items():
        # get the start time
        st = time.time()
        # fit the model with data
        model.fit(X_train, y_train)
        # predict by the trained model
        y_pred = model.predict(X_test)
        # get the end time
        et = time.time()
        # get the execution time
        exc_time = et - st
        # accuracy, precision, recall
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
    
        # confusion matrix
        cm = confusion_matrix(y_test, y_pred)
    
        # store error metric
        a_model_error_info = [algo_name, accuracy, precision, recall, f1, cm, exc_time]
        # append error of 1 model into the big list
        error_info.append(a_model_error_info)
    return error_info