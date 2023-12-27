import pickle


def filter_dump(filename, objects, typename):
    with open(filename, mode='wb') as file:
        pickle.dump(list(filter(lambda x: isinstance(x, typename), objects)), file)
