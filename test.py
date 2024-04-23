import torch
print(torch.cuda.is_available())
import numpy as np
rng = np.random.default_rng(123)

print(rng.integers(low=0, high=5))
print(rng.integers(low=0, high=5))
print(rng.integers(low=0, high=5))
# print(rng.random())
# print(rng.random())