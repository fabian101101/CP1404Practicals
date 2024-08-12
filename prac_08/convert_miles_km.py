from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    """ConvertMilesKmApp is a Kivy App for converting miles to kilometres"""
    output_text = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file"""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, text):
        """Convert miles to kilometres and update the label"""
        miles = self.validate_input(text)
        kilometres = miles * MILES_TO_KM
        self.output_text = str(kilometres)

    def handle_increment(self, text, change):
        """Handle up/down button press, increment miles, and update the TextInput"""
        miles = self.validate_input(text) + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_conversion(str(miles))

    def validate_input(self, text):
        """Validate the input; return 0.0 if invalid"""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKmApp().run()
