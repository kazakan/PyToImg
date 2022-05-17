from abc import ABCMeta, abstractmethod
from PIL import Image,ImageDraw,ImageFont

from tools import add_coord, getcharbox

class Component(metaclass=ABCMeta):

    def __init__(self,offset=(0,0),color=(0,0,0)):
        self.offset = offset
        self.color = color

    @abstractmethod
    def draw(self,img : Image):
        raise NotImplementedError('draw NotImplemented')

class Rectangle(Component):

    def __init__(self,offset=(0,0),size=(0,0),color=(0,0,0)):
        super().__init__(offset,color)
        self.size=size

    def draw(self,img : Image):
        dc = ImageDraw.Draw(img)
        dc.rectangle(self.bbox,fill=self.color)

    @property
    def bbox(self):

        return (self.offset[0],self.offset[1],self.offset[0]+self.size[0],self.offset[1]+self.size[1])

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]


class TitleBar(Rectangle):
    
    def __init__(self,offset=(0,0),size=(0,0),color=(0,0,0),title='',font=None,text_color = (0,0,0)):
        super().__init__(offset,size,color)
        self.title = title
        self.font = font if font is not None else ImageFont.truetype('consola.ttf', 20,encoding='unic')
        self.text_color = text_color
    
    def draw(self, img: Image):
        super().draw(img)

        dc = ImageDraw.Draw(img)
        pos = (self.offset[0],self.offset[1])
        dc.text(pos,text=self.title,font=self.font,fill=self.text_color)
        

class CodeArea(Rectangle):

    def __init__(self,offset=(0,0),size=(0,0),color=(0,0,0),writer=None,codeoffset=(0,0)):
        super().__init__(offset,size,color)
        self.writer=writer
        self.codeoffset=codeoffset

    def draw(self, img: Image):
        super().draw(img)

        if self.writer is not None:
            self.writer.write2img(img,offset=add_coord(self.offset,self.codeoffset))

class LineNum(Rectangle):
    def __init__(self,linenum,offset=(0,0),size=(0,0),color=(0,0,0),font=None,spacing=10,cbox=None,text_color=(0,0,0)):
        super().__init__(offset,size,color)
        self.linenum = linenum
        self.font = font if font is not None else ImageFont.truetype('consola.ttf', 20,encoding='unic')
        self.spacing=spacing
        self.cbox = cbox if cbox is not None else getcharbox(self.font)
        self.text_color = text_color

    def draw(self, img: Image):
        super().draw(img)

        dc = ImageDraw.Draw(img)
        for i in range(self.linenum):
            pos = (self.offset[0]+self.size[0],self.offset[1] + self.spacing + (self.cbox[1] + self.spacing) * i)
            dc.text(pos,text=str(i+1),font=self.font,anchor='ra',fill=self.text_color)
