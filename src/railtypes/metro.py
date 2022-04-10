from railtype import Railtype

def main(disabled=False):
    railtype = Railtype(
        id="metro",
    )
    railtype.register(disabled=disabled)
