import openpyxl
from openpyxl import Workbook
from datetime import datetime


def calculate_time_diff(log_entries, keyword1, keyword2):
    """
    Calculates the time difference between records containing the specified keywords.

    :param log_entries: list of tuples (time, message)
    :param keyword1: first keyword
    :param keyword2: second keyword
    :return: list of tuples (time1, time2, difference)
    """
    results = []

    time1 = None
    for time, message in log_entries:
        if keyword1 in message:
            time1 = time
        elif keyword2 in message and time1:
            time2 = time
            time_diff = time2 - time1
            results.append((time1, time2, time_diff))
            time1 = None

    return results


def save_to_excel(data, output_file):
    """
    Saves the results to an XLSX file.

    :param data: list of tuples (time1, time2, difference)
    :param output_file: path to the source file
    """
    wb = Workbook()
    ws = wb.active
    ws.append(["Counter diff time", "SP calls time", "Time difference"])

    for time1, time2, time_diff in data:
        ws.append([time1.strftime('%H:%M:%S.%f')[:-3], time2.strftime('%H:%M:%S.%f')[:-3], str(time_diff)])

    wb.save(output_file)
