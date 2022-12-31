from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="dreadnought",
        base_numeric_id=16510,
        name="Dreadnought",
        role="super_heavy_express",
        role_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 3300,
        },
        random_reverse=False,  # Dreadnought has asymmetric logo pixels that don't look great when running reversed
        gen=5,
        speed=125,  # Dreadnought not replaced, but has gen 6 speeds
        fixed_run_cost_points=300,  # give a small malus to this one (balancing eh?)
        additional_liveries=[],
        default_livery_extra_docs_examples=[
            ("COLOUR_PURPLE", "COLOUR_WHITE"),
            ("COLOUR_GREEN", "COLOUR_ORANGE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=102,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist.description = """This one, it does go some."""
    consist.foamer_facts = """Porterbrook Leasing Class 55 <i>Deltic</i>'"""

    return consist
