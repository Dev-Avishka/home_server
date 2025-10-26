from db import send_first_15_objects


def home():
    json_data = send_first_15_objects()
    return {"memes": json_data}