import _photos

def pick_image(show_albums=False):
	image_info = _photos.pick_image(show_albums)
	if image_info is None:
		return None
	else:
		image_data, w, h = image_info
		import Image
		img = Image.fromstring('RGBA', (w, h), image_data)
		return img

def capture_image():
	image_info = _photos.capture_image()
	if image_info is None:
		return None
	else:
		image_data, w, h = image_info
		import Image
		img = Image.fromstring('RGBA', (w, h), image_data)
		return img

def get_count():
	return _photos.get_image_count()

def get_thumbnail(image_index=-1):
	image_info = _photos.get_thumbnail_image(image_index)
	if image_info is None:
		return None
	else:
		image_data, w, h = image_info
		import Image
		img = Image.fromstring('RGBA', (w, h), image_data)
		return img

def get_image(image_index=-1):
	image_info = _photos.get_image(image_index)
	if image_info is None:
		return None
	else:
		image_data, w, h = image_info
		import Image
		img = Image.fromstring('RGBA', (w, h), image_data)
		return img

def get_fullscreen_image(image_index=-1):
	image_info = _photos.get_image(image_index, True)
	if image_info is None:
		return None
	else:
		image_data, w, h = image_info
		import Image
		img = Image.fromstring('RGBA', (w, h), image_data)
		return img

def get_metadata(image_index=-1):
	metadata_json = _photos.get_metadata(image_index)
	if metadata_json is None:
		return None
	else:
		import json
		return json.loads(metadata_json)

def save_image(image):
	rgba_image = image
	if image.mode != 'RGBA':
		rgba_image = image.convert('RGBA')
	image_data = rgba_image.tostring()
	return _photos.save_image(image_data, image.size[0], image.size[1])
	
