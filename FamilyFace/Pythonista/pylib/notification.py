import _notification

cancel_all = _notification.cancel_all

def schedule(message, delay=0, sound_name=None, action_url=None):
	if sound_name is None:
		sound_name = ''
	if action_url is None:
		action_url = ''
	fire_date = _notification.schedule(message, delay, sound_name, action_url)
	return {'message': message, 'fire_date': fire_date, 'sound_name': sound_name if sound_name == '' else sound_name + '.caf', 'action_url': action_url}

def get_scheduled():
	notifications_json = _notification.get_notifications()
	import json
	return json.loads(notifications_json)

def cancel(notification_dict):
	message = notification_dict.get('message', '')
	fire_date = notification_dict.get('fire_date', 0.0)
	sound_name = notification_dict.get('sound_name', '')
	action_url = notification_dict.get('action_url', '')
	_notification.cancel(message, fire_date, sound_name, action_url)
