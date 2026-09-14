class C_tech:
    def __init__(self,page):
        self.page = page

        #titles
        self.technologies = page.locator('(//a[text() = "Technologies"])[1]')

        #tech catogories
        self.ec = page.locator('(//strong[text() = "eCommerce Development"])')
        self.mad = page.locator('(//strong[text() = "Mobile App Development"])')
        self.ai = page.locator('(//strong[text() = "Artificial Intelligence"])')

        #tech ec sub categories
        self.ec1 = page.locator('(//a[text() = "Magento Development"])')
        self.ec2 = page.locator('(//a[text() = "Codeigniter Development"])[1]')
        self.ec3 = page.locator('(//a[text() = "Big Commerce"])[1]')
        self.ec4 = page.locator('(//a[text() = "CS-Cart Development"])[1]')
        self.ec5 = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.ec6 = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.ec7 = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.ec8 = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.ec9 = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.ec10 = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.ec11 = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.ec12 = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.ec13 = page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.ec14 = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.ec15 = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.ec16 = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.ec17 = page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.ec_list = [self.ec1,self.ec2,self.ec3,self.ec4,self.ec5,self.ec6,self.ec7,self.ec8,self.ec9,self.ec10,self.ec11,self.ec12,self.ec13,self.ec14,self.ec15,self.ec16,self.ec17]

        #tech mad sub categories
        self.mad1 = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.mad2 = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.mad3 = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.mad4 = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.mad5 = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.mad6 = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mad_list = [self.mad1,self.mad2,self.mad3,self.mad4,self.mad5,self.mad6]

    def ec_options(self):
        for x in self.ec_list:
            self.technologies.hover()
            self.ec.hover()
            x.click()

    def mad_options(self):
        for x in self.mad_list:
            self.technologies.hover()
            self.mad.hover()
            x.click()

    def ai_options(self):
        self.technologies.hover()
        self.ai.click()
                    





        