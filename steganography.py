import sys
from PIL import Image

# Arguments must be correcly given
if len(sys.argv) < 3:
    print("Wrong arguments")
    print("Filename Picturename [Data to Hide]")
    exit()

# load picture and get metadata from picture
im = Image.open(sys.argv[1])
width, height = im.size
pix = im.load()

# join all arguments to get a Text
st = ' '.join(sys.argv[2:])
st += '>'

# convert text to binary
binary_st = ''.join(format(ord(i),'b').zfill(8) for i in st)

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

# remove picturetype from picturename
picturename = sys.argv[1].split('.')

im.save('{}_steganography.png'.format(picturename[0]))
print('Done.')
print('Saved as "{}_steganography.png".'.format(picturename[0]))
