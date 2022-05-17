from PIL import Image,ImageFont,ImageDraw

def getcharbox(font=None):
    """
    returns (width,height) of text 'A' bounding box with given font
    """
    dummy_img = Image.new("RGB",(100,100),(0,0,0))
    dummy_dc = ImageDraw.Draw(dummy_img)

    if font is None : 
        font = ImageFont.truetype('consola.ttf', 20,encoding='unic')

    left,upper,right,lower = dummy_dc.textbbox((0,0),text='A',font=font)

    width = right - left
    height = lower - upper

    return width, height

def add_coord(t1 ,t2):
    return (t1[0]+t2[0],t1[1]+t2[1])