import re
from datetime import datetime


def parse_log(file_path):
	"""
	Parses the log file and returns a list of records with timestamps and messages.

	:param file_path: path to the log file
	:return: list of tuples (time, message)
	"""
	log_entries = []
	time_pattern = re.compile(r'(\d{2}:\d{2}:\d{2}\.\d{3})')

	with open(file_path, 'r') as file:
		for line in file:
			match = time_pattern.match(line)
			if match:
				time_str = match.group(1)
				time_obj = datetime.strptime(time_str, '%H:%M:%S.%f')
				message = line[len(time_str):].strip()
				log_entries.append((time_obj, message))

	return log_entries
