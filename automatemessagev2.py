import os
#import config

def get_lyrics(file_path):
	with open(file_path, 'r') as read_file:
		text = read_file.readlines()[0]
		lyrics = text.split()
	return lyrics

def send_message(phone_number, message):
	os.system('osascript sentMessage.scpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
	lyrics = get_lyrics('chickfilye.txt')
	for each_lyric in lyrics:
		send_message(2403089035, each_lyric)
			