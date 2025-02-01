from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="higuma",
        base_numeric_id=30870,
        name="Higuma",
        subrole="express",
        subrole_child_branch_num=-2,
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 1600,  # breaks the 300 hp step size, but eh, lots of precedent  1800 hp would be too much?
        },
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "SWOOSH"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit",
        weight=60,
        vehicle_length=8,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    # https://en.wikipedia.org/wiki/New_Zealand_DL_class_locomotive
    # https://en.wikipedia.org/wiki/New_Zealand_DM_class_locomotive
    consist_factory.add_description("""A tiny mighty bear.""")
    consist_factory.add_foamer_facts(
        """KiwiRail Stadler SALi locomotives, Kawasaki (Japan) Class DF200-7000 bo-bo-bo (dedicated locomotive for JR Kysushu <i>Seven Stars in Kyushu</i> luxury train)"""
    )

    return consist_factory
