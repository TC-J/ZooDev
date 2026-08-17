def singleton(cls):
    """A class decorator that enforces a 
		strict singleton pattern.
    """
    has_instance = False

    
    def get_instance(*args, **kwargs):
        nonlocal has_instance
        if has_instance:
            raise RuntimeError(f"Cannot instantiate '{cls.__name__}': An instance already exists.")
        
        # Mark as created and return the single allowed instance
        has_instance = True
        return cls(*args, **kwargs)
        
    return get_instance

    

def track_instances(cls):
    """
    A modern class decorator that tracks all active instances 
    without causing memory leaks.
    """
    # A WeakSet automatically discards objects when they are garbage-collected
    instances = weakref.WeakSet()

    # Intercept object creation using __new__ instead of __init__
    original_new = cls.__new__

    def new_new(cls_target, *args, **kwargs):
        # 1. Handle object creation safely, even for object built-ins
        if original_new is object.__new__:
            instance = original_new(cls_target)
        else:
            instance = original_new(cls_target, *args, **kwargs)
        
        # 2. Track the instance immediately
        instances.add(instance)
        return instance

    # Override __new__ instead of __init__ to avoid breaking inheritance
    cls.__new__ = new_new

    # Attach the explicit tracking retrieval method
    @staticmethod
    def get_instances():
        return list(instances)

    cls.get_instances = get_instances
    return cls

