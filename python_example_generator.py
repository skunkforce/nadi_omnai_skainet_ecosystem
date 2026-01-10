def nadi_send(format:dict, data, channel: int):
    print(f"[Python] Got from C++: {data}")
    # Respond back
    response = {"ack": True, "received": data.get("id")}
    nadi.callback(response)

def nadi_handle_events():
    r = 1
