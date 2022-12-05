import tree_dir as t
import episodes as e
from pprint import pprint

root = '/home/alan-cugler/Videos/'
mkv_shows = []
exp_shows = []

def show_mapping(root):
    raw = t.get_root_dir(root)
    pprint(raw)
    shows = t.remove_files(raw)
    pprint(shows)
    mkv_shows = t.get_show_with_mkv_children_only(shows)
    pprint(mkv_shows)
    exp_shows = t.get_show_expansions(shows)
    pprint(exp_shows)

def change_mapping(mkv_shows, exp_shows):
    t.make_season_dir(mkv_shows, exp_shows)
    t.move_mkv_into_subdir(mkv_shows, exp_shows)
    e.ep_rename(mkv_shows)
    t.move_mkv_into_subdir(mkv_shows, exp_shows)

if __name__ == '__main__':
    show_mapping(root)
    change_mapping(mkv_shows, exp_shows)
