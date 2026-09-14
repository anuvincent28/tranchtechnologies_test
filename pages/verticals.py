class vertical:
    def __init__(self,page):
        self.page=page
        self.vertic=page.locator('(//a[text()="Verticals"])[1]')
        self.trading=page.locator('(//a[text()="Verticals"])[1]')
        self.retail=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.healthcare=page.locator('(//a[@href="https://www.tranktechnologies.com/healthcare-mobile-app-development-company"])[1]')
        self.fintech=page.locator('(//a[@href="https://www.tranktechnologies.com/fintech-mobile-app-development-company"])[1]')
        self.customeapp=page.locator('(//a[@href="#"])[4]')
        # Vertical trading menu list
        self.sttrade=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.papertr=page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.cfdtr=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.stdtr=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.algotr=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.customtr=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.webportal=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.tradinglist=[self.sttrade,self.papertr,self.cfdtr,self.stdtr,self.algotr,self.customtr,
                          self.webportal]
        #Retailsand ecomm
        self.ecommweb=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.ecommapp=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.retaillist=[self.ecommweb,self.ecommapp]
    #healthcare
        self.nutrition=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.health=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.healthcarelist=[self.nutrition,self.health]
    #fintech
        self.pos=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        self.fintechlist=[self.pos,self.crypto]
    #customapp
        self.desktopapp=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.hrmdev=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.traveldev=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.datedev=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.crmdev=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.crmddev=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.erpdev=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.elearndev=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.estatedev=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.customlist=[self.desktopapp,self.hrmdev,self.traveldev,self.datedev,self.crmdev,self.crmddev,self.erpdev,
                         self.elearndev,self.estatedev]
    def trading_options(self):
        for i in self.tradinglist:
            self.vertic.hover()
            self.trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def retails_options(self):
        for i in self.retaillist:
            self.vertic.hover()
            self.retail.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def healthcare_options(self):
        for i in self.healthcarelist:
            self.vertic.hover()
            self.healthcare.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def fintech_options(self):
        for i in self.fintechlist:
            self.vertic.hover()
            self.fintech.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    def customs_options(self):
        for i in self.customlist:
            self.vertic.hover()
            self.customeapp.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
    





