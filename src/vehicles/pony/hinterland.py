from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        roster_id=roster_id,
        id="hinterland",
        base_numeric_id=21740,
        name="Hinterland",
        subrole="universal",
        subrole_child_branch_num=-5,
        power_by_power_source={
            "DIESEL": 1200,
        },
        random_reverse=True,
        base_track_type_name="NG",
        gen=3,
        intro_year_offset=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit",
        weight=58,
        vehicle_length=8,
        effect_z_offset=11,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist_factory.description = """Our pride, a force from overseas. Thrives in the solitude of the frontier or the clamor of the mills."""
    consist_factory.foamer_facts = """Alco RSD8 / DL351"""

    return consist_factory
