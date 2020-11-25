from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext

def mapper(line):
    """
    Mapper that converts an input line to a feature vector
    """    
    feats = line.strip().split(",") 
    # labels must be at the beginning for LRSGD
    label = feats[len(feats) - 1] 
    feats = feats[: len(feats) - 1]
    feats.insert(0,label)
    features = [ float(feature) for feature in feats ] # need floats
    return LabeledPoint(label, features)

# Load and parse the data
data = sc.textFile("./dataset.txt")
parsedData = data.map(mapper)

# Train model
model = LogisticRegressionWithSGD.train(parsedData)

# Evaluating the model on training data
labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda lp: lp[0] != lp[1]).count() / float(parsedData.count())
print("Training Error = " + str(trainErr))