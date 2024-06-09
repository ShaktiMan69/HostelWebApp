import random
from HC import db, create_app
from HC.models import Hostel, Rooms

app = create_app()
with app.app_context():
    n_rooms_in_each_hostel = [h.as_dict()['nrooms'] for h in Hostel.query.all()]

    wId = 0
    for index, n_rooms in enumerate(n_rooms_in_each_hostel):
        if index % 2 == 0:
            wId += 1
            floor = 1
        else:
            floor = 2

        if floor == 2:
            start = prev_rooms + 1
        else:
            start = 1

        if wId > 3:
            gender = 'g'
        else:
            gender = 'b'

        print(wId, gender, floor, start, start+n_rooms)
        # input()
        for i in range(start, start+n_rooms):
            room = Rooms(warden_id=wId, hostel_id=wId, room_num=i, gender=gender, floor_num=floor, is_occupied=bool(random.getrandbits(1)))
            db.session.add(room)

        prev_rooms = n_rooms


    db.session.commit()