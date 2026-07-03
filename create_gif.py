import imageio.v3 as iio
import glob

images = [ ]

filenames = sorted(glob.glob("shrek/*.png"))

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('shrek.gif', images, duration = 100, loop = 0)
print("GIF created successfully!")