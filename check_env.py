import sys 

import pandas as pd 
import sklearn
import torch

def main (): 
    print("Python:", sys.version.split()[0])
    print("pandas:", pd.__version__)
    print("scikit-learn:", sklearn.__version__)
    print("torch:", torch.__version__) 

# Accelerator check

if torch.cuda.is_available():
    device = "cuda"
    print("GPU available: CUDA")

elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
    device = "mps"
    print("GPU available: Apple MPS")

else:
    device = "cpu"
    print("GPU not available — using CPU")

    
    
    # Tensor computation test
    x = torch.tensor([1.0, 2.0, 3.0], device=device)
    y = torch.tensor([4.0, 5.0, 6.0], device=device)
    z = x + y


    print("uv runTensor computation result:", z)
    print("Environment verification complete!")
    print()
    print()


if __name__ == "__main__":
    main()