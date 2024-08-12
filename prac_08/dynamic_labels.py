from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App to create dynamic labels based on a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Define a list of names
        self.names = ["Ada", "Bob", "Sam", "Uche", "Chuks"]

    def build(self):
        """Build the Kivy app from the kv file and dynamically create labels."""
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Dynamically create a label for each name in the list."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
