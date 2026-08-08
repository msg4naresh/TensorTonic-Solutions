import torch

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    
    """

    x = torch.tensor(x,dtype = torch.float32)
    y = torch.tensor(y,dtype = torch.float32)
    if op == "add":
        result =torch.add(x,y)
    elif op == "multiply":
        result =torch.mul(x,y)
    elif op == "matmul":
        result =torch.matmul(x,y)
    elif op == "power":
        result =torch.pow(x,y)
    elif op == "max":
        result =torch.max(x,y)
    else:
        raise ValueError("Unsupported operation")
        
    
    return result.tolist()