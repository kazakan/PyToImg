from writer import *
from theme import DT1_THEME, DT2_THEME, JUSTTEXT_THEME, MATRIX_THEME, MONAKAI_THEME
from windows import *

import argparse

if __name__ == "__main__":
    import sys, theme

    theme = {
        'matrix':MATRIX_THEME,
        'text':DT1_THEME,
        'monakai':DT2_THEME,
        'dt1':JUSTTEXT_THEME,
        'dt2':MONAKAI_THEME
    }

    argparser = argparse.ArgumentParser(description='PyCode 2 Image')
    argparser.add_argument('path')
    argparser.add_argument('--theme','-t',choices=['matrix','text','monakai','dt1','dt2','all'],default='text')
    argparser.add_argument('--nametype','-n',choices=[0,1,2],default=0,type=int)

    args = argparser.parse_args()

    name = args.path.split('/')[-1].split('.')[0]

    img = None
    if(args.theme == 'all'):
        for t in theme.values():
            img = Windows(
                args.path,
                theme=t,
                adaptive_size=True,
                title_type=args.nametype
            ).draw()
            img.save('./out/'+name+'_'+t.name+'.png',format='png')
    else:
        img = Windows(
            args.path,
            theme=theme[args.theme],
            adaptive_size=True,
            title_type=args.nametype
        ).draw()
        img.save('./out/'+name+'_'+theme[args.theme].name+'.png',format='png')
    #a.save('./out/aa.png')


