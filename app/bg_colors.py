from PIL import Image
from glob import glob

PRIMARY_PASTEL_COLORS = [(255, 204, 204), (255, 255, 204), (204, 255, 204), (204, 255, 255), (255, 204, 255), (204, 204, 255), (204, 204, 204)]  # (204, 204, 204) = #ccc


def glob_files():
    f = glob('./static/img/*')
    return f


def highest_range(c):
    # Find highest RGB range
    return (max(c[1]) - min(c[1]))


def brighten_colors(c):
    MAX_VALUE = 255
    increase = 90
    # Tuples are immutable
    rgb = list(c)
    # Increase brightness by set amount or until it reaches MAX_VALUE
    lighter_rgb = [x+increase if x <= MAX_VALUE-increase else 255 for x in rgb]
    # Print out values for reference
    print('original: {} brighter: {}'.format(c, lighter_rgb))
    return tuple(lighter_rgb)


def get_content():
    colors_array = []

    for f in glob_files():
        # default palette is WEB?
        # If the size is too big getcolors returns None
        # im = Image.open('./static/img/10.jpg').resize((15, 15)).convert(mode='RGB', palette='ADAPTIVE', colors=256)
        im = Image.open(f).resize((15, 15)).convert(mode='RGB', palette='ADAPTIVE', colors=255)
        # List colors in image
        colors = im.getcolors(maxcolors=256)
        # Sort colors by frequency - this makes a small difference
        colors.sort(reverse=True)
        # Sort by highest RGB range and grab top result
        interesting_color = sorted(colors, key=highest_range)[-1][1]
        # Brighten RGB variables
        final_color = brighten_colors(interesting_color)
        # Create dict of filenames + tuples wrapped in strings (for dev only)
        o = {'img': f, 'bg': str(final_color)}
        # Append dict to array
        colors_array.append(o)

    return colors_array
