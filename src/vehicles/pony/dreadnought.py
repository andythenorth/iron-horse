from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="dreadnought",
        base_numeric_id=16510,
        name="Dreadnought",
        subrole="super_heavy_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 3450,
        },
        random_reverse=False,  # Dreadnought has asymmetric logo pixels that don't look great when running reversed
        gen=5,
        replacement_consist_id="defiant",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PURPLE", "COLOUR_WHITE"),
            ("COLOUR_GREEN", "COLOUR_ORANGE"),
        ],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit",
        weight=102,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist_factory.description = """This one, it does go some."""
    consist_factory.foamer_facts = """Porterbrook Leasing Class 55 <i>Deltic</i>'"""

    return consist_factory
