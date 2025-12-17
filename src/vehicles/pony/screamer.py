from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="screamer",
        base_numeric_id=21090,
        name="Screamer",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "OHLE": 5000,
        },
        random_reverse=False,
        gen=5,
        intro_year_offset=2,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        pantograph_type="z-shaped-double",
        # railfreight grey, intercity, GNER?
        liveries=[
            "FRUIT_RIPPLE", # strictly not quite, but close enough
            "FRUIT_RIPPLE",
            "BANGER_BLUE",
            "MAIL_BY_RAIL",
            "VAPID_VOYAGER",
            "STOCK_STANDARD",
            "FREIGHTLINER_GBRF",
            "FREIGHTLINER_GBRF",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricEngineUnit",
        weight=85,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description(
        """We're knocking these out cheap enough. Look after them, they might last longer."""
    )
    model_def.define_foamer_facts("""BR Class 90""")

    result.append(model_def)

    return result
