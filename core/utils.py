def queryset_to_dict(queryset, *args):
    ret = []
    for obj in queryset.values(*args):
        ret.append(obj)
    return ret


def time_durations(times):
    ret = []
    time_duration = ""

    # time = ['09:00:00', '10:00:00', '11:00:00']
    # time = ['09:00:00-10:00:00', '10:00:00-11:00:00']
    for i in range(len(times) - 1):
        time_duration += f"{times[i]} - {times[i+1]}"
        ret.append(time_duration)
        time_duration = ""

    return ret
