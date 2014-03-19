def _capture_exceptions_main():
	import _outputcapture
	import sys
	import traceback
	from functools import partial
	
	def exception_handler(script_path, type, value, tb):
		try:
			if tb is not None:
				tracebacks = traceback.extract_tb(tb)
				for trace in reversed(tracebacks):
					path = trace[0]
					if path == script_path or (path == '<string>' and script_path != 'prompt'):
						line = trace[1]
						_outputcapture.HandleException(line, type.__name__, str(value))
						break
				else:
					sys.__excepthook__(type, value, tb)
			elif type == SyntaxError or type == IndentationError:
				if value.filename == script_path:
					_outputcapture.HandleException(value.lineno, type.__name__, value.msg)
				else:
					sys.__excepthook__(type, value, tb)
		except:
			pass

	sys.excepthook = partial(exception_handler, '{{PYTHONISTA_SCRIPT_PATH}}')

_capture_exceptions_main()
del _capture_exceptions_main
