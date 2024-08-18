import sys
import os
from PIL import Image

# grab first and second argument
source = sys.argv[1]
destination = sys.argv[2]

# check is new/ exists, if not create it.
if not os.path.exists(destination):
    os.makedirs(destination)

# loop through pokedex,
for file in os.listdir(source):
    img = Image.open(f'{source}{file}')
    clean_name = os.path.splitext(file)[0]
 
    #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
    # convert images to png and save it in the new folder.
    img.save(f'{destination}{clean_name}.png', 'png')
    print('all done!')
