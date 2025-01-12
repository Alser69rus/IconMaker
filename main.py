from PIL import Image, ImageFont, ImageDraw, ImageOps
from pathlib import Path

text = input('Введите номер проекта:')

for file in Path('img').iterdir():
    im = Image.new('RGB', (256, 256), 'white')
    background = Image.open(file)
    background2 = ImageOps.pad(background, (256, 180),color='white')
    im.paste(background2)
    font = ImageFont.truetype('arial.ttf', 72)
    d = ImageDraw.Draw(im)
    d.text((256, 256), text, 'red', font, 'rd')
    filename=Path('icon')/Path(file.stem+'.ico')
    im.save(filename)

