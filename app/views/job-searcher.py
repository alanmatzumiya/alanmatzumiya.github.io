from webbrowser import open_new_tab


class WebSite:
    names = (
        "indeed",
        "bumeran",
        "occ",
        "computrabajo",
        "linkedin"
    )
    urls = (
        "https://mx.indeed.com/",
        "https://www.bumeran.com.mx/",
        "https://www.occ.com.mx/",
        "https://mx.computrabajo.com/",
        "https://www.linkedin.com/"
    )
    page = {name: url for name, url in zip(names, urls)}

    @staticmethod
    def geturl(name):
        return WebSite.page.get(name)

    @staticmethod
    def openurl(name):
        open_new_tab(WebSite.geturl(name))

    @staticmethod
    def open_all():
        for url in WebSite.urls:
            open_new_tab(url)
