rm(list=ls())
library(forecast)
workDirectory = "/Users/zhangyiqun/Desktop/Term2/IR_DM/GroupProject/irdm"
inputFile = './features/load_features.csv'
outputFile = './output/ann_fit.csv'
setwd(workDirectory)

if(!file.exists(inputFile)){
    stop(paste(inputFile, " doesn't exist, please check!"))
}

load = read.csv(inputFile)

zones = 1:20
loadzones = load[,10:29]
#bk_date_start = ['2005-3-6 00:00:00', '2005-6-20 00:00:00', '2005-9-10 00:00:00', '2005-12-25 00:00:00', '2006-2-13 00:00:00', '2006-5-25 00:00:00', '2006-8-2 00:00:00', '2006-11-22 00:00:00']
#bk_date_end = ['2005-3-12 23:00:00', '2005-6-26 23:00:00', '2005-9-19 23:00:00', '2005-12-31 23:00:00', '2006-2-19 23:00:00', '2006-5-31 23:00:00', '2006-8-8 23:00:00', '2006-11-28 23:00:00']
missing_index1 = 10321:10488 # 167
missing_index2 = 12865:13032
missing_index3 = 14833:15000
missing_index4 = 17377:17544
missing_index5 = 18577:18744
missing_index6 = 21001:21168 
missing_index7 = 22657:22824
missing_index8 = 25345:25512
missing_index9 = 39247:39414
missing_index = list(missing_index1, missing_index2, missing_index3, missing_index4, missing_index5, missing_index6, missing_index7, missing_index8, missing_index9)
for(i in zones){
    tmp_loadzone = loadzones[i]
    for(idx in 1:length(missing_index)){
        train_s = 1
        train_e = missing_index[[idx]][1] - 1
        for(f in 1:7){
            train_data = tmp_loadzone[1:train_e,]
            train_data[train_data==0] = mean(train_data)
            fit <- nnetar(log(train_data))
            predictions <- forecast(fit, h=24)
            test_value = predictions[['mean']]
            tmp_loadzone[(train_e+1):(train_e+24),] = exp(test_value)
            train_e = train_e + 24
        }
        print(paste('missing_index', idx))
    }
    load[9+i] = tmp_loadzone
    print(paste('zones', i))
}

if(file.exists(outputFile)){
    file.remove(outputFile) # remove temp file
}
write.table(load, file=outputFile, sep=',', row.names = FALSE, col.names = TRUE)


