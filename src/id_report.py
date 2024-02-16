import global_constants
import iron_horse


def find_vacant_id_runs(numeric_id_defender, lower_bound, upper_bound):
    unused_ids = []
    for i in range(int(lower_bound / 10), int(upper_bound / 10)):
        id = i * 10
        if id not in iron_horse.roster_manager.numeric_id_defender:
            unused_ids.append(id)
    id_runs = []
    run = []
    unused_ids.sort()
    for count, unused_id in enumerate(unused_ids):
        # first loop
        if count == 0:
            run.append(unused_id)
        # all other loops
        else:
            previous_id = unused_ids[count - 1]
            if (unused_id - previous_id) == 10:
                # run continues
                run.append(unused_id)
            else:
                id_runs.append(run)
                run = [unused_id]
        if count == len(unused_ids) - 1:
            # if last, close the run
            id_runs.append(run)
        else:
            previous_id = unused_id
    result = []
    for id_run in id_runs:
        result.append(sorted([min(id_run), max(id_run)]))
    return result


def main():
    iron_horse.main()
    # when adding vehicles it's useful to know what the next free numeric ID is
    # tidy-mind problem, but do we have any vacant numeric ID slots in the currently used range?

    id_gaps_articulated = find_vacant_id_runs(
        iron_horse.roster_manager.numeric_id_defender,
        0,
        global_constants.max_articulated_id - 10,
    )
    id_gaps_non_articulated = find_vacant_id_runs(
        iron_horse.roster_manager.numeric_id_defender,
        global_constants.max_articulated_id + 10,
        # yolo 65k why not
        65000,
    )
    report_content = ""
    for label, id_runs in {
        "Articulated IDs": id_gaps_articulated,
        "Non-Articulated IDs": id_gaps_non_articulated,
    }.items():
        id_gaps = []
        for id_run in id_runs:
            if id_run[0] == id_run[1]:
                # single id
                id_gaps.append(str(id_run[0]))
            else:
                # range of ids
                id_gaps.append(" to ".join([str(id) for id in id_run]))
        report_content += "Vacant " + label + ":\n" + ", ".join(id_gaps) + "\n"
    # 'print' eh? - but it's fine echo_message isn't intended for this kind of info, don't bother changing
    print(report_content)


if __name__ == "__main__":
    main()
