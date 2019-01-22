import re
from rake_nltk import Rake
from primary_ui import PrimaryUI
from stop_words import words

INPUT_TEXT = 0

TYPE_SELECTION = 1

def main():

    primary_ui = PrimaryUI()

    rake = Rake()

    while True:

        event, value = primary_ui.Read()

        if event is None: break

        else:

            if event == PrimaryUI.SUBMIT:

                extraction_type = value[TYPE_SELECTION]

                input_text = re.sub(r'[^A-Za-z0-9\.?!"\' ]','',value[INPUT_TEXT].strip())

                if input_text:

                    if extraction_type == PrimaryUI.KEYWORD_COUNT:

                        keyword_count_dict = {}

                        for line in input_text.splitlines():

                            for keyword in line.split(' '):

                                if (
                                    keyword.upper() in words or
                                    not keyword.strip()): continue

                                keyword_count_dict[keyword] = (
                                    keyword_count_dict[keyword] + 1
                                    if keyword in keyword_count_dict.keys()
                                    else
                                    1
                                )

                        output_text = []

                        keyword_count_dict = [(k, keyword_count_dict[k]) for k in sorted(keyword_count_dict, key=keyword_count_dict.get, reverse=True)]

                        for keyword, count in keyword_count_dict: output_text.append(f'{keyword} : {count}')

                        primary_ui.set_output_text('\n'.join(output_text))

                    elif extraction_type == PrimaryUI.RANKED_PHRASES:

                        rake.extract_keywords_from_text(input_text)

                        primary_ui.set_output_text('\n'.join(rake.get_ranked_phrases()))  

                else: primary_ui.display_warning_dialog("No input text was provided. Please provide Input.")

            elif event == PrimaryUI.CLEAR: primary_ui.clear_input_text()
