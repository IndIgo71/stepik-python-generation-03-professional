def parse_ranges(ranges):
    return (
        i
        for r in ranges.split(',')
        for i in range(int(r.split('-')[0]), int(r.split('-')[1]) + 1)
    )
