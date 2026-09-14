class contact:
    def __init__(self,page):
        self.page=page
        self.contactus=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
    # footer 
        self.develomentwebsite=page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
        self.devlopmentwb=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
        self.developmentportal=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
        self.devlopmentapp=page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
        self.developmentandroid=page.locator('//a[@href="https://www.tranktechnologies.com/android-mobile-app-development-company"]')
        self.developmenthybrid=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.developmentplatform=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
        self.developmenprogressive=page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')
        self.logodesign=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.bannerdesign=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packingdesign=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.buinesscards=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')
        self.appdesign=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.webdesign=page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.identitydesign=page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')
        self.contactuslist=[self.develomentwebsite,self.devlopmentwb,self.developmentportal,self.devlopmentapp,
                            self.developmentandroid,self.developmenthybrid,self.developmentplatform,self.developmenprogressive,
                            self.logodesign,self.bannerdesign,self.packingdesign,self.buinesscards,self.appdesign,self.webdesign,
                            self.identitydesign]
    # Social Media Pages
        self.fb=page.locator('//a[@href="https://www.facebook.com/TrankTechnologies"]')
        self.linkedin=page.locator('//a[@href="https://in.linkedin.com/company/trank-technologies-official"]')
        self.insta=page.locator('//a[@href="https://www.instagram.com/tranktechnologies/"]')
        self.pinterest=page.locator('//a[@href="https://in.pinterest.com/tranktechnologies12/"]')
        self.twitter=page.locator('(//a[@href="https://twitter.com/tranktechno"]')
        self.youtube=page.locator('//a[@href="https://www.youtube.com/channel/UCWu1Y-tfrXf-Utpaft830Cg]')
        self.quora=page.locator('//a[@href="https://www.quora.com/profile/Trank-Technologies-1"]')
        self.medialist=[self.fb,self.linkedin,self.insta,self.pinterest,self.twitter,self.youtube,self.quora]   
        self.contactus.click()
    def contactus_options(self):
            for i in self.contactuslist:
                i.click()
                self.page.wait_for_load_state("load")
                self.page.go_back()
    def media_options(self):
         self.contactus.click()
         self.page.wait_for_load_state("load")
         self.medialist=[self.fb,self.linkedin,self.insta,self.pinterest,self.twitter,self.youtube,self.quora] 
         for i in self.medialist:
              with self.page.context.expect_page() as new_page_info:
                   i.click()
                   new_tab=new_page_info.value
                   new_tab.wait_for_load_state("load")
                   new_tab.close()
             

    
    
