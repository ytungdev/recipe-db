class Recipe:
    """Create Recipe object.

    ### Parameters
    - name : str
    - name_alt : str
    - style :str [western, chinese, japanese]
    - meal : str [breakfast, lunch, dinner, light]
    - ingredients : list
    - steps : str
    """
    def __init__(self, name=None, name_alt=None, style=None, meal=None, ingredients=None, steps=None) -> None:
        self.name = name
        self.name_alt = name_alt
        self.style = style
        self.meal = meal
        self.ingredients = ingredients
        self.steps = steps

    def format(self):
        res = {
            'name':self.name,
            'name_alt':self.name_alt,
            'style':self.style,
            'meal':self.meal,
            'ingredients':self.ingredients,
            'steps':self.steps
        }
        return res
    
    def example(self):
        self.name = '薑汁撞奶'
        self.name_alt = 'Ginger milk curd'
        self.style = 'chinese'
        self.meal = 'light'
        self.ingredients = ['薑','奶']