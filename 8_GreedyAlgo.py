
#state
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

#radio stations list
stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["mt", "wa", "id"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"])
}

final_stations = set()

while states_needed:
    best_stations = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_stations = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_stations)
    del stations[best_stations] #newline 

print(final_stations)