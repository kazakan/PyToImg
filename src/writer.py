""" Code to image """

from theme import JUSTTEXT_THEME, Theme
import tools
import keyword, tokenize
from PIL import Image, ImageDraw

import pytoken

class Writer:

    def __init__(self, path,theme=JUSTTEXT_THEME):
        self.n_row = -1
        self.n_col = -1
        self.tokens = []

        self.theme = theme
        self.colors = theme.code_color
        self.spacing = self.theme.code_spacing

        self.path = path
        self.font = theme.font_code

        self.char_width, self.char_height = tools.getcharbox(self.font)

        with open(path,'rb') as f:
            for _t in tokenize.tokenize(f.readline):
                self.n_col = max(self.n_col,_t.end[1])
                self.tokens.append(_t)
        
        if len(self.tokens) > 0 : self.n_row = self.tokens[-1].end[0]
        
    def write2img(self,img,offset=(0,0)):

        dc = ImageDraw.Draw(img)

        for _t in self.tokens:
            tok_type = _t.type

            cur_row = _t.start[0]
            cur_col = _t.start[1]

            is_long_comment = _t.string.startswith('"""') or _t.string.startswith("'''")

            if is_long_comment:
                pos = (offset[0], offset[1] + (self.char_height + self.spacing) * cur_row)
                value = _t.line
            else :
                pos = (offset[0] + self.char_width*cur_col, offset[1] + self.spacing + (self.char_height + self.spacing) * (cur_row-1))
                value = _t.string


            if keyword.iskeyword(_t.string) or _t.string in pytoken.RESERVED_WORDS: tok_type = pytoken.KEYWORD
            if _t.string in pytoken.BUILT_IN_FN : tok_type = pytoken.BUILTIN_FN
            if _t.string in pytoken.BUILT_IN_CONSTS : tok_type = pytoken.BUILTIN_CONST

            if tok_type in self.colors:
                dc.text(pos,value,fill=self.colors[tok_type],font=self.font,anchor='la')

        return img


    def code2img(self,offset=(0,0),background_color = (255,255,255)):

        img = Image.new("RGB",self.bbox(offset),background_color)

        return self.write2img(img,offset=offset)

    def bbox(self,offset=(0,0)):
        return tools.add_coord(offset,self.size())

    def size(self):
        return (self.char_width*self.n_col -1,(self.char_height + self.spacing)*self.n_row)
   
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage python2img.py [.py path]")
        exit(0)

    print("Formatting...")
    image = Writer(sys.argv[1]).code2img()
    image.show()
