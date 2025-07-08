import json
from selenium.webdriver.chrome.options import Options


class ConfigReader:
    def get_browser_options(self, language='en'):
        options = Options()
        with open('config.json') as f:
            for opt in json.load(f).get('browser', {}).get('options', []):
                options.add_argument(opt)

        options.add_argument(f"--lang={language}")

        return options
