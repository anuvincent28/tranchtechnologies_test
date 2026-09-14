class cls_Verti:
    def __init__(self,page):
        self.page = page

        #titles
        self.verticals = page.locator('(//a[text()="Verticals"])[1]')
        
        


        #verticals sub titles
        self.trading = page.locator('//li[@data-id="trading"]')
        self.r_and_ecom = page.locator('//strong[text()= "Retail and Ecommerce"]')
        self.healthcare = page.locator('//li[@data-id="healthcare"]')
        self.finetch = page.locator('//strong[text() = "Fintech"]')
        self.customapp = page.locator('//li[@data-id="customApp"]')
        #self.verticals_list = [self.trading,self.r_and_ecom,self.healthcare,self.finetch,self.customapp]


        #trading
        self.td1 = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.td2 = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.td3 = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.td4 = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.td5 = page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.td6 = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.td7 = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.td_list = [self.td1,self.td2,self.td3,self.td4,self.td5,self.td6,self.td7]

        #rae
        self.rae_1 = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.rae_2 = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.rae_list = [self.rae_1,self.rae_2]

        #hc
        self.hc1 = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.hc2 = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.hc_list = [self.hc1,self.hc2]

        #ft
        self.ft_1 = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.ft_2 = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        self.ft_list = [self.ft_1,self.ft_2]

        #ca
        self.ca_1 = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.ca_2 = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.ca_3 = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.ca_4 = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.ca_5 = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.ca_6 = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.ca_7 = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.ca_8 = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.ca_9 = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.ca_list = [self.ca_1,self.ca_2,self.ca_3,self.ca_4,self.ca_5,self.ca_6,self.ca_7,self.ca_8,self.ca_9]
    def click_trading_options(self):
        #self.list_of_list = [self.td_list,self.rae_list,self.hc_list,self.ft_list,self.ca_list]
    
        #self.list_of_list_index = 0
        #for y in self.verticals_list:
            
        for x in self.td_list:
                self.verticals.hover()
                self.trading.hover()
                x.click()
                self.page.wait_for_load_state()
                print(self.page.url)
                self.page.go_back()
            #self.list_of_list_index += 1
    def click_rae_options(self):
         for x in self.rae_list:
            self.verticals.hover()
            self.r_and_ecom.hover()
            x.click()
            self.page.wait_for_load_state()
            print(self.page.url)
            self.page.go_back()
    def click_hc_options(self):
             for x in self.hc_list:
                self.verticals.hover()
                self.healthcare.hover()
                x.click()
                self.page.wait_for_load_state()
                print(self.page.url)
                self.page.go_back()
    def click_ft_options(self):
             for x in self.ft_list:
                self.verticals.hover()
                self.finetch.hover()
                x.click()
                self.page.wait_for_load_state()
                print(self.page.url)
                self.page.go_back()
    def click_ca_options(self):
             for x in self.ca_list:
                self.verticals.hover()
                self.customapp.hover()
                x.click()
                self.page.wait_for_load_state()
                print(self.page.url)
                self.page.go_back()