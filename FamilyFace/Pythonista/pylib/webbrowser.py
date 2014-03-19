import _webbrowser

def open(url, modal=False, stop_when_done=False):
	return _webbrowser.open(url, modal, stop_when_done)

def can_open(url):
	return _webbrowser.can_open(url)

add_to_reading_list = _webbrowser.add_to_reading_list
