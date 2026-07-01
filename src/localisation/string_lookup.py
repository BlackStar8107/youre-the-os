import json, os

class StringLookup():

    def __init__(self, lang: str = "en_us") -> None:
        self.lang = lang
        self.long_lang = self.fetch_long_lang(lang)
        self.translation_key = {}
        self.read_localisation_file()

    def get_lang(self) -> str:
        """Returns the short name of the current language."""
        return self.lang
    
    def set_lang(self, lang:str) -> None:
        """Set the language currently being used, this must be the short name."""
        self.lang = lang
        self.long_lang = self.fetch_long_lang(lang)
        self.translation_key = {}
        self.read_localisation_file()

    def get_long_lang(self) -> str:
        """Returns the currently stored Long Name."""
        return self.long_lang

    def fetch_long_lang(self, token: str) -> str:
        """Fetches the Long Name from file, requires a token"""
        try:
            # CWD is src/
            # This weird format is due to the loc files not wanting to be found!
            # ToDo: Review if this is resolved when properly implimented
            class_file_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(class_file_path, "lang_names.json")

            file_data = ""
            with open(file_path) as f:
                file_data = json.load(f)

            if token in file_data:
                self.long_lang = file_data[token]
                return self.long_lang
            else:
                return token
                
        except Exception as E:
            print(f"Error | fetch_long_lang | {E}")
            raise E

    def get_string(self, token: str) -> str|list:
        """Returns the correct localised string or list of strings based on a token; Failing to do so will just result in the token."""
        if len(self.translation_key) < 1:
            self.read_localisation_file()

        if token not in self.translation_key:
            return "@#@ " + token + " @#@"
        else:
            return self.translation_key[token]

    def read_localisation_file(self) -> bool:
        """This attempts to read the current language's localisation file."""
        try:

            # CWD is src/
            # This weird format is due to the loc files not wanting to be found!
            # ToDo: Review if this is resolved when properly implimented
            class_file_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(class_file_path, self.lang+".json")

            with open(file_path, "r") as f:
                self.translation_key = json.load(f)
        
        except Exception as E:
            print(f"Error | read_localisation_file | {E}")
            self.translation_key = {}
            return False

        return True

# ToDo: Remove this temp test!
if __name__ == "__main__":
    print("Main Detected, Beginning Tests")
    string_lookup = StringLookup("en_us")
    print(string_lookup.get_string("you_got_rebooted"))
    print(string_lookup.get_string("how_to_play_0_0"))
    print("")
    print(string_lookup.get_lang())
    print(string_lookup.get_long_lang())

    print("")
    print("Start en_uk Test")
    print("")

    string_lookup.set_lang("en_uk")
    print(string_lookup.get_string("you_got_rebooted"))
    print(string_lookup.get_string("how_to_play_0_0"))
    print("")
    print(string_lookup.get_lang())
    print(string_lookup.get_long_lang())
    print("")