from train import ConsistFactory


def main(**kwargs):
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

    consist_factory.add_unit(
        class_name="DieselEngineUnit",
        weight=23,
        vehicle_length=4,
        effect_z_offset=9,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist_factory.description = """This is a big small cat."""
    consist_factory.foamer_facts = """Corsican CFD Locotracteur BB-400, South African 'Funkey' diesels, FAUR L45H B-B"""

    print("cabbage 939", consist_factory.kwargs["id"])
    """
    consist_factory.add_clone(base_numeric_id=910, clone_units=[1])

    # this is a JFDI thing, the 2-unit version varies sprites per unit position, which is generally supported, but the *buy menu* compositor does not support that as of Jan 2024, so hax
    consist_factory.clones[0].add_unit(
        class_name="DieselEngineUnit", weight=23, vehicle_length=4, spriterow_num=1
    )

    # JFDI recalculate power to account for 2 units
    consist_factory.clones[0].set_clone_power_from_clone_source()
    """
    return consist_factory
