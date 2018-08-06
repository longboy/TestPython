class Baidutest(object):
    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def get_url(self, url):
        self.driver.get(url)

    def quit_brower(self):
        self.driver.quit()
