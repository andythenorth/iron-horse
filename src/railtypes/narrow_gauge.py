from railtype import Railtype

def main(disabled=False):
    railtype = Railtype(
        id="narrow_gauge",
    )
    railtype.register(disabled=disabled)
