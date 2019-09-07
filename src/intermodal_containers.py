registered_container_gestalts = ["intermodal_box_16px",
                                 "intermodal_box_24px",
                                 "intermodal_box_32px",
                                 "intermodal_bulk_16px",
                                 "intermodal_bulk_24px",
                                 "intermodal_bulk_32px",
                                 "intermodal_edibles_tank_16px",
                                 "intermodal_edibles_tank_24px",
                                 "intermodal_edibles_tank_32px",
                                 "intermodal_flat_16px",
                                 "intermodal_flat_24px",
                                 "intermodal_flat_32px",
                                 "intermodal_livestock_16px",
                                 "intermodal_livestock_24px",
                                 "intermodal_livestock_32px",
                                 "intermodal_reefer_16px",
                                 "intermodal_reefer_24px",
                                 "intermodal_reefer_32px",
                                 "intermodal_tank_16px",
                                 "intermodal_tank_24px",
                                 "intermodal_tank_32px"]

def get_container_types():
    return {'bulk': [1, 2, 3], 'reefer': [1, 2, 3], 'box': [1, 2, 3], 'tank': [1, 2, 3],
            'livestock': [1, 2, 3], 'flat': [1, 2, 3], 'edibles_tank': [1, 2, 3]}


def main():
    print("Intermodal Containers!")
