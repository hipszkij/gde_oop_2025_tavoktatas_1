# Target interface (az új rendszer az alábbi interfészt használja)

class CarInterface:
    def drive(self):
        raise NotImplementedError("Subclasses should implement this!")