import handler, sys
from PIL import Image

args = sys.argv

if len(args) > 1:
    del args[0] # delete the first argument, which is just the script filename
else:
    print('No filenames passed for arguments to de-convert, returning...')
    exit()

for arg in args:
    
    img = Image.open(str(arg))
    with open(arg.split('.')[0] + '.txt', 'w') as f:
        f.write(handler.image_to_text(img))
    
    print(f'de-converted {arg} to a text file. Saving...')