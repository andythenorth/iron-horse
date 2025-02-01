from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="constance",
        base_numeric_id=20950,
        name="Constance",
        subrole="heavy_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 3450,
            "AC": 4200,  # yes it's the very close on both, just the effect changes; this is a tech tree cheat to get an extra ~3450 hp diesel and to get a 4200 hp electric
        },
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=6,
        intro_year_offset=-2,  # introduce earlier than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        # additional_liveries=["SWOOSH", "SWOOSH", "FREIGHTLINER_GBRF"],
        sprites_complete=True,
        sprites_additional_liveries_potential=True,
    )

    consist_factory.add_unit(
        class_name="ElectroDieselEngineUnit",
        weight=95,
        vehicle_length=8,
        spriterow_num=0,
    )

    consist_factory.add_description("""Runs like a Swiss watch.""")
    consist_factory.add_foamer_facts("""Siemens Vectron Dual Mode""")

    result.append(consist_factory)

    return result
