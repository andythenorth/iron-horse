from train import TGVCabEngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = TGVCabEngineConsist(
        roster_id=roster_id,
        id="helm_wind_cab",
        base_numeric_id=12100,
        name="Helm Wind",
        role="very_high_speed",
        role_child_branch_num=1,
        power_by_power_source={
            "AC": 1700,
        },
        dual_headed=True,
        pantograph_type="z-shaped-single-reversed",
        gen=5,
        intro_year_offset=-3,  # introduce earlier than gen epoch by design
        additional_liveries=["GNER"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit,
        weight=76,
        # no pax capacity on Helm Wind cabs
        capacity=0,
        spriterow_num=0,
        chassis="4_axle_solid_express_32px",
        tail_light="very_high_speed_32px_1",
    )

    consist.description = """Can we get there faster? That's what drives me."""
    consist.foamer_facts = (
        """BR InterCity 225 (Class 91), Shinkansen-style distributed traction"""
    )

    return consist
