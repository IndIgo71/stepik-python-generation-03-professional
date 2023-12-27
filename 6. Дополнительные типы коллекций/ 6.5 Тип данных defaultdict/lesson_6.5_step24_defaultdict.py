from collections import defaultdict


def best_sender(messages, senders):
    res = defaultdict(int)
    for sender, message in zip(senders, messages):
        res[sender] += len(message.split())
    return max(reversed(res), key=res.get)
