from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailcar",
        base_id="zeus",
        base_numeric_id=25830,
        name="Zeus",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 620,
        },
        pantograph_type="z-shaped-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        gen=6,
        sprites_complete=True,
        intro_year_offset=-3,
    )  # introduce early by design

    model_def.add_unit_def(
        class_name="ElectricRailcarPaxUnit",
        weight=39,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    model_def.define_description("""Gets you from A to Z and back.""")
    model_def.define_foamer_facts("""BR Class 365 <i>Networker Express</i>""")

    result.append(model_def)

    return result
