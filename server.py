import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5555")


def format_string(song):
    output = ''
    output += '\n'
    output += 'ID: ' + song[0] + '\n'
    output += 'Title: ' + song[1] + '\n'
    output += 'Artist: ' + song[2] + '\n'
    output += 'Album: ' + song[3] + '\n'
    output += 'Genre: ' + song[4] + '\n'
    return output

while True:
    message = socket.recv_string()
    time.sleep(1)

    if message:
        if message.lower() == 'q':
            context.destroy()
            break
        else:
            data_rows = message.split('\n')
            keyword = data_rows[0]
            data_type = data_rows[1]
            song_data = data_rows[2:]

            song_data = [song.split('*') for song in song_data]

            result = ''
            if data_type == 'song':
                for song in song_data:
                    if song[1] == keyword:
                        output = format_string(song)
                        result += output

            if not result:
                result += "No songs found"

            socket.send_string(result)





