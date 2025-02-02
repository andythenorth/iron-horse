from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="PassengerHSTCabEngineConsist",
        id="firebird",
        base_numeric_id=21500,
        name="Firebird",
        subrole="hst",  # quite a specific role, may or may not scale to other rosters
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 3300,  # it's the Deltic that never was!  It's OP, but eh, it's just cartoon trains.
        },
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH"],
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="DieselEngineUnit",
        weight=68,
        vehicle_length=8,
        capacity=16,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
        spriterow_num=0,
        tail_light="hst_32px_1",
    )

    consist_factory.define_description("""The Train of Today.""")
    consist_factory.define_foamer_facts("""BR <i>Blue Pullman</i>""")

    result.append(consist_factory)

    return result
