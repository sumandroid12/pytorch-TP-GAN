import os
import sys

# To remove images without a frontal image file.

images = os.listdir(sys.argv[-1])
# os.mkdir(os.path.join(sys.argv[-1], 'clean'))
i = 0
for img in images:
    frag = img.split('_')
    frontal = '_'.join(frag[:-2]) + '_051_'+ frag[-1]
    if not os.path.exists(os.path.join(sys.argv[-1], frontal)):
        # os.rename(os.path.join(sys.argv[-1],img) , os.path.join(sys.argv[-1]+'clean', img))
        i += 1
        print(img)

print(i)