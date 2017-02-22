import os
from os.path import join, dirname, abspath


def _get_posts():

    postfiles = join(abspath(join(dirname(abspath(__file__)), os.pardir)), 'posts')
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