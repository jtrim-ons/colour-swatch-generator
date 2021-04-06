import sys

from PIL import Image, ImageDraw

out_dir = sys.argv[2]

for line in sys.stdin.readlines():
	colour = line.strip().replace('#', '')
	size = int(sys.argv[1])
	img = Image.new('RGB', (size, size), color='#'+colour)
	img.save(out_dir + '/' + colour + '.png')

