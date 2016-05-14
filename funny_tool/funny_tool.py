from .bleach import BLEACH
from .dytt import DYTT
from .tvserials import TVSerials
import os, argparse

def all():
    parser = argparse.ArgumentParser(description = 'funny_tool: Download movies, tv serials and comics!')
    parser.add_argument('-b', '--bleach', action='store_true', help='Download BLEACH.')
    parser.add_argument('-d', '--dytt', action='store_true', help='Download latest movies from dytt.')
    parser.add_argument('-p', '--page', action='store', type=int, default=1, 
        help='pages to retrieve when downloading movies from dytt, should be used with -d.')
    parser.add_argument('-t', '--tv', action='store', type=str, help='Download TV serials by giving ID, use flag -l to check IDs.')
    parser.add_argument('-l', '--list', action='store_true', help='TV serials list.')
    given_args = parser.parse_args()


    print('''
                                                                        ,----,                            
                                                                      ,/   .`|                            
    ,---,.                                                          ,`   .'  :                    ,--,    
  ,'  .' |                                                        ;    ;     /                  ,--.'|    
,---.'   |         ,--,      ,---,      ,---,                   .'___,/    ,'  ,---.     ,---.  |  | :    
|   |   .'       ,'_ /|  ,-+-. /  | ,-+-. /  |                  |    :     |  '   ,'\   '   ,'\ :  : '    
:   :  :    .--. |  | : ,--.'|'   |,--.'|'   |     .--,         ;    |.';  ; /   /   | /   /   ||  ' |    
:   |  |-,,'_ /| :  . ||   |  ,"' |   |  ,"' |   /_ ./|         `----'  |  |.   ; ,. :.   ; ,. :'  | |    
|   :  ;/||  ' | |  . .|   | /  | |   | /  | |, ' , ' :             '   :  ;'   | |: :'   | |: :|  | :    
|   |   .'|  | ' |  | ||   | |  | |   | |  | /___/ \: |             |   |  ''   | .; :'   | .; :'  : |__  
'   :  '  :  | : ;  ; ||   | |  |/|   | |  |/ .  \  ' |             '   :  ||   :    ||   :    ||  | '.'| 
|   |  |  '  :  `--'   \   | |--' |   | |--'   \  ;   :             ;   |.'  \   \  /  \   \  / ;  :    ; 
|   :  \  :  ,      .-./   |/     |   |/        \  \  ;             '---'     `----'    `----'  |  ,   /  
|   | ,'   `--`----'   '---'      '---'          :  \  \                                         ---`-'   
`----'                                            \  ' ;                                                  
                                                   `--`                                                                                 
    ''')

    if given_args.bleach:
        b = BLEACH()
        b.get_Latest_URLs()
    
    if given_args.dytt:
        t = DYTT()
        t.get_Latest_URLs(given_args.page)
    
    if given_args.tv:
        s = TVSerials()
        s.get_serials(given_args.tv)
    
    if given_args.list:
        from .utils.TVList import get_list
        tvlist = get_list()
        for key in tvlist.keys(): print(key + ' ' + tvlist[key])
    
    if not given_args.bleach and not given_args.dytt and not given_args.tv and not given_args.list:
        parser.print_help()
