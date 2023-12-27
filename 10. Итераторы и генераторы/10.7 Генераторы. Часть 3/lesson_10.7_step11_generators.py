def planet_features(file):
    features = {}
    for _ in range(4):
        key, value = file.readline().strip().split(' = ')
        features[key] = value
    return features

def txt_to_dict():
    with open('planets.txt') as file:
        line = 'lets some yield'
        while line:
            yield planet_features(file)
            line = file.readline()