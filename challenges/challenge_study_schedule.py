def study_schedule(permanence_periods, target_time):
    if target_time is None:
        return None
    count = 0
    for entry in permanence_periods:
        if not all(isinstance(val, int) for val in entry) \
                or entry[0] is None \
                or entry[1] is None \
                or entry[0] > entry[1]:
            return None
        if entry[0] <= target_time <= entry[1]:
            count += 1

    return count if count > 0 else None
