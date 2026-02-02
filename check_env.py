import sys 

import pandas as pd 
import sklearn
import torch

def main (): 
    print("Python:", sys.version.split()[0])
    print("pandas:", pd.__version__)
    print("scikit-learn:", sklearn.__version__)
    print("torch:", torch.__version__) 