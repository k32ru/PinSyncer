import logging
import time

from telethon import TelegramClient, events

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
import config as config

if __name__ == '__main__':

    client = TelegramClient('APPIN', config.api_id, config.api_hash)


    @client.on(events.NewMessage)
    async def my_event_handler(event):
        if config.sync_start_message in event.raw_text:
            print(event.raw_text)
            chat = await event.get_chat()
            sender = await event.get_sender()
            chat_id = event.chat_id
            sender_id = event.sender_id
            # print('sender_id', sender_id)
            # print('sender', sender)
            # print('chat', chat)
            # print('chat_id', chat_id)

            # 特定のチャンネルで特定の人が発言した場合にのみout_chat_idで発言をする
            if chat_id == config.in_chat_id and sender_id == config.sync_bot_id:
                time.sleep(60)
                await client.send_message(config.out_chat_id, '/pin update')
                await client.send_message(config.in_chat_id, 'このチャンネルでのピン留めの更新を検知したので、集積所にも更新をしました。(実験的)')


    client.start()
    client.run_until_disconnected()
