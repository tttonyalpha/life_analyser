import re


def parse_text(dct):
    '''
    Parses a dictionary containing text and extracts relevant information.

    This function takes a dictionary `dct` as input, where the key 'text' holds a string containing various information,
    including dates, days, and scores. It extracts and processes this information, updating the dictionary with
    additional parsed values.

    Args:
        dct (dict): A dictionary containing text information.

    Returns:
        dict: An updated dictionary with parsed values, including 'parsed_date', 'productivity_score',
        'interest_score', 'stress_score', and 'parsed_text'.'''

    input_string = dct.get('text', None)

    if input_string is None:
        return dct

    date_pattern = r'\d{2}\.\d{2}\.\d{2}'
    day_pattern = r'\b(?:MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY|SUNDAY)\b'

    date_match = re.search(date_pattern, input_string)
    day_match = re.search(day_pattern, input_string)

    date = date_match.group() if date_match else None
    day = day_match.group() if day_match else None

    parsed_date = date.split('.')[-1] + '-' + date.split('.')[1] + \
        '-' + date.split('.')[0] if date or day else None

    dct['parsed_date'] = parsed_date

    if date_match:
        input_string = input_string.replace(
            date_match.group(), "") if parsed_date is not None else input_string
    if day_match:
        input_string = input_string.replace(
            day_match.group(), "") if parsed_date is not None else input_string

    regex_list = [r'How productive have you been\?:\s*(\S|\s+|\d+\.?\d*)/10',
                  r'How interesting was the day\?:\s*(\S|\s+|\d+\.?\d*)/10', r'How stressful was the day\?:\s*(\S|\s+|\d+\.?\d*)/10']
    names_list = ['productivity_score', 'interest_score', 'stress_score']

    for regex, name in zip(regex_list, names_list):
        match = re.search(regex, input_string)

        if match:
            try:
                parsed_score = float(match.group(1))
            except:
                parsed_score = None
        else:
            parsed_score = None

        # parsed_score = match.group(1) if match and match.group(1).isdigit() else None

        dct[name] = parsed_score

        input_string = input_string.replace(
            match.group(), "") if match else input_string

    dct['parsed_text'] = input_string.split('\n')
    return dct


def parse_activities(dct):
     """
    Parses a dictionary containing parsed text and extracts structured activity information.

    This function takes a dictionary `dct` as input, where the key 'parsed_text' holds a list of strings,
    each representing an activity. It processes the activity information, extracting emojis and text descriptions,
    and updates the dictionary with the parsed activity details.

    Args:
        dct (dict): A dictionary containing parsed text information.

    Returns:
        dict: An updated dictionary with parsed activities, stored under the 'parsed_activities' key.

    Example:
        input_data = {
            'parsed_text': ["🏃 Exercise", "* Worked on project", "🛒 Grocery shopping"]
        }
        parsed_activities_data = parse_activities(input_data)
        print(parsed_activities_data)
        # Output: {'parsed_text': ..., 'parsed_activities': [('🏃', 'Exercise'), ('*', 'Worked on project'),
        # ('🛒', 'Grocery shopping')]}

    Note:
        Emoji ranges \U0001F000-\U0001F9FF and \U0001FA00-\U0001FA6F include various emojis.
    """

    input_list = dct.get('parsed_text', None)

    if input_list is None:
        return dct

    result = []
    for item in input_list:
        match = re.match(
            r'^([\U0001F000-\U0001F9FF]+|[\U0001FA00-\U0001FA6F]+|\*)?\s*(.*)$', item)
        if match:
            emoji = match.group(1)
            text = match.group(2).strip()
            if emoji or text:
                result.append((emoji, text))

    dct['parsed_activities'] = result
    return dct
