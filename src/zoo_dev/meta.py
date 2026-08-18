def singleton(cls):
    """A singleton class."""
    exists = False

    def singleton_check(*args, **kwargs):
        nonlocal exists
        
        if exists:
            raise RuntimeError(f"Cannot instantiate '{cls.__name__}': An instance already exists.")
        
        # mark as exists. 
        exists = True
        
        return cls(*args, **kwargs)
        
    return singleton_check