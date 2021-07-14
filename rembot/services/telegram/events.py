from collections import namedtuple

MessageReceived = namedtuple('MessageReceived', 'chat_id, message_id, text, replies')