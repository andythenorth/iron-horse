# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="mka",
        base_numeric_id=10020,
        name="MKA",
        subrole="universal",
        subrole_child_branch_num=-3,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 1200,
        },
        gen=4,
        intro_year_offset=8,
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit,
        weight=55,
        vehicle_length=6,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        rel_spriterow_index=0,
    )

    consist_cabbage.description = """"""
    consist_cabbage.foamer_facts = """"""

    return consist_cabbage
