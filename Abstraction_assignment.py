from abc import abstractmethod, ABC


class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
    def scroll(self):
        print("scroll in HP")

class Dell(TouchScreenLaptop):
    def scroll(self):
        print("Scroll in Dell")

class HPNotebook(HP):
    def scroll(self):
        print("Scroll in HPNotebook")

    def click(self):
        print("Click in HPNotebook")

class DellNotebook(Dell):
    def scroll(self):
        print("Scroll in DellNotebook")

    def click(self):
        print("Click in DellNotebook")

h = HPNotebook()
h.scroll()
h.click()

d = DellNotebook()
d.scroll()
d.click()