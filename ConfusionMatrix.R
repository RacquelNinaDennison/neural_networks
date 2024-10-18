validationResults = read.csv("validation_results.csv")

actualOutput = validationResults$Actual.Output
predictedOutput = validationResults$Model.Output

confusionMatrix = table(Actual = actualOutput, Predicted = predictedOutput)
print(confusionMatrix)

testingResults = read.csv("testing_results.csv")

actualOutput = testingResults$Actual.Output
predictedOutput = testingResults$Model.Output

confusionMatrix = table(Actual = actualOutput, Predicted = predictedOutput)
print(confusionMatrix)

correct_predictions <- sum(diag(confusionMatrix))
total_predictions <- sum(confusionMatrix)
accuracy = correct_predictions / total_predictions