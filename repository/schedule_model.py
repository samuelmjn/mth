class Schedule():
    def __init__(self, branch, date_time, worship_leader, singers, keyboard, bass, drum, e_guitar, acc_guitar, aux_keys, id=None):
        self.id = id
        self.branch = branch
        self.date_time = date_time
        self.worship_leader = worship_leader
        self.singers = singers
        self.keyboard = keyboard
        self.bass = bass
        self.drum = drum
        self.e_guitar = e_guitar
        self.acc_guitar = acc_guitar
        self.aux_keys = aux_keys

def to_obj(req):
    return Schedule(
        id = req["_id"],
        branch = req["branch"],
        date_time = req["date_time"],
        worship_leader = req["worship_leader"],
        singers = req["singers"],
        keyboard = req["keyboard"],
        bass = req["bass"],
        drum = req["drum"],
        e_guitar = req["e_guitar"],
        acc_guitar = req["acc_guitar"],
        aux_keys = req["aux_keys"]
    )