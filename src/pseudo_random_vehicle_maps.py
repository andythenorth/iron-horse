import random

"""
Pre-compiled determinstic random maps, for randomised vehicles that use pseudo-random sequences.

Provides multiple types of train configuration based on Car Type Diversity and Sequence Entropy.

Train Types and Description Table:
------------------------------------------------------------------------------------------------------------------------------------------------------------
Train Type                  | Car Type Diversity | Sequence Entropy               | Notes
------------------------------------------------------------------------------------------------------------------------------------------------------------
Pure Block Train            | 0                  | 0                              | Fully uniform train with identical cars throughout.
Block with Minor Variation  | Low (0.1 - 0.3)    | Low but Random (0.3-0.4)       | Mostly uniform block train with small variations or substitutions.
Segmented Block Train       | Moderate (0.3-0.5) | Moderate, Structured (0.3-0.5) | Limited car types, highly structured into distinct blocks.
Mixed, One Type More Common | Moderate (0.5-0.7) | Moderate to High (0.5-0.7)     | A mixed train with various car types, but one type predominates.
Loose Mixed Train           | High (0.7-1.0)     | High (0.8-1.0)                 | Randomly arranged train with a variety of car types and little structure.
------------------------------------------------------------------------------------------------------------------------------------------------------------

ASCII Plot of Train Classifications:
    Entropy (Sequence Entropy - Y-axis)
    1.0 |                                        * Loose Mixed Train
        |
    0.8 |
        |
    0.6 |                                * Mixed, One Type More Common
        |
    0.4 |                      * Segmented Block Train
        |                      * Block with Minor Variation
    0.2 |
        |
    0.0 |* Pure Block Train
        |_____________________________________________________
            0.0    0.2     0.4      0.6      0.8      1.0
                      Car Type Diversity (X-axis)

Explanation:
- Car Type Diversity (X-axis): Measures the variety of car types in the train.
- Sequence Entropy (Y-axis): Measures the randomness or structure in the sequence of car types.
- The chart visually represents the different classifications of trains based on these two dimensions.
"""

# Define the configuration for each type of map
map_configurations = {
    # pure block train is not provided as random for obvious reasons
    "map_block_train_with_minor_variation": {
        "min_run": 1,  # Max run set to 1 for consistency
        "max_run": 1,
        "prefer_run_lengths": {1: 1.0},  # Every wagon is its own 'run'
        "seed": 45,
        "predominance_fraction": 0.625,  # predominance applied to 5/8 of the map
    },
    "map_segmented_block_train": {
        "min_run": 3,
        "max_run": 4,
        "prefer_run_lengths": {3: 0.5, 4: 0.5},
        "seed": 42,
        "predominance_fraction": 0,
    },
    "map_mixed_train_one_car_type_more_common": {
        "min_run": 1,
        "max_run": 5,
        "prefer_run_lengths": {1: 0.2, 2: 0.3, 3: 0.2, 4: 0.2, 5: 0.1},
        "seed": 44,
        "predominance_fraction": 0.25,  # predominance applied to 1/4 of the map
    },
    "map_loose_mixed_train": {
        "min_run": 1,
        "max_run": 2,
        "prefer_run_lengths": {1: 0.5, 2: 0.5},
        "seed": 43,
        "predominance_fraction": 0,
    },
}


def generate_predominance_based_map(
    size=64, value_range=16, predominance_fraction=0.25, min_run=2, max_run=5
):
    """
    Generate a list of values where one value appears as a specific fraction of entries, and all other values are randomised.
    This method supports providing a predominant car type, then attempts to meet slice constraints approximately.
    This method can produce highly shuffled sequences, with a tuneable bias towards one type of car.

    :param size: Total size of the final list (default 64)
    :param value_range: Range of possible random values (including predominant value)
    :param predominance_fraction: Fraction of the list to be filled with the predominant value
    :param min_run: Minimum run size
    :param max_run: Maximum run size
    :return: A combined list with random slices from the sorted list, ensuring correct proportions
    """
    num_predominant = int(size * predominance_fraction)
    num_other = size - num_predominant

    predominant_value = random.randint(0, value_range - 1)
    predominant_list = [predominant_value] * num_predominant

    other_list = []
    while len(other_list) < num_other:
        rand_value = random.randint(0, value_range - 1)
        if rand_value != predominant_value:
            other_list.append(rand_value)

    full_list = predominant_list + other_list
    full_list.sort()

    final_result = []
    while full_list:
        slice_size = min(random.randint(min_run, max_run), len(full_list))
        offset = random.randint(0, len(full_list) - 1)
        final_result.extend(full_list[offset : offset + slice_size])
        del full_list[offset : offset + slice_size]

    assert len(final_result) == size, "Final list size does not match target size"
    actual_predominant_fraction = final_result.count(predominant_value) / size
    assert (
        abs(actual_predominant_fraction - predominance_fraction) < 0.05
    ), "Predominant value proportion deviation"

    return final_result


def generate_run_based_map(
    size=64, value_range=16, min_run=2, max_run=5, prefer_run_lengths=None
):
    """
    Generate a list of values with predictable runs based on predefined run lengths.
    This method doesn't support providing a predominant car type.
    This method can produce highly structured maps.

    :param size: Total size of the list
    :param value_range: Range of possible random values (0 to value_range-1)
    :param min_run: Minimum run size
    :param max_run: Maximum run size
    :param prefer_run_lengths: A dictionary with run lengths and their probabilities
    :return: A list of values with runs of predictable length
    """
    if prefer_run_lengths is None:
        prefer_run_lengths = {1: 1.0}

    map_entries = []
    while len(map_entries) < size:
        run_length = random.choices(
            population=list(prefer_run_lengths.keys()),
            weights=[
                prefer_run_lengths.get(length, 0.1)
                for length in prefer_run_lengths.keys()
            ],
            k=1,
        )[0]

        run_value = random.randint(0, value_range - 1)
        run_length = min(
            run_length, size - len(map_entries)
        )  # Ensure the run fits within the remaining space
        map_entries.extend([run_value] * run_length)

    return map_entries


def get_deterministic_random_vehicle_maps(
    map_type, num_maps=64, map_size=64, value_range=64
):
    """
    Generate multiple random maps based on a predefined configuration.

    :param map_type: The string key to determine which map configuration to use
    :param num_maps: The number of maps to generate
    :param map_size: The number of entries per map
    :param value_range: The range of random values for candidates
    :return: A list of unique maps
    """
    if map_type not in map_configurations:
        raise ValueError(f"Unknown map type: {map_type}")

    # Get the config for the selected map type
    config = map_configurations[map_type]

    random.seed(config["seed"])  # Set the seed for determinism

    maps = set()
    for _ in range(num_maps):
        # Note that attempting to enforce both sequence pattern (runs) and car prevalence (predominance fraction) is too complex, so choose one or the other.
        if config["predominance_fraction"] > 0:
            # Use the balanced random slicing method for predominance maps
            new_map = tuple(
                generate_predominance_based_map(
                    size=map_size,
                    value_range=value_range,
                    predominance_fraction=config.get("predominance_fraction", 0),
                    min_run=config["min_run"],
                    max_run=config["max_run"],
                )
            )
        else:
            # Use the run-based map generation method
            new_map = tuple(
                generate_run_based_map(
                    size=map_size,
                    value_range=value_range,
                    min_run=config["min_run"],
                    max_run=config["max_run"],
                    prefer_run_lengths=config["prefer_run_lengths"],
                )
            )

        maps.add(new_map)

    return [list(map_entry) for map_entry in maps]
