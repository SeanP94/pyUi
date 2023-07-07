import pygame as pg
pg.init()

fonts = pg.font.get_fonts()
fonts.sort()
for font in fonts:
    print(font)

print("fixedsys" in fonts)

