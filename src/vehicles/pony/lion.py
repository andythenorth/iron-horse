from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="lion",
        base_numeric_id=20960,
        name="Lion",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 3300,  # first high HP diesel in this roster??
        },
        speed=87,  # for lolz
        random_reverse=True,
        gen=4,
        intro_year_offset=12,  # let's be later for this one, it's long-lived also
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE", "SWOOSH"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=132,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
    )

    model_def.define_description("""Good horses make short miles.""")
    model_def.define_foamer_facts(
        """BRCW / BR D0260 Lion prototype, Brush HS4000 Kestrel prototype"""
    )

    result.append(model_def)

    return result
