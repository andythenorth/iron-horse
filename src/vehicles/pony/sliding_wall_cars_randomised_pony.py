from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="BoxCarSlidingWallRandomised",
        base_numeric_id=33370,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit",
        chassis="empty_16px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BoxCarSlidingWallRandomised",
        base_numeric_id=33390,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit",
        chassis="empty_24px",
    )

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------
    # starts gen 4, B and C only

    model_def = ModelDef(
        schema_name="BoxCarSlidingWallRandomised",
        base_numeric_id=30000,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BoxCarSlidingWallRandomised",
        base_numeric_id=30020,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit",
        chassis="empty_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BoxCarSlidingWallRandomised",
        base_numeric_id=30040,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit",
        chassis="empty_24px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="BoxCarSlidingWallRandomised",
        base_numeric_id=30060,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit",
        chassis="empty_32px",
    )

    result.append(model_def)

    # as of May 2025, randomised can't be used with articulated (buy menu sprite issues)

    #     model_def = ModelDef(
    #         schema_name="BoxCarSlidingWallRandomised",
    #         base_numeric_id=1950,
    #         gen=5,
    #         subtype="D",
    #         sprites_complete=True,
    #     )
    #
    #     model_def.add_unit_def(
    #         schema_name="FreightCarUnit",
    #         chassis="empty_20px",
    #         symmetry_type="asymmetric",
    #         rel_spriterow_index=0,
    #     )
    #
    #     model_def.add_unit_def(
    #         schema_name="FreightCarUnit",
    #         chassis="empty_20px",
    #         symmetry_type="asymmetric",
    #         rel_spriterow_index=4,
    #     )
    #
    #     result.append(model_def)
    #
    return result
