from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="sizzler",
        base_numeric_id=21410,
        name="Sizzler",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=4,
        power_by_power_source={
            "AC": 7200,
        },
        random_reverse=True,
        gen=6,
        intro_year_offset=2,  # introduce later than gen epoch by design
        lgv_capable=True,  # for lolz
        extended_vehicle_life=True,
        pantograph_type="z-shaped-double",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ElectricEngineUnit", weight=82, vehicle_length=8, spriterow_num=0
    )

    model_def.define_description(
        """Looks like a cheese to me, goes alright though."""
    )
    model_def.define_foamer_facts(
        """proposed Bombardier Traxx P200, various electric locomotives from Stadler, Siemens, Adtranz"""
    )

    result.append(model_def)

    return result
