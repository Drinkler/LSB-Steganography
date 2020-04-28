# Steganography :framed_picture:

[![Build Status](https://travis-ci.com/Drinkler/LSB-Steganography.svg?branch=master)](https://travis-ci.com/Drinkler/LSB-Steganography)

My first and one of the simplest ways of steganography.

run "python3 steganography.py Picturename [Data which you would like to hide]" to Hide the data in the picture.
E.g:

```
python3 steganography.py space_wallpaper.jpg This should be the hidden data
```

run "python3 decrypt_steganography.py Picturename [File to which the data will be saved]" to get the hidden data from the picture.
E.g:

```
python3 decrypt_steganography.py space_wallpaper_steganography.png data.txt
```

# Max Data Size

"Max Data Size in Byte" = "Image height" _ "Image width" _ 0.25
