import handler, sys, os

args = sys.argv

if len(args) > 1:
    del args[0] # delete the first argument, which is just the script filename
else:
    print('No filenames passed for arguments to convert, returning...')
    exit()

for arg in args:
    with open(arg) as f:
        try:
            contents = f.read()
        except:
            print('Error: Can convert file that isn\'t text. Exiting...')
            exit()
        img = handler.text_to_image(str(contents))
        save_path = os.path.join(os.getcwd(), os.path.basename(arg).split('.')[0] + '.png')
        img.save(save_path)
        print(f'Converted {arg} to an image. Saving to {save_path}')