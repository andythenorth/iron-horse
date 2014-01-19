registered_pipelines = {}

# colour defaults
CC1 = 198
CC2 = 80

# a convenience constant that holds a mapping for swapping CC1 and CC2 around
CC1_CC2_SWAP_MAP = {}
for i in range(8):
    CC1_CC2_SWAP_MAP[CC1 + i] = CC2 + i
    CC1_CC2_SWAP_MAP[CC2 + i] = CC1 + i
