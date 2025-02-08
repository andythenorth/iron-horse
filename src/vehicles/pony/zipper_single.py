from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailbusConsist",
        id="zipper_single",
        base_numeric_id=25270,
        name="Zipper",
        subrole="pax_railbus",
        subrole_child_branch_num=-3000,  # excessive child branch number to hide them from tech tree (and also -ve to hide in simplified mode)
        power_by_power_source={
            "DIESEL": 280,
        },
        gen=6,
        # introduce early by design
        intro_year_offset=-4,
        buyable_variant_group_id="zipper",  # for pony, specifically force variant group (parent) to equivalent twin-unit railbus id
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="DieselRailcarPaxUnit",
        weight=25,
        chassis="railbus_lwb_24px",
        tail_light="railcar_24px_1",
    )

    model_def.define_description("""It's the same donkey, but with a new saddle.""")
    model_def.define_foamer_facts("""BR Class 144e <i>Pacer</i>, Vivarail D-Train""")

    result.append(model_def)

    return result
