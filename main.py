from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.properties import ListProperty, StringProperty
from kivy.metrics import dp

import math

# تنظیم اندازه پنجره برای دسکتاپ
if platform != 'android' and platform != 'ios':
    Window.size = (400, 600)

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(5)
    canvas.before:
        Color:
            rgba: app.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
    
    # Header with theme switch button
    BoxLayout:
        size_hint_y: 0.1
        spacing: dp(10)
        
        Label:
            text: "HOSSEIN HAMIDY"
            font_size: "20sp"
            halign: "center"
            valign: "middle"
            color: app.text_color
            bold: True
        
        Button:
            text: "Theme"
            font_size: "16sp"
            size_hint_x: 0.3
            background_color: app.theme_switch_color
            color: app.text_color
            on_release: app.toggle_theme()
    
    # Display
    Label:
        id: display
        text: "0"
        font_size: "48sp"
        size_hint_y: 0.15
        halign: "right"
        valign: "middle"
        color: app.text_color
        text_size: self.width - dp(20), self.height
        padding: dp(20), 0
        canvas.before:
            Color:
                rgba: app.display_bg_color
            Rectangle:
                pos: self.pos
                size: self.size
    
    # Calculator buttons
    GridLayout:
        cols: 4
        rows: 5
        spacing: dp(5)
        padding: dp(5)
        size_hint_y: 0.75
        
        # Row 1
        Button:
            text: "C"
            font_size: "22sp"
            background_color: app.clear_button_color
            color: app.text_color
            on_release: app.clear()
        
        Button:
            text: "R"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.backspace()
        
        Button:
            text: "%"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.percentage()
        
        Button:
            text: "/"
            font_size: "22sp"
            background_color: app.operation_color
            color: app.text_color
            on_release: app.add_operation("/")
        
        # Row 2
        Button:
            text: "7"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.add_number("7")
        
        Button:
            text: "8"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.add_number("8")
        
        Button:
            text: "9"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.add_number("9")
        
        Button:
            text: "*"
            font_size: "22sp"
            background_color: app.operation_color
            color: app.text_color
            on_release: app.add_operation("*")
        
        # Row 3
        Button:
            text: "4"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.add_number("4")
        
        Button:
            text: "5"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.add_number("5")
        
        Button:
            text: "6"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.add_number("6")
        
        Button:
            text: "-"
            font_size: "22sp"
            background_color: app.operation_color
            color: app.text_color
            on_release: app.add_operation("-")
        
        # Row 4
        Button:
            text: "1"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.add_number("1")
        
        Button:
            text: "2"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.add_number("2")
        
        Button:
            text: "3"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.add_number("3")
        
        Button:
            text: "+"
            font_size: "22sp"
            background_color: app.operation_color
            color: app.text_color
            on_release: app.add_operation("+")
        
        # Row 5
        Button:
            text: "0"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.add_number("0")
        
        Button:
            text: "00"
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.add_number("00")
        
        Button:
            text: "."
            font_size: "22sp"
            background_color: app.button_color
            color: app.text_color
            on_release: app.add_decimal()
        
        Button:
            text: "="
            font_size: "22sp"
            background_color: app.equal_color
            color: app.text_color
            on_release: app.calculate()
'''


class CalculatorApp(App):
    # Color properties
    bg_color = ListProperty([0.1, 0.1, 0.1, 1])
    display_bg_color = ListProperty([0.15, 0.15, 0.15, 1])
    button_color = ListProperty([0.2, 0.3, 0.2, 1])
    operation_color = ListProperty([0.15, 0.25, 0.15, 1])
    equal_color = ListProperty([0.25, 0.4, 0.25, 1])
    clear_button_color = ListProperty([0.3, 0.2, 0.2, 1])
    text_color = ListProperty([0.9, 1, 0.9, 1])
    theme_switch_color = ListProperty([0.3, 0.3, 0.3, 1])
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_dark_theme = True
        self.current_input = ""
        self.last_result = None
        
    def build(self):
        return Builder.load_string(KV)
    
    def add_number(self, number):
        """Add number to display"""
        if self.current_input == "0":
            self.current_input = number
        elif self.current_input == "":
            self.current_input = number
        else:
            self.current_input += number
        self.update_display()
    
    def add_decimal(self):
        """Add decimal point"""
        if self.current_input == "":
            self.current_input = "0."
        elif self.current_input[-1] in "+-*/":
            self.current_input += " 0."
        else:
            parts = self.current_input.split()
            if parts and "." not in parts[-1]:
                self.current_input += "."
        self.update_display()
    
    def add_operation(self, operation):
        """Add operator"""
        if self.current_input == "":
            return
        
        if self.current_input[-1] in "+-*/":
            self.current_input = self.current_input[:-1] + operation
        else:
            self.current_input += operation
        
        self.update_display()
    
    def calculate(self):
        """Calculate result"""
        try:
            if not self.current_input:
                return
            
            expression = self.current_input.replace(" ", "")
            expression = expression.replace("÷", "/").replace("×", "*")
            
            result = eval(expression)
            
            if isinstance(result, float):
                if result.is_integer():
                    self.current_input = str(int(result))
                else:
                    self.current_input = f"{result:.10f}".rstrip('0').rstrip('.')
            else:
                self.current_input = str(result)
            
            self.last_result = self.current_input
            
        except ZeroDivisionError:
            self.current_input = "Error: Div/0"
        except Exception as e:
            print(f"Error: {e}")
            self.current_input = "Error"
        
        self.update_display()
    
    def clear(self):
        """Clear all"""
        self.current_input = ""
        self.last_result = None
        self.update_display()
    
    def backspace(self):
        """Remove last character"""
        if self.current_input and self.current_input not in ["Error", "Error: Div/0"]:
            self.current_input = self.current_input[:-1]
            
            if not self.current_input:
                self.current_input = "0"
        
        self.update_display()
    
    def percentage(self):
        """Calculate percentage"""
        try:
            if self.current_input and self.current_input not in ["Error", "Error: Div/0"]:
                parts = self.current_input.split()
                if parts:
                    last_part = parts[-1]
                    if last_part.replace('.', '').replace('-', '').isdigit():
                        value = float(last_part)
                        parts[-1] = str(value / 100)
                        self.current_input = ''.join(parts)
        
        except Exception as e:
            print(f"Percentage error: {e}")
            self.current_input = "Error"
        
        self.update_display()
    
    def update_display(self):
        """Update display label"""
        if hasattr(self.root, 'ids'):
            display = self.root.ids.display
            if self.current_input == "":
                display.text = "0"
            else:
                display.text = self.current_input
    
    def toggle_theme(self):
        """Toggle between Dark Green/Black and Black/White themes"""
        self.is_dark_theme = not self.is_dark_theme
        
        if self.is_dark_theme:
            # Dark Green theme
            self.bg_color = [0.08, 0.08, 0.08, 1]  # Very dark black
            self.display_bg_color = [0.12, 0.12, 0.12, 1]  # Dark black
            self.button_color = [0.2, 0.35, 0.2, 1]  # Dark green
            self.operation_color = [0.15, 0.25, 0.15, 1]  # Darker green
            self.equal_color = [0.25, 0.45, 0.25, 1]  # Lighter green
            self.clear_button_color = [0.4, 0.2, 0.2, 1]  # Dark red
            self.text_color = [0.9, 1, 0.9, 1]  # Light green
            self.theme_switch_color = [0.3, 0.3, 0.3, 1]  # Gray
        else:
            # Black and White theme
            self.bg_color = [0.95, 0.95, 0.95, 1]  # Off white
            self.display_bg_color = [0.9, 0.9, 0.9, 1]  # Light gray
            self.button_color = [0.85, 0.85, 0.85, 1]  # Gray
            self.operation_color = [0.8, 0.8, 0.8, 1]  # Medium gray
            self.equal_color = [0.7, 0.7, 0.7, 1]  # Dark gray
            self.clear_button_color = [0.9, 0.6, 0.6, 1]  # Light red
            self.text_color = [0.1, 0.1, 0.1, 1]  # Almost black
            self.theme_switch_color = [0.5, 0.5, 0.5, 1]  # Gray


if __name__ == "__main__":
    CalculatorApp().run()