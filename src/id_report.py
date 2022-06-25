import iron_horse
from vehicles import numeric_id_defender

def main():
    iron_horse.main()
    # when adding vehicles it's useful to know what the next free numeric ID is
    # tidy-mind problem, but do we have any vacant numeric ID slots in the currently used range?
    max_id = max(numeric_id_defender) - (max(numeric_id_defender) % 10)
    id_gaps = []
    for i in range(0, int(max_id / 10)):
        id = i * 10
        if id not in numeric_id_defender:
            id_gaps.append(str(id))
    report_content = (
        "Vacant numeric ID slots: "
        + ", ".join(id_gaps)
        + (" and from " if len(id_gaps) > 0 else "")
        + str(max_id + 10)
        + " onwards"
    )
    # 'print' eh? - but it's fine echo_message isn't intended for this kind of info, don't bother changing
    print(report_content)


if __name__ == "__main__":
    main()

