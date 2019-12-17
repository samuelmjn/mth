class Branch():
    def __init__(self, name, address, instruments, id = None):
        self.id = id
        self.name = name
        self.address = address
        self.instruments = instruments

def to_obj(req):
    return Branch(
        id = req["_id"],
        name = req["name"],
        address = req["address"],
        instruments = req["instruments"]
    )