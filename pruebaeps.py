



from urllib.request import urlopen

class WebClient(object):
  """WebClient class"""
  def __init__(self):       #self es como this
      super(WebClient, self).__init__()

  def download_page(arg):
      # connect to the web site
      f = urlopen("http://www.eps.udl.cat/ca/")
      # get the download_page
      page = f.read()
      # close the connection
      f.close()
      return page


  def run(self):
      # download a web pag
      page = self.download_page()
      # search activities in web pag
      # print the activities
      print(page)


if __name__ == "__main__":
  c = WebClient()
  c.run()
