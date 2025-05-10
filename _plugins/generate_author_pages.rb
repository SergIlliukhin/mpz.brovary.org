module Jekyll
  class AuthorPageGenerator < Generator
    safe true

    def generate(site)
      site.data['authors'].each do |author|
        site.pages << AuthorPage.new(site, author)
      end
    end
  end

  class AuthorPage < Page
    def initialize(site, author)
      @site = site
      @base = site.source
      @dir = 'author'
      @name = "#{author['login']}.html"

      self.process(@name)
      self.read_yaml(File.join(@base, '_layouts'), 'author.html')
      
      self.data['author'] = author['login']
      self.data['title'] = author['name']
      self.data['description'] = "Статті автора #{author['name']}"
    end
  end
end 