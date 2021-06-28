# Add the functions in this file
import json


def load_journal(fp):
    f = open(fp)
    data = json.load(f)
    return data


def compute_phi(fp, event):
    data = load_journal(fp)
    n11 = 0
    n00 = 0
    n10 = 0
    n01 = 0

    n1_ = 0
    n0_ = 0
    n_1 = 0
    n_0 = 0
    for dic in data:
        if event in dic["events"]:
            n1_ += 1
            if dic['squirrel']:
                n11 += 1
            else:
                n10 += 1
        if not event in dic["events"]:
            n0_ += 1
            if dic['squirrel']:
                n01 += 1
            else:
                n00 += 1
        if dic['squirrel']:
            n_1 += 1
        else:
            n_0 += 1

    k = (n1_ * n0_ * n_1 * n_0) ** 0.5
    m = (n11 * n00 - n10 * n01)
    return m/k


def compute_correlations(fp):
    data = load_journal(fp)
    event = []
    for dic in data:
        for even in dic['events']:
            if not even in event:
                event.append(even)
    corel = {}
    for even in event:
        val = compute_phi(fp, even)
        corel[even] = val
    return corel


def diagnose(fp):
    data = compute_correlations(fp)
    max_key = max(data, key=data.get)
    min_key = min(data, key=data.get)
    return max_key, min_key
