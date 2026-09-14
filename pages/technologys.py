

class technology:
    def __init__(self,page):
        self.page=page
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')
        self.ecommwebcomp=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[3]')
        self.mobileappcomp=page.locator('(//a[@href="https://www.tranktechnologies.com/mobile-app-development-company"])[1]')
        self.aiservice=page.locator('//a[@href="https://www.tranktechnologies.com/artificial-intelligence-development-services-company-india"]').first
#ecomme
        self.magntodev=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.codeigniterdev=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.bigcomm=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.cscartdev=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.noncommdev=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.laravaldev=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.drupaldev=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.joomladev=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.jomladev=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.expressdev=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.opencartdev=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.wordpressdev=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.shoifydev=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.nodejsdev=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.woodev=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.prestshopdev=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.wixdev=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.reactdev=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.ecommlist=[self.magntodev,self.codeigniterdev,self.bigcomm,self.cscartdev,self.noncommdev,self.laravaldev,self.drupaldev,
                   self.joomladev,self.jomladev,self.expressdev,self.opencartdev,self.wordpressdev,
                   self.shoifydev,self.nodejsdev,self.woodev,self.prestshopdev,self.wixdev,self.reactdev]
        #mobil app development
        self.navtiveapp=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.xamarinapp=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.flutterapp=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.swiftapp=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.entpriseapp=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.kotlinapp=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.ionicapp=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.appoinment=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mobiledevelopentlist=[self.navtiveapp,self.xamarinapp,self.flutterapp,self.swiftapp,self.entpriseapp,
                                   self.kotlinapp,self.ionicapp,self.appoinment]
        #AI
        self.aiservice=page.locator('//a[@href="https://www.tranktechnologies.com/artificial-intelligence-development-services-company-india"]').first
        self.Ailist=[self.aiservice]

    def ecomm_options(self):
        for i in self.ecommlist:
            self.technologies.hover()
            self.ecommwebcomp.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def mobileapp_options(self):
        for i in self.mobiledevelopentlist:
            self.technologies.hover()
            self.mobileappcomp.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def Ai_Options(self):
        for i in self.Ailist:
            self.technologies.hover()
            self.aiservice.hover()
            