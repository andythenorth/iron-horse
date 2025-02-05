from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="EngineConsist",
        id="trojan",
        base_numeric_id=21450,
        name="Trojan",
        subrole="freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1750,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=6,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="DieselEngineUnit", weight=95, vehicle_length=8, spriterow_num=0
    )

    model_type_factory.define_description("""Steel yourself, this one's on the move.""")
    model_type_factory.define_foamer_facts(
        """GEC Stephenson steel mill locomotives, Alco RSD-1 export switcher"""
    )

    result.append(model_type_factory)

    return result
