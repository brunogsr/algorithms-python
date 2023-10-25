def study_schedule(permanence_periods, target_time):
    if (target_time is None):
        return None

    for entry in permanence_periods:
        if (not isinstance(entry[0], int)) or (not isinstance(entry[1], int)):
            return None
        if (entry[0] is None) or (entry[1] is None):
            continue
        if (entry[0] > entry[1]):
            return None

    count = sum((1 for entry in permanence_periods if (entry[0] <= target_time) and (target_time <= entry[1])))
    return count
