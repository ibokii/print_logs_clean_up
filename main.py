import json
from log_cleaner.cleaner import clean_logs
from log_cleaner.parser import parse_log
from log_cleaner.time_diff import calculate_time_diff, save_to_excel


def load_config(config_file):
	with open(config_file, 'r') as file:
		config = json.load(file)
	return config


if __name__ == "__main__":
	config = load_config('config/config_imm_s_1300_1.json')

	input_file = config['input_file']
	cleaned_file = config['cleaned_file']
	output_file = config['output_file']
	keywords = config['keywords']
	keyword1 = config['keyword1']
	keyword2 = config['keyword2']

	clean_logs(input_file, cleaned_file, keywords)

	log_entries = parse_log(cleaned_file)

	time_diffs = calculate_time_diff(log_entries, keyword1, keyword2)

	save_to_excel(time_diffs, output_file)

	print(f'Logs cleaned. Output saved to {cleaned_file}')
	print(f'Time differences calculated. Results saved to {output_file}')