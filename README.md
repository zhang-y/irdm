##IRDM Group Project -- Global Energy Forecasting Competition 2012: Load Forecasting
Group Members: RUIJIE TU, DONG SUN, YIQUN ZHANG

###src Directory:
    all code are in root directory(python and R)
    filename start with 'old' are for models which are not discussed in our report.

###data Directory:
    all files in this directory are downloaded from https://www.kaggle.com/c/global-energy-forecasting-competition-2012-load-forecasting/data
    
###features Directory:
    csv files containing data after feature engineering are saved in this directory.
    load_features.csv has only features generated from Load_history.csv
    GP_temppred.csv has only features generated from temperature.csv 
    loadtemp_features.csv is the combination of load_features.csv and GP_temppered.csv file
    loadtemp_features_withsmoothtemp.csv is by add smoothed tempeartures to loadtemp_features.csv file(part of smoothed tempteratures are acquired from https://github.com/jamesrobertlloyd/gp-structure-search)

###output Directory:
    ann_keras_fit.csv is the result for Neural Network, and result is used in the report.
    svm_output.csv is the result for SVM, and result is used in the report.
    gbm_output3.csv is the result for Gradient Boosting, and result is used in the report.
    arima_fit.csv it the result for ARIMA(this is only done for backcast), result is not good and not used in the report.
    
    
