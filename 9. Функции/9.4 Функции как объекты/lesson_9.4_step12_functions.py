def remove_marks(text, marks):
    remove_marks.count = remove_marks.__dict__.get('count', 0) + 1
    return ''.join(c for c in text if c not in marks)
