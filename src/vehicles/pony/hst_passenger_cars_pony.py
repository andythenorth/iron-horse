from train import PassengerHSTCarConsist, PaxCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = PassengerHSTCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30330,
        gen=4,
        subtype="U",
        intro_year_offset=0,  # match to Firebird
        cab_id="firebird",
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="high_speed_32px")

    consist = PassengerHSTCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=30340,
        gen=5,
        subtype="U",
        intro_year_offset=-10,  # match to Blaze HST
        cab_id="blaze",
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    consist.add_unit(type=PaxCar, chassis="high_speed_32px")
