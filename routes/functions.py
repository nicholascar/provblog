import os


def _get_posts():
    postfiles = os.listdir('posts')
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