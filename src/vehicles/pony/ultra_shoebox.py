from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="ultra_shoebox",
        base_numeric_id=21340,
        name="Ultra Shoebox",
        subrole="heavy_express",
        subrole_child_branch_num=-3,
        power_by_power_source={"DIESEL": 1650, "OHLE": 2800},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=5,
        intro_year_offset=6,  # earlier than anything IRL, but we want 125 mph capability so eh, there we go
        extended_vehicle_life=True,  # because long time until replaced
        liveries=["INVERSIONS", "VAPID_VOYAGER", "LOWER_LINES", "BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectroDieselEngineUnit",
        weight=84,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """Top to bottom, it's an old Shoebox made new. Right powerful small engines."""
    )
    model_def.define_foamer_facts(
        """Network Rail / GBRF Class 73/9 (re-engineered), BR Class 74, proposed Class 75"""
    )

    result.append(model_def)

    return result
