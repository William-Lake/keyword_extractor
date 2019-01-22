import PySimpleGUI as psg

class PrimaryUI(psg.Window):

    SUBMIT = 'Submit'

    CLEAR = 'Clear'

    RANKED_PHRASES = 'Ranked Phrases'

    KEYWORD_COUNT = 'Keyword Count'

    def __init__(self):

        super().__init__('Keyword Extractor')

        self.__txt_input_size = (40,10)

        self.__txt_input = psg.Multiline(size=self.__txt_input_size, do_not_clear=True)

        self.__cmb_type = psg.InputCombo(values=(PrimaryUI.RANKED_PHRASES, PrimaryUI.KEYWORD_COUNT))

        self.__btn_submit = psg.Button(button_text=PrimaryUI.SUBMIT)

        self.__btn_clear = psg.Button(button_text=PrimaryUI.CLEAR)

        self.__txt_output= psg.Multiline(size=self.__txt_input_size)

        self.Layout(
            [[self.__txt_input],
            [self.__cmb_type, self.__btn_submit, self.__btn_clear],
            [self.__txt_output]]
        )

    def display_warning_dialog(self,warning_message):

        psg.Popup('Warning',warning_message)

    def set_output_text(self,ouput_text):

        self.__txt_output.Update(ouput_text)

    def clear_input_text(self):

        self.__txt_input.Update('')

