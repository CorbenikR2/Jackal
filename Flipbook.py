from PIL import Image
import os

# Load the flipbook image
img = Image.open('/mnt/data/T_Avatar_DiamondGrillz.png')

w, h = img.size
cols, rows = 4, 4
frame_w = w // cols
frame_h = h // rows

frames = []
for r in range(rows):
    for c in range(cols):
        box = (c * frame_w, r * frame_h, (c+1)*frame_w, (r+1)*frame_h)
        frame = img.crop(box)
        frames.append(frame)

gif_path = '/mnt/data/diamond_grillz.gif'
frames[0].save(
    gif_path,
    save_all=True,
    append_images=frames[1:],
    duration=80,
    loop=0
)

gif_path
