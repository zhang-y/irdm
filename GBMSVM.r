library(gbm)
library(e1071)

X <- read.table('gbmi_input_2.csv', header = TRUE, sep = ',')

for (i in 1:20)
{
  test <- is.na(X[,i])
  #use this 168 points as evaluation points
  test[39246:39414] = TRUE
  train <- !test
  gbm1 <- gbm.fit(X[train,21:dim(X)[2]], X[train,i], n.trees=10000, distribution="gaussian", interaction.depth=3, shrinkage=0.01)
  X[test,i] <- predict.gbm(gbm1,X[test,21:dim(X)[2]],10000)
}

X <- read.table('gbmi_input_2.csv', header = TRUE, sep = ',')

for (i in 1:20)
{
  test <- is.na(X[,i])
  #use this 168 points as evaluation points
  test[39246:39414] = TRUE
  train <- !test
  my_svm <- svm(X[train,21:dim(X)[2]], X[train,i])
  X[test,i] <- predict(my_svm,X[test,21:dim(X)[2]])
}
