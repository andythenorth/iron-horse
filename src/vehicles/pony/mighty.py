from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="mighty",
        base_numeric_id=14150,
        name="Mighty",
        subrole="universal",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "DIESEL": 1200,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=4,
        intro_year_offset=-15,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit",
        weight=48,
        vehicle_length=6,
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    # Irish Rail 141 / 181
    # see also https://es.wikipedia.org/wiki/Serie_1600_de_Renfe
    # see also https://en.wikipedia.org/wiki/FGC_254_Series
    consist_factory.description = """"""
    consist_factory.foamer_facts = """"""

    return consist_factory
