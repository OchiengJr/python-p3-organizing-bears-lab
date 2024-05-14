def pytest_itemcollected(item):
    # Extract the parent and node objects
    par = item.parent.obj if item.parent else None
    node = item.obj if hasattr(item, 'obj') else None
    
    # Get the prefix and suffix for the test item name
    pref = par.__doc__.strip() if par and par.__doc__ else par.__class__.__name__ if par else ''
    suf = node.__doc__.strip() if node and node.__doc__ else node.__name__ if node else ''
    
    # Construct the nodeid based on prefix and suffix
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))
