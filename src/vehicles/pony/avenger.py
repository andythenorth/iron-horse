from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="avenger",
        base_numeric_id=21530,
        name="Avenger",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=3,
        power_by_power_source={
            "OHLE": 6200,
        },
        random_reverse=True,
        gen=5,
        pantograph_type="z-shaped-single",
        intro_year_offset=-2,  # introduce slightly earlier than gen epoch by design
        lgv_capable=True,  # for lolz
        liveries=[
            "FRUIT_RIPPLE",
            "RIDEWELL",
            "RIDEWELL",
            "VINYL_VECTOR",
            "VAPID_VOYAGER",
            "RAILFREIGHT_TRIPLE_GREY",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricEngineUnit",
        weight=100,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """Daft as a brush if you ask me.  Or mad as a badger.  Goes like stink off a shovel though."""
    )
    model_def.define_foamer_facts("""BR Class 89""")

    result.append(model_def)

    return result
