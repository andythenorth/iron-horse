from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="flindermouse",
        base_numeric_id=790,
        name="Flindermouse",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 2500,
        },
        speed=60,  # continues a long way into gen 3, so go faster
        gen=2,
        pantograph_type="diamond-double",
        intro_year_offset=7,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        # additional_liveries=["FREIGHT_BLACK", "BANGER_BLUE"],
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE"],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=65,
        vehicle_length=6,
        spriterow_num=0,
        repeat=2,
    )

    model_def.define_description(
        """We're giving electrics a go for freight.  Don't right know if they'll catch on, but they can pull, I give em that."""
    )
    model_def.define_foamer_facts("""NER EF1""")

    result.append(model_def)

    model_def_clone = model_def.begin_clone(base_numeric_id=34920, unit_repeats=[1])

    model_def = model_def_clone.complete_clone()

    result.append(model_def)

    return result
