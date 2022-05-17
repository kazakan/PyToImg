from writer import Writer
from theme import JUSTTEXT_THEME, MONAKAI_THEME, Theme
from tools import add_coord, getcharbox

from components import *

# values for title setting

TITLE_FULL_PATH = 0
TITLE_WITH_EXT = 1
TITLE_ONLY_NAME = 2


class Windows:

    def __init__(self,
                path : str,
                winsize = None,
                adaptive_size = True, # not implemented yet
                theme : Theme = JUSTTEXT_THEME,
                title_type = TITLE_WITH_EXT
                ):

        self.writer=Writer(path,theme)
        self.theme=theme
        self.winsize = winsize
        self.adaptive_size = adaptive_size
        self.title_type = title_type

        # size setting
        self._size = None

        if self.adaptive_size:
            tmp = self.writer.size()
            tmp = add_coord(
                tmp,
                (self.theme.window_linenum_width,self.theme.window_title_height)
            )
            self._size = tmp
        elif self.winsize is not None:
            self._size = self.winsize
        else :
            self._size = self.theme.window_size

        # title setting
        self.title=path

        if title_type == TITLE_WITH_EXT:
            self.title = path.split('/')[-1]
        elif title_type == TITLE_ONLY_NAME:
            self.title = path.split('/')[-1].split('.')[0]


    def draw(self):

        # create base image
        img = Image.new("RGB",self._size,self.theme.color_default)

        # set elements
        elements = [
            TitleBar(color=self.theme.color_title_bg,
                size=(img.size[0],self.theme.window_title_height),
                title=self.title,
                font=self.theme.font_title, 
                text_color=self.theme.color_title_text),

            CodeArea(color=self.theme.color_code_bg,
                offset=(self.theme.window_linenum_width,self.theme.window_title_height),
                size=(img.size[0],img.size[1]-self.theme.window_title_height),
                writer=self.writer,
                codeoffset=(self.theme.window_code_lpad,0)),

            LineNum(color=self.theme.color_linenum_bg,
                offset=(0,self.theme.window_title_height),
                size=(self.theme.window_linenum_width,img.size[1]-self.theme.window_title_height),
                linenum=self.writer.n_row,
                font=self.theme.font_linenum,
                cbox=getcharbox(self.theme.font_code),
                text_color=self.theme.color_linenum_text,
                spacing=self.theme.code_spacing)
        ]

        # draw elements to img
        for ele in elements:
            ele.draw(img)

        return img

if __name__ == "__main__":
    import sys

    # path to code
    path_to_code = None

    # size
    s1 = None
    s2 = None

    # result object
    result = None
    
    if len(sys.argv) == 2 :
        path_to_code = sys.argv[1]
    elif len(sys.argv) == 4 :
        path_to_code = sys.argv[1]
        s1 = sys.argv[2]
        s2 = sys.argv[3]
    else :
        print("Usage : python windows.py path_to_code [sizex sizey]")


    result = Windows(path_to_code,adaptive_size=True,theme=MONAKAI_THEME).draw()
    result.show()
    #a.save('./out/aa.png')

