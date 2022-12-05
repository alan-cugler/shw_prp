import re
import os

root = '/home/alan-cugler/Videos/'

def get_root_dir(root):
    """
    Returns a list of the provided directory.
    """
    raw = os.listdir(root)
    return raw

def remove_files(raw):
    """
    Returns a list of files/directories that are not hidden
    with the preceding '.' naming convention.
    """
    edited = []
    for el in raw:
        if not '.' in el:
            edited.append(el)
    return edited

def get_mkv_in_root(raw):
    """
    Returns a list of '.mkv' files in the provided file/directory
    name list.
    """
    edited = []
    for el in raw:
        if '.mkv' in el:
            edited.append(el)
    return edited

def get_shows_with_mkv_children(shows):
    """
    Returns a list of directories with children '.mkv' files present.
    """
    edited = []
    for show in shows:
        ep_lst = os.listdir(show)
        for ep in ep_lst:
            if '.mkv' in ep:
                print(show+': '+ep)
                edited.append(show)
    return edited

def get_show_with_mkv_children_only(shows):
    """
    Returns a list of directories with only children '.mkv' files present.
    """
    edited = []
    for show in shows:
        only_mkv = True
        epl = os.listdir(root+show)
        for ep in epl:
            if not '.mkv' in ep:
                only_mkv = False
        if only_mkv:
            edited.append(show)
    return edited

def get_show_with_subdir_only(shows):
    """
    Returns a list of directories with only sub directories present.
    """
    edited = []
    for show in shows:
        only_mkv = True
        epl = os.listdir(root+show)
        for ep in epl:
            if not '.mkv' in ep:
                only_mkv = False
        if not only_mkv:
            edited.append(show)
    return edited

def get_show_expansions(shows):
    """
    Returns a list of directories with names indicating 2nd+
    seasons or special episodes.
    """
    edited = []
    re_lst = ['[sS]eason', '[sS][0-9][2-9]', 'OVA']
    for show in shows:
        for check in re_lst:
            exp = ''
            exp = re.search(check, show)
            if exp:
                edited.append(show)
                break
    return edited

def make_exp_season_dir(show):
    """
    Creates 2nd+ or special 'Season ##' sub directories
    return list.
    """
    num_list = ['02', '03', '04', '05', '06', '07', '08',
                '09', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22',
                '23', '24', '25', '26', '27', '28', '29',
                '30', '31', '32', '33', '34', '35', '36',
                '37', '38', '39', '40', '41', '42', '43',
                '44', '45', '46', '47', '48', '49', '50',
                '01']
    if 'OVA' in show:
        print('created: '+show+'/Season 00')
        #os.makedirs(root+show+'/Season 00', exist_ok=True)
    for num in num_list:
        if 'S'+ str(num) in show:
            print('created: '+show+'/Season '+ str(num))
            #os.makedirs(root+show+'/Season '+ str(num), exist_ok=True)

def make_season_dir(mkv_shows, exp_shows):
    """
    Creates assumed 'Season 01' sub directory for all shows
    with only '.mkv' children in its directory.
    """
    for show in mkv_shows:
        exp_owned = False
        for exp in exp_shows:
            if exp == show:
                exp_owned = True
                make_exp_season_dir(show)
        if not exp_owned:
            print('created: ' + show + '/Season 01')
            #os.makedirs(root+show + '/Season 01', exist_ok=True)

def move_mkv_into_subdir(mkv_shows, exp_shows):
    """
    Moves '.mkv' files in shows directory to the season sub
    directory.
    """
    for show in mkv_shows:
        exp_owned = False
        for exp in exp_shows:
            if exp == show:
                exp_owned = True
                move_exp_season_dir(show)
                break
        if not exp_owned:
            for ep in os.listdir(root+show):
                if '.mkv' in ep:
                    print(show+'/Season 01/'+ep)
                #os.rename(root+show+'/'+ep, root+show+'/Season 01/'+ep)

def move_exp_season_dir(show):
    """

    """
    num_list = ['02', '03', '04', '05', '06', '07', '08',
                '09', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22',
                '23', '24', '25', '26', '27', '28', '29',
                '30', '31', '32', '33', '34', '35', '36',
                '37', '38', '39', '40', '41', '42', '43',
                '44', '45', '46', '47', '48', '49', '50',
                '01']
    if 'OVA' in show:
        for ep in os.listdir(root + show):
            if '.mkv' in ep:
                print('created: '+show+'/Season 00/'+ep)
        # os.rename(root+show+'/'+ep, root+show+'/Season 00/'+ep)

    for num in num_list:
        if 'S' + str(num) in show:
            for ep in os.listdir(root + show):
                if '.mkv' in ep:
                    print('moved: '+show+'/Season '+str(num)+'/'+ep)
            # os.rename(root+show+'/'+ep, root+show+'/Season '+str(num)+'/'+ep)


