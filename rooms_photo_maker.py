from pathlib import Path
import shutil
from glob import glob

hostels = {'Boy': [1,2,3], 'Girl': [4,5]}
for gender in ['Boy', 'Girl']:
    for hostel_num in hostels[gender]:
        for floor_num in range(1, 3):
            for room_num in range(1, 27): # TODO currently hardcoded , assuems fixed number of rooms for each hostel at a floor
                final_path = f"HC/static/assets/img/rooms/{gender}/{hostel_num}/{floor_num}/{room_num}"
                Path(final_path).mkdir(parents=True, exist_ok=True)

                # move images

                for file in glob('HC/static/assets/img/rooom/*'):
                    shutil.copyfile(file, final_path + '/' + file.split("\\")[-1])

                # input()