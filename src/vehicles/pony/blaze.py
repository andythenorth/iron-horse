from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineHSTCab",
        base_id="blaze",
        base_numeric_id=21640,
        name="Blaze HST",
        subrole="hst",  # quite a specific role, may or may not scale to other rosters
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 5000,
        },
        intro_year_offset=-10,  # let's be a little bit earlier for this one - keep coaches matched
        gen=5,
        lgv_capable=True,  # for lolz
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[
            "BANGER_BLUE",
            "WHITE_STRIPE_1995",
            "SWOOSH_1995",
            "SWOOSH_1995",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=70,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
        spriterow_num=0,
        tail_light="hst_32px_1",
    )

    model_def.define_description("""Power is of the essence. Faster is everything.""")
    model_def.define_foamer_facts("""BR Class 43 (High Speed Train)""")

    result.append(model_def)

    return result
