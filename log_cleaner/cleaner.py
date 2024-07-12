def clean_logs(input_file, cleaned_file, keywords):
    """
    Clears the log file of strings that do not contain the specified keywords.

    :param input_file: path to the input log file
    :param cleaned_file: path to the cleaned file with cleared logs
    :param keywords: list of keywords
    """
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(cleaned_file, 'w') as file:
        for line in lines:
            if any(keyword in line for keyword in keywords):
                file.write(line)
