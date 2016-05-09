from .bleach import BLEACH
from .dytt import DYTT
from .shield import SHIELD
import argparse

def all():
    parser = argparse.ArgumentParser(description = 'funny_tool: Download movies, tv serials and comics!')
    parser.add_argument('-b', '--bleach', action='store_true', help='Download BLEACH.')
    parser.add_argument('-d', '--dytt', action='store_true', help='Download latest movies from dytt.')
    parser.add_argument('-p', '--page', action='store', type=int, default=1, 
        help='pages to retrieve when downloading movies from dytt, should be used with -d.')
    parser.add_argument('-s', '--shield', action='store_true', help='Download Marvels.Agents.of.S.H.I.E.L.D.')
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

    if given_args.shield:
        s = SHIELD()
        s.get_serials()

    if given_args.bleach == False and given_args.dytt == False and given_args.shield == False:
        parser.print_help()
