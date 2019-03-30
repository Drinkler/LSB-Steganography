import sys
from PIL import Image

# Text must be given as arguments
if len(sys.argv) < 2:
    print("Wrong arguments")
    exit()

# load picture and get metadata from picture
im = Image.open("space_wallpaper.jpg")
width, height = im.size
pix = im.load()

# join all arguments to get a Text
st = ' '.join(sys.argv[1:])
st += '>'

# convert text to binary
binary_st = ''.join(format(ord(i),'b').zfill(8) for i in st)

#im.show()
print('Calculating...')

i = 0
for x in range(width):
    for y in range(height):
        if i < len(binary_st):
            # get rgb of current pixel
            r, g, b = pix[x, y]

            # convert red int to binary
            binary_r = format(r, 'b').zfill(8)

            # replace the two least significent bits of red with the converted text
            new_binary_r = binary_r[:-2] + binary_st[i:i+2]

            # convert the new binary red to an int
            new_r = int(new_binary_r, 2)

            # replace current red of pixel with new red
            pix[x, y] = (new_r, g, b)
            i += 2

#im.show()
im.save('space_wallpaper_steg.png')
print('Done.')
print('Saved as "space_wallpaper_steg.png"')
