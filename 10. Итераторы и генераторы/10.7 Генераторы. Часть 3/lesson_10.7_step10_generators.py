def nonempty_lines(file):
    with open(file, encoding='utf-8') as f:
        yield from (line.strip() if len(line.strip()) < 26 else '...' for line in f if line.strip())
