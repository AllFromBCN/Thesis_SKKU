from surprise import SVD
from surprise import Dataset
from surprise import evaluate, print_perf
import numpy


# Loading the dataset and divide it into 3 for cross-validation
filePath = '/Users/JeongSooMin/iCloud Drive(아카이브)/Desktop/Gpaper/최종보고/dataset/ml-20m/movies.csv'
reader = dataset.Reader(line_format='user item rating timestamp', sep='\t')