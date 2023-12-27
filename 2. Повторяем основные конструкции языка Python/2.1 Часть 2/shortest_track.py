d1, d2, d3 = [int(input()) for _ in range(3)]
track_v1 = d1 + d2 + d3
track_v2 = (d1 + d2) * 2
track_v3 = min((d1 + d3) * 2, (d2 + d3) * 2)
print(min([track_v1, track_v2, track_v3]))
