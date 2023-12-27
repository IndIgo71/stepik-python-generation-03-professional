def spell(*args):
    return {first_letter.lower(): max(map(lambda x: len(x) if x.startswith(first_letter) else 0, args))
            for first_letter in [item[0] for item in args]}
