#! /bin/env python3
import numpy
import subprocess
inkscape = "/usr/bin/inkscape" # path to inkscape executable

input_svg_path = ["NeXus_Logo.svg","NeXus_Logo_dark.svg"]
output_png_path = ["bitmaps/NeXus_Logo_","bitmaps/NeXus_Logo_dark_"]
width = [100,1000,10000]

for i in [0,1]:
    for w in width:
        # read svg file -> write png file
        subprocess.run([inkscape, '--export-type=png', f'--export-filename={output_png_path[i]}{w}.png', f'--export-width={w}', input_svg_path[i]])


input_svg_path = ["NeXus_Logo_square.svg","NeXus_Logo_dark_square.svg"]
output_png_path = ["bitmaps/NeXus_Logo_square_","bitmaps/NeXus_Logo_dark_square_"]
width = [16,32,48,64,128,180,192,228,256]

for i in [0,1]:
    for w in width:
        # read svg file -> write png file
        subprocess.run([inkscape, '--export-type=png', f'--export-filename={output_png_path[i]}{w}.png', f'--export-width={w}', input_svg_path[i]])



print('done')
