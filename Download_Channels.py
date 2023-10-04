from telethon.sync import TelegramClient
import asyncio

async def export_channels(api_id, api_hash, phone, export_file):
    async with TelegramClient('anon', api_id, api_hash) as client:
        # Ensure you're authorised
        await client.start(phone)
        print('Process Started.')

        # Fetch all the channels and groups
        async for dialog in client.iter_dialogs():
            if dialog.is_channel or dialog.is_group:
                with open(export_file, 'a', encoding='utf-8') as f:
                    f.write(f"{dialog.name}\n")


if __name__ == '__main__':
    api_id = input('YOUR_API_ID: ')
    api_hash = input('YOUR_API_HASH: ')
    phone = input('YOUR_PHONE_NUMBER: ')  # Replace with your phone number
    export_file = 'channels.txt'  # Output file

    loop = asyncio.get_event_loop()
    loop.run_until_complete(export_channels(api_id, api_hash, phone, export_file))
    print('Process Complete.')
