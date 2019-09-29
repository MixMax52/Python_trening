class Locators:
    def __init__(self):
        self.search_string = "//input[@id='text']"
        self.search_button = "//button[@type='submit']"

        # Locators for test WEATHER
        self.select_weather = "//span[text()=' в нижнем новгороде']"
        self.result_weather = "/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/ul/li[1]/div/div[1]/h2/a/div[2]"

        # Locators for test LIPETSK
        self.result_lipetsk = "//div[text()='Липецк']"

        # Locators for test LOTO
        self.result_loto = "//a[text()='лото']"

        # Locators for test IMAGES
        self.button_img = "//a[@data-id='images']"
        self.result_img_myTape = "//a[text()='Моя лента']"
        self.result_img_myCollections = "//a[text()='Мои коллекции']"