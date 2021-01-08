import requests


def send(data):
    event_data = {
        'event_type': 'CommentCreated',
        'event_data': data
    }
    requests.post('http://localhost:5000/events/', json=event_data)