from telethon.tl.types import InputMessagesFilterPhotos
from telethon import TelegramClient, events
import nest_asyncio
import configparser
import json

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError


config = configparser.ConfigParser()
config.read("config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_token = config['Telegram']['api_token']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']
channel_link = config['Telegram']['channel_link']


nest_asyncio.apply()

import os.path


def get_posts(num_posts=1, download_media=False, only_with_media=True, offset_id=0, posts_list=[]):
    """
    Fetches posts from a Telegram channel and returns a list of post information.

    Args:
        num_posts (int, optional): The number of posts to fetch. Defaults to 1.
        download_media (bool, optional): Whether to download media files (photos) associated with posts. Defaults to False.
        only_with_media (bool, optional): If True, only fetch posts with media content. Defaults to True.
        offset_id (int, optional): The message ID to start fetching posts from. Defaults to 0.
        posts_list (list, optional): List to store the fetched posts. Defaults to an empty list.

    Returns:
        list: A list of dictionaries containing post information. Each dictionary includes:
            - 'upload_date' (str): Upload date of the post.
            - 'text' (str): Text content of the post.
            - 'post_id' (int): ID of the post.
            - 'photos_id_list' (list): List of IDs of photos associated with the post.
            - 'photos_names_list' (list): List of filenames of downloaded photos.
            - 'id_list' (list): List of message IDs in the post.
            - 'edit_date' (str): Edit date of the post.

    Note:
        - This function requires `telethon` library to be installed.
        - The `config.ini` file should be properly configured with API credentials and other settings.
        - When `download_media` is True, media files will be saved in the './media/' directory.
    """

    client = TelegramClient(username, api_id, api_hash)
    posts_list = []

    async def main(num_posts, download_media, offset_id, posts_list):

        if num_posts < 100:
            message_limit = num_posts
        else:
            message_limit = 100

        last_post_date = None
        post = {}

        await client.start()

        try:
            entity = await client.get_entity(channel_link)

            while True:
                messages = await client.get_messages(entity, limit=message_limit, offset_id=offset_id)

                for message in messages:

                    if only_with_media:
                        if not message.media:
                            continue

                    if last_post_date == None:
                        last_post_date = message.date

                    # if delay between uploading messages is more than 10 second i will separate them
                    if (last_post_date - message.date).seconds > 10:
                        post['upload_date'] = last_post_date.strftime(
                            '%Y-%m-%d %H:%M:%S') if last_post_date else None

                        last_post_date = message.date

                        posts_list.append(post)
                        post = {}

                    if len(message.message) > 0:
                        post['text'] = post.get('text', '') + message.message

                        # post_id in messages set will be id of message with text and photo
                        post['post_id'] = message.id

                    if message.media and download_media:

                        photo_id = message.media.photo.id
                        filename = f'image_{photo_id}.jpg'
                        path = f"./media/{filename}"

                        # some of this i should drop, but later
                        post['photos_id_list'] = post.get(
                            'photos_id_list', []) + [photo_id]
                        post['photos_names_list'] = post.get(
                            'photos_names_list', []) + [filename]

                        # if file exist check
                        if not os.path.isfile(path) and download_media:
                            await client.download_media(message, file=path)

                    post['id_list'] = post.get('id_list', []) + [message.id]
                    post['edit_date'] = message.edit_date.strftime(
                        '%Y-%m-%d %H:%M:%S') if message.edit_date else None

                offset_id = messages[len(messages) - 1].id

                if len(posts_list) >= num_posts:
                    break

        except Exception as e:
            print(f"Error: {e}")

        await client.disconnect()

        return posts_list

    if __name__ == "__main__":
        client.loop.run_until_complete(
            main(num_posts, download_media, offset_id, posts_list))

    return posts_list
