import re
from datetime import datetime

def parse_chat(file_path):
    chat = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        match = re.match(r"^(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2} [ap]m) - (.*?): (.*)", line)
        if match:
            date_str, time_str, sender, message = match.groups()
            timestamp = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %I:%M %p")
            chat.append({
                "timestamp": timestamp,
                "sender": sender,
                "message": message.strip()
            })
    return chat
