from vk_api import VkApi
from time import sleep
from random import choice

from modules import config
from modules import util


def main():
    cfg = config.load()

    group_ids = cfg['group_ids']
    messages = cfg['messages']
    delay = cfg['delay']
    access_token = cfg['access_token']

    vk_session = VkApi(token=access_token)
    api = vk_session.get_api()

    row = {}

    if not util.check():
        print('Ошибка: вы не малолетний дебил')
        print('Прочтите README.md (часть "инсталейшн") и выполните пункт 3')
        exit(0)

    for group_id in group_ids:
        if group_id > 0:
            group_id = -group_id

        wall = api.wall.get(owner_id=group_id, filter='all', extended=1, count=1)
        try:
            row.update({group_id: wall['items'][0]['id']})

        except IndexError:
            group = wall['groups'][0]
            print('Группа ' + group['name'] + ' (vk.com/' + group['screen_name'] + ') ' +
                  'будет проигнорирована, т.к у нее нет постов.')

    print('Бот отслеживает новые посты в заданных группах. Ожидайте')

    while True:
        for group_id, latest_post_id in row.items():

            wall = api.wall.get(owner_id=group_id, filter='all', extended=1, count=1)
            post = None
            try:
                post = wall['items'][0]

            except IndexError:
                group = wall['groups'][0]
                print('Группа ' + group['name'] + ' (vk.com/' + group['screen_name'] + ') ' +
                      'будет проигнорирована, т.к у нее больше нет постов.')

            if post:
                if post['id'] > latest_post_id:
                    row.update({group_id: post['id']})
                    message = choice(messages)
                    sleep(1)
                    api.wall.createComment(owner_id=group_id, post_id=post['id'], message=message)
                    print('Бот оставил комментарий с текстом "' + message + '" ' +
                          'под постом https://vk.com/feed?w=wall' + str(group_id) + '_' + str(post['id']))

        sleep(delay)


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        exit(0)
