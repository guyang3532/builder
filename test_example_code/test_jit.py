import torch

def hflip(img: torch.Tensor) -> torch.Tensor: return img.flip(-1)
print(torch.jit.script(hflip)(torch.rand(3, 8, 8)))
