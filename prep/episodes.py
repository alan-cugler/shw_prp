import os
import re

root = '/home/alan-cugler/Videos/'

def extension_discovery(raw):
    file_type = ''
    extension = ['.mkv', '.mp4']

    for ext in extension:
        for ep in raw:
            if ext in ep:
                file_type = ext
                break
    return file_type

def extension_removal(raw, file_type):
    edited = []

    for ep in raw:
        edited.append(ep.split(file_type)[0])
    return edited

def square_bracket_splicing(ep_list):
    """
    incomplete
    """
    edited = []
    brckt_cnt = 0

    for ep in ep_list:
        if ep.count('[') > brckt_cnt:
            brckt_cnt = ep.count('[')
            break

    for ep in ep_list:
        for brckt in range(brckt_cnt):
            frst_chnk = ep.split('[', 1)[0]
            scnd_chnk = ep.split(']', 1)[1]



def torrent_signature_removal(raw, ep_list):
    """
    deprecated
    """
    edited = []
    brand_found = ''
    torrenters = ['[Judas]', '[EMBER]', '[Erai-raws]', '[Anime Time]', '[HR]', '[DB]', '[Cleo]', '[Nep_Blanc]']

    for brand in torrenters:
        for ep in raw:
            if brand in ep:
                brand_found = brand
                break

    if brand_found:
      for ep in ep_list:
          edited.append(ep.replace(brand_found, '').strip())
      return edited
    else:
      return ep_list


def title_metadata_removal(ep_list):
    edited = []
    tag_found = ''
    metadata = ['(Dual Audio_10bit_BD1080p_x265)', '(Dual Audio_10bit_1080p_x265)', ' [1080p][Multiple Subtitle]', ' [1080p][HEVC 10bit x265][AAC][Multi Sub]', '[BD-1080P] [10Bit] [X265] [SUBBED] [AAC] ']

    for tag in metadata:
        for ep in ep_list:
            if tag in ep:
                tag_found = tag
                break

    if tag_found:
        for ep in ep_list:
            edited.append(ep.replace(tag_found, '').strip())
        return edited
    else:
        return ep_list


def spacer_chracter_removal(ep_list):
    """
    deprecated
    """
    edited = []
    spacer_found = ''
    spacers = [' - ', '_-_']

    for waste in spacers:
        for ep in ep_list:
            if waste in ep:
                spacer_found = waste
                break

    if spacer_found:
        for ep in ep_list:
            edited.append(ep.replace(spacer_found, ' ').strip())
        return edited
    else:
        return ep_list


def extension_addition(ep_list, file_type):
    edited = []
    for ep in ep_list:
        edited.append(ep + file_type)
    return edited

def correlate_versions(raw, ep_list):
    show_dict = {}

    for el in range(len(raw)):
        show_dict[raw[el]] = ep_list[el]
    return show_dict

def write_file_name_changes(show_dict):
    for k, v in show_dict.items():
        os.rename(k, v)

def add_episode_monicure(ep_list):
    edited = []
    re_lst = ['\s[0-9][0-9]\s','\s[0-9][0-9].','-[0-9][0-9]\s',
              '[0-9][0-9]-', '[0-9][0-9]_' ]

    ep = x.search('')

#    for ep in ep_list:

#def grab_series_name():
#    for path, subdirs, files



def corporate():
    raw = os.listdir(path="./Black Summoner")

    file_type = ''
    ep_list = []
    ep_dict = {}

    file_type = extension_discovery(raw)
    ep_list = extension_removal(raw, file_type)
    ep_list = torrent_signature_removal(raw, ep_list)
    ep_list = title_metadata_removal(ep_list)
    ep_list = spacer_chracter_removal(ep_list)
    ep_list = extension_addition(ep_list, file_type)
    ep_dict = correlate_versions(raw, ep_list)

    for k, v, in ep_dict.items():
        print('original title: '+ k)
        print('refactor title: '+ v)
        print('--------------------------------')


#def dir_crawling():
#    for path, subdirs, files in os.walk('.'):
#        for show in subdirs:
#            if 

#import os
#import shutil
#from pathlib import Path

#here = Path(os.path.dirname(os.path.realpath(__file__)))
#target_path = Path("/home/alan-cugler/Games/starsector/starsector/mods")


#for mod_husk in here.iterdir():
#    if mod_husk.is_dir():
#        for mod in mod_husk.iterdir():
#            print(mod)
#            shutil.copytree(mod, target_path, copy_function=os.link)

#corporate()
    #write_file_name_changes(ep_dict)


#for path, subdirs, files in os.walk('.'):
#    print(path)
#    print(subdirs)
#    print(files)
#    for name in subdirs:
#        print(os.path.join(path, name))

#cont_lst = []
#for el in edited:
#    x = ''
#    x = re.search('[sS]eason', el)
#    x = re.search('[sS][0-9][2-9]', el)
#    if x:
#        cont_lst.append(el)

#for el in edited:
#    lst = os.listdir(el)
#    for le in lst:
#        if '.mkv' in le:
#            print(el+': '+le)
#        if not '.mkv' in le:
#            print(el+': '+le)

#for el in cont_lst:
#    for nm in num_lst:
#        if 'S'+nm in el:
#            print(el+': Season '+nm)
#    if "OVA" in el:
#        print(el+': Season 00')

# Captures all the strings with '[]'
#re.findall('\[[a-zA-Z0-9\ \_\-]*\]', VARIABLE )

# Captures all the strings with '()'
#re.findall('\([a-zA-Z0-9\ \_\-]*\)', VARIABLE )

# capture all dual numbers with separation characters
#re.findall('[_| |-|[eE][0-9][0-9][_| |-|\.]',VARIABLE)

# captures variations of s##e##
#re.findall('[sS][0-9][0-9][eE][0-9][0-9]',ep)


def ep_rename(mkv_shows):
    for show in mkv_shows:
        name = show
        exp = ''
        exp = re.findall(' [sS][0-9][2-9]', show)
        if exp:
            name = show.split(exp[0])[0]

        for ep in os.listdir(root + show):
            x = ''
            y = ''
            x = re.findall('[_| |-][0-9][0-9][_| |-|\.]', ep)
            if x:
                y = re.findall('[0-9][0-9]', x[0])
                print(root+show+'/'+name+' - s01e'+y[0]+'.mkv')
                # os.rename(root+show+'/'+ep, root+show+'/'+name+' - s01e'+y[0]+'.mkv')
            else:
                x = re.findall('[sS][0-9][0-9][eE][0-9][0-9]', ep)
                if x:
                    print(root+show+'/'+name+' - '+x[0].lower()+'.mkv')
                    # os.rename(root+show+'/'+ep, root+show+'/'+name+' - '+x[0].lower()+'.mkv')

