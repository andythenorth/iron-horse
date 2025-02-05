from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="EngineConsist",
        id="borax",
        base_numeric_id=24780,
        name="Borax",
        subrole="metro",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "METRO": 950,
        },
        random_reverse=True,
        gen=2,
        intro_year_offset=1,  # introduce later than gen epoch by design
        fixed_run_cost_points=120,  # substantial cost bonus for balance against same-era steam engines
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="MetroUnit", weight=60, vehicle_length=8, spriterow_num=0
    )

    model_type_factory.define_description(
        """Is London drowning? Because I live by the river."""
    )
    model_type_factory.define_foamer_facts("""Metropolitan Railway electric locos""")

    result.append(model_type_factory)

    return result
