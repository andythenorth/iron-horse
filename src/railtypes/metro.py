from railtype import Railtype


def main(disabled=False):
    return Railtype(
        id="metro",
        label="IHC_",
        construction_cost=10,
        maintenance_cost=10,
        railtype_flags=["RAILTYPE_FLAG_NO_LEVEL_CROSSING"],
        map_colour=0x25,
        # as of April 2022 there are no obvious appropriate labels for metro in the standardised scheme, so there are no compatible, powered or alternate types
        # this could be changed if a clear label was agreed (metro isn't just standard gauge 3rd rail like SAA3, it's an isolated dedicated system)
        compatible_railtype_list=[
            "MTRO",
        ],
        powered_railtype_list=["MTRO"],
        alternative_railtype_list=[
            "MTRO",
        ],
        use_custom_sprites=True,
        use_custom_signals=True,
    )
