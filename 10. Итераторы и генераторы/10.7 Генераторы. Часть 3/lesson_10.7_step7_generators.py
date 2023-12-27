def filter_names(names, ignore_char, max_names):
    filtered_names = (
        name
        for name in names
        if not (name.lower().startswith(ignore_char.lower()) or any(map(str.isdigit, name)))
    )
    return (name for i, name in enumerate(filtered_names) if i < max_names)
