def interleave(*args):
    return (val for tp in zip(*args) for val in tp)
