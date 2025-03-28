from abc import ABC, abstractmethod

class IStyleButton(ABC):
    @abstractmethod
    def setButtonStyle(self) -> str:
        pass

class ButtonStyleDefault(IStyleButton):
    def __init__(self):
        self.padding = "p-1"
        self.textColor = "text-white"
        self.bgColor = "bg-blue-500"
        #self.shadow = "shadow-xl"
        self.rounded = "rounded-sm"
        self.w = "w-50"
        self.h = "h-auto"
        self.text = "text-sm"
        self.placeHolder = "placeholder:text-md"


        attributes = [value for key, value in self.__dict__.items() if value is not None and key != 'style']
        self.style = " ".join(attributes)


    def setButtonStyle(self) -> str:
        return self.style

class ButtonStyleCustom(ButtonStyleDefault):
    def __init__(self,style):
        super().__init__()
        self.styleCustom = style


    def setButtonStyle(self) -> str:
        return f"{self.style} {self.styleCustom}"