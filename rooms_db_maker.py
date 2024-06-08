from HC import db, create_app
from HC.models import Hostel, Rooms

app = create_app()
with app.app_context():
    n_rooms_in_each_hostel = [h.as_dict()['nrooms'] for h in Hostel.query.all()]

    wId = 1
    for n_rooms in n_rooms_in_each_hostel:
        for i in range(1, n_rooms+1):
            room = Rooms(warden_id=wId, hostel_id=wId, room_num=i)
            db.session.add(room)
        wId += 1

    db.session.commit()