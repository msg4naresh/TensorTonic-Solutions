import torch

def create_tensor(method, shape, value=0.0):
    """
    Returns: list
    """
    if method == "ones":
        return torch.full(shape,fill_value=1.0).tolist()
    l = torch.full(shape,fill_value=value)
    
    return l.tolist()