def sort_priority(values, group):
    values.sort(key=lambda x: (x not in group, x))
