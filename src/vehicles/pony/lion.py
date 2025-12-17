from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="lion",
        base_numeric_id=20960,
        name="Lion",
        subrole="super_heavy_freight",
        subrole_child_branch_num=3,
        power_by_power_source={
            "DIESEL": 3500,  # first high HP diesel in this roster - not too high because replaced by 3450 HP diesels in gen 5
        },
        speed=87,  # these don't *have* to be replaced at game end
        random_reverse=True,
        gen=4,
        intro_year_offset=11,  # let's be later for this one
        liveries=["INVERSIONS", "BANGER_BLUE", "INVERSIONS"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="DieselEngineUnit",
        weight=132,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
    )

    model_def.define_description("""Good horses make short miles.""")
    model_def.define_foamer_facts(
        """Brush HS4000 Kestrel prototype, BRCW / BR D0260 Lion prototype"""
    )

    result.append(model_def)

    return result
