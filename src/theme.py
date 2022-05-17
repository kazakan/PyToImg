import token
import tokenize
from PIL import ImageFont

import pytoken

s1 = (2048,2048)

s2= (2048,1024)

s3= (1024,512)

s = s3

class Theme:

    def __init__(self,name="",**kwargs):
        self.name = name

        self.color_default = kwargs['color_default']
        self.color_code_bg = kwargs['color_code_bg']
        self.color_title_bg = kwargs['color_title_bg']
        self.color_title_text = kwargs['color_title_text']
        self.color_linenum_bg = kwargs['color_linenum_bg']
        self.color_linenum_text = kwargs['color_linenum_text']

        self.color_code_num  = kwargs['color_code_num']
        self.color_code_op = kwargs['color_code_op']
        self.color_code_string = kwargs['color_code_string']
        self.color_code_comment = kwargs['color_code_comment']
        self.color_code_name = kwargs['color_code_name']
        self.color_code_errortoken = kwargs['color_code_errortoken']
        self.color_code_keyword = kwargs['color_code_keyword']
        self.color_code_text = kwargs['color_code_text']
        self.color_code_builtinfn = kwargs['color_code_builtinfn']
        self.color_code_builtinconst = kwargs['color_code_builtinconst']

        self.fontname_code = kwargs['fontname_code']
        self.fontname_title  = kwargs['fontname_title']
        self.fontname_linenum = kwargs['fontname_linenum']

        self.fontsize_code = kwargs['fontsize_code']
        self.fontsize_title  = kwargs['fontsize_title']
        self.fontsize_linenum = kwargs['fontsize_linenum']

        self.window_title_height = kwargs['window_title_height']
        self.window_linenum_width =kwargs['window_linenum_width']
        self.window_code_lpad = kwargs['window_code_lpad']
        self.window_size = kwargs['window_size']

        self.code_spacing = kwargs['code_spacing']

        if self.fontname_code and self.fontsize_code:
            self.font_code = ImageFont.truetype(self.fontname_code,self.fontsize_code)

        if self.fontname_title and self.fontsize_title:
            self.font_title = ImageFont.truetype(self.fontname_title,self.fontsize_title)

        if self.fontname_linenum and self.fontsize_linenum:
            self.font_linenum = ImageFont.truetype(self.fontname_linenum,self.fontsize_linenum)

    @property
    def code_color(self):
        return {
            token.NUMBER:       self.color_code_num,
            token.OP:           self.color_code_op,
            token.STRING:       self.color_code_string,
            tokenize.COMMENT:   self.color_code_comment,
            token.NAME:         self.color_code_name,
            token.ERRORTOKEN:   self.color_code_errortoken,
            pytoken.KEYWORD:           self.color_code_keyword,
            pytoken.TEXT:              self.color_code_text,
            pytoken.BUILTIN_FN:        self.color_code_builtinfn,
            pytoken.BUILTIN_CONST:     self.color_code_builtinconst
        }

MONAKAI_THEME = Theme(
    name='monakai',

    color_default='#000000',
    color_code_bg='#282c34',
    color_title_bg='#9da5b4',
    color_title_text='#000000',
    color_linenum_bg= '#495162',
    color_linenum_text='#000000',

    color_code_num ='#0080C0',
    color_code_op ='#e06c75',
    color_code_string='#ff28cb',
    color_code_comment='#676f7d',
    color_code_name='#abb2bf',
    color_code_errortoken='#FF8080',
    color_code_keyword='#e06c75',
    color_code_text='#000000',
    color_code_builtinfn='#98c379',
    color_code_builtinconst='#56b6c2',

    fontname_code ='consola.ttf',
    fontsize_code= 40,
    fontname_title='consola.ttf',
    fontsize_title= 40,
    fontname_linenum= 'cour.ttf',
    fontsize_linenum= 40,

    window_size=s,
    window_title_height=40,
    window_linenum_width=80,
    window_code_lpad=10,

    code_spacing = 20
)

DT1_THEME = Theme(
    name='dt1',

    color_default='#000000',
    color_code_bg='#000000',
    color_title_bg='#0d0d0d',
    color_title_text='#cc9500',
    color_linenum_bg= '#000000',
    color_linenum_text='#494949',

    color_code_num ='#ff64ff',
    color_code_op ='#c1c1c1',
    color_code_string='#ffff3c',
    color_code_comment='#3ce9ff',
    color_code_name='#ffffff',
    color_code_errortoken='#FF8080',
    color_code_keyword='#f41414',
    color_code_text='#ffffff',
    color_code_builtinfn='#285dff',
    color_code_builtinconst='#285dff',

    fontname_code ='consola.ttf',
    fontsize_code= 40,
    fontname_title='consola.ttf',
    fontsize_title= 40,
    fontname_linenum= 'consola.ttf',
    fontsize_linenum= 40,

    window_size=s,
    window_title_height=40,
    window_linenum_width=80,
    window_code_lpad=10,

    code_spacing = 20
)

MATRIX_THEME = Theme(
    name='matrix',

    color_default='#0d0208',
    color_code_bg='#0d0208',
    color_title_bg='#0d0208',
    color_title_text='#008f11',
    color_linenum_bg= '#0d0208',
    color_linenum_text='#005400',

    color_code_num ='#88ff88',
    color_code_op ='#008f11',
    color_code_string='#009000',
    color_code_comment='#006816',
    color_code_name='#1ae000',
    color_code_errortoken='#008f11',
    color_code_keyword='#88ff88',
    color_code_text='#008f11',
    color_code_builtinfn='#00ff41',
    color_code_builtinconst='#00ff41',

    fontname_code ='consola.ttf',
    fontsize_code= 40,
    fontname_title='consola.ttf',
    fontsize_title= 40,
    fontname_linenum= 'consola.ttf',
    fontsize_linenum= 40,

    window_size=s,
    window_title_height=40,
    window_linenum_width=80,
    window_code_lpad=10,

    code_spacing = 20
)

DT2_THEME = Theme(
    name='dt2',

    color_default='#212121',
    color_code_bg='#212121',
    color_title_bg='#353535',
    color_title_text='#adadad',
    color_linenum_bg= '#212121',
    color_linenum_text='#494949',

    color_code_num ='#ff6950',
    color_code_op ='#ffa450',
    color_code_string='#ff8c8b',
    color_code_comment='#676f7d',
    color_code_name='#abb2bf',
    color_code_errortoken='#FF8080',
    color_code_keyword='#f41463',
    color_code_text='#c1c1c1',
    color_code_builtinfn='#00cc7a',
    color_code_builtinconst='#28d5ff',

    fontname_code ='consola.ttf',
    fontsize_code= 40,
    fontname_title='consola.ttf',
    fontsize_title= 40,
    fontname_linenum= 'cour.ttf',
    fontsize_linenum= 40,

    window_size=s,
    window_title_height=40,
    window_linenum_width=80,
    window_code_lpad=10,

    code_spacing = 20
)

JUSTTEXT_THEME = Theme(
    name='justtext',

    color_default='#ffffff',
    color_code_bg='#ffffff',
    color_title_bg='#ffffff',
    color_title_text='#000000',
    color_linenum_bg= '#ffffff',
    color_linenum_text='#000000',

    color_code_num ='#000000',
    color_code_op ='#000000',
    color_code_string='#000000',
    color_code_comment='#000000',
    color_code_name='#000000',
    color_code_errortoken='#000000',
    color_code_keyword='#000000',
    color_code_text='#000000',
    color_code_builtinfn='#000000',
    color_code_builtinconst='#000000',

    fontname_code ='consola.ttf',
    fontsize_code= 40,
    fontname_title='consola.ttf',
    fontsize_title= 40,
    fontname_linenum= 'consola.ttf',
    fontsize_linenum= 40,

    window_size=s,
    window_title_height=40,
    window_linenum_width=80,
    window_code_lpad=10,

    code_spacing = 20
)
