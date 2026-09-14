class blog:
    def __init__(self,page):
            self.page=page
            self.blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
            self.blogappdev=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[2]')
            self.aiblog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"])')
            self.contantblog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"])')
            self.crmblog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"])')
            self.digitalblog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"])')
            self.ecommrceblog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
            self.emailblog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"])')
            self.graphicblog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
            self.softwareblog=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
            self.swdblog=page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
            self.uiuxblog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
            self.webdevblog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
            self.bloglist=[self.blogappdev,self.aiblog,self.contantblog,self.crmblog,self.digitalblog,self.ecommrceblog,
                           self.graphicblog,self.softwareblog,self.swdblog,self.uiuxblog,self.webdevblog
                           ]
            self.blog.click()
    def blog_options(self):
          for i in self.bloglist:
                i.click()
                self.page.wait_for_load_state("load")
                self.page.go_back()

        
