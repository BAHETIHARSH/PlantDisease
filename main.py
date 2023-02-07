from diseaseDetection import *
from prePreocess import *


path = "early.JPG"

data = preprocess(path)
disease = predictDisease(data)

print(disease)
