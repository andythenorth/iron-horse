from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="PassengerEngineExpressRailcar",
        model_id="borealis",
        base_numeric_id=4920,
        name="Borealis",
        subrole="express_pax_railcar",  # quite a specific role, may or may not scale to other rosters
        subrole_child_branch_num=-4,
        power_by_power_source={
            "DIESEL": 1450,
            "OHLE": 2450,
        },
        intro_year_offset=-7,  # let's be a little bit earlier for this one - keep match to HST coaches
        gen=6,
        livery_group_name="gen_6_pax_liveries_special_case_jank",  # override default liveries from gestalt
        pantograph_type="z-shaped-double",
        lgv_capable=True,  # for lolz
        tilt_bonus=True,  # for lolz
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectroDieselExpressRailcarPaxUnit",
        weight=57,
        capacity=24,
        chassis="railcar_32px",
        tail_light="railcar_32px_7",
        suppress_roof_sprite=True,
        repeat=2,
    )

    model_def.define_description(
        """"We were miles away from our real lives."""
    )
    model_def.define_foamer_facts(
        """Hitachi Class 810 <i>Aurora</i>, Class 800/801/802 families"""
    )

    result.append(model_def)

    return result
