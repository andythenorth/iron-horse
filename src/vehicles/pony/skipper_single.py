from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailbusConsist",
        base_id="skipper_single",
        base_numeric_id=25260,
        name="Skipper",
        subrole="pax_railbus",
        subrole_child_branch_num=-3000,  # excessive child branch number to hide them from tech tree (and also -ve to hide in simplified mode)
        power_by_power_source={
            "DIESEL": 225,
        },
        gen=5,
        # introduce early by design
        intro_year_offset=-4,
        buyable_variant_group_id="skipper",  # for pony, specifically force variant group (parent) to equivalent twin-unit railbus id
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarPaxUnit",
        weight=24,
        chassis="railbus_lwb_24px",
        tail_light="railcar_24px_1",
    )

    model_def.define_description("""Patience is the virtue of the donkeys.""")
    model_def.define_foamer_facts("""BR Class 141/142/143/144 <i>Pacers</i>""")

    result.append(model_def)

    return result
