from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineRailbus",
        model_id="clipper_single",
        base_numeric_id=25250,
        name="Clipper",
        subrole="pax_railbus",
        subrole_child_branch_num=-3000,  # excessive child branch number to hide them from tech tree (and also -ve to hide in simplified mode)
        power_by_power_source={
            "DIESEL": 180,
        },
        gen=4,
        # introduce early by design
        intro_year_offset=-4,
        buyable_variant_group_id="clipper",  # for pony, specifically force variant group (parent) to equivalent twin-unit railbus id
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselRailcarPaxUnit",
        weight=22,
        chassis="railbus_swb_24px",
        tail_light="railcar_24px_1",
    )

    model_def.define_description(
        """The horses of hope gallop, but the donkeys of experience go slowly."""
    )
    model_def.define_foamer_facts(
        """BR 1st generation AC Cars/Wickham/Waggon-und Maschinenbau and similar railbuses"""
    )

    result.append(model_def)

    return result
