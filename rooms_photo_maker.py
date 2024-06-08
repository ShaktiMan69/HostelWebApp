from pathlib import Path
import shutil
from glob import glob

hostels = {'b': [1,2,3], 'g': [4,5]}
for gender in ['b', 'g']:
    for hostel_num in hostels[gender]:
        for floor_num in range(1, 3):
            for room_num in range(1, 27): # TODO currently hardcoded , assuems fixed number of rooms for each hostel at a floor
                final_path = f"HC/static/assets/img/rooms/{gender}/{hostel_num}/{floor_num}/{room_num}"
                Path(final_path).mkdir(parents=True, exist_ok=True)

                # move images

                for file in glob('HC/static/assets/img/rooom/*'):
                    shutil.copyfile(file, final_path + '/' + file.split("\\")[-1])

                # input()