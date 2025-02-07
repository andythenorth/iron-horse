from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_def = ModelTypeFactory(
        class_name="EngineConsist",
        id="tornado",
        base_numeric_id=21750,
        name="Tornado",
        subrole="branch_express",
        subrole_child_branch_num=2,
        power_by_power_source={"DIESEL": 750, "AC": 1900},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=5,
        intro_year_offset=6,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "DB_SCHENKER", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
        sprites_additional_liveries_potential=True,  # banger blue, industrial?
    )

    model_def.define_unit(
        class_name="ElectroDieselEngineUnit",
        weight=70,
        vehicle_length=6,
        spriterow_num=0,
    )

    model_def.define_description(
        """The Boosters needed a boost. Rebuilt, repainted, off to the races we go."""
    )
    model_def.define_foamer_facts("""BR Class 74, Class 73""")

    result.append(model_def)

    return result
