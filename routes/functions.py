import os
from os.path import dirname, abspath, join


def _get_posts():
    parent_dir = dirname(dirname(abspath(__file__)))
    postfiles = os.listdir(join(parent_dir, 'posts'))
    posts = []
    for pf in postfiles:
        posts.append(
            {
                'link': pf[:-3],
                'title': pf[10:-3].replace('-', ' '),
                'date': pf[:10]
            }
        )

    return posts