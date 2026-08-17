

def ft_filter(f, lst, /):
    ''' Return an iterator yielding those items of iterable for \
which function(item)
is true. If function is None, return the items that are true. '''
    newlist = [x for x in lst if f(x)]
    return newlist
