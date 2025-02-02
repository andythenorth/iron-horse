from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="boar_cat",
        base_numeric_id=21270,
        name="Boar Cat",
        subrole="universal",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 600,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=3,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="DieselEngineUnit",
        weight=23,
        vehicle_length=4,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist_factory.define_description("""This is a big small cat.""")
    consist_factory.define_foamer_facts(
        """Corsican CFD Locotracteur BB-400, South African 'Funkey' diesels, FAUR L45H B-B"""
    )


    result.append(consist_factory)

    consist_factory = consist_factory.begin_clone(base_numeric_id=910, unit_repeats=[1])

    print("cabbage 939", consist_factory.kwargs["id"])
    # this is a JFDI thing, the 2-unit version varies sprites per unit position, which is generally supported
    # but the *buy menu* compositor does not support that as of Jan 2024, so hax
    consist_factory.unit_factories[0].kwargs["spriterow_num"] = 1
    consist_factory.define_unit(
        class_name="DieselEngineUnit", weight=23, vehicle_length=4, spriterow_num=0
    )

    consist_factory.complete_clone()

    result.append(consist_factory)

    return result
