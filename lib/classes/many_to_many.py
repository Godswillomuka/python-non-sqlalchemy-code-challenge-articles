class Article:
    all = []

    def __init__(self, author, magazine, title):

        if not (5 <= len(title) <= 50):
            print("Error: Title must be between 5 and 50 characters")
            return  
        self.author = author
        self.magazine = magazine
        self._title = title
        magazine._articles.append(self)
        author._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        print("Error: Title cannot be changed after initialization")


class Author:
    def __init__(self, name):

        if not isinstance(name, str) or len(name) == 0:
            print("Error: Author's name must be a non-empty string")
            return  
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        print("Error: Author's name cannot be changed once set")

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles)) if self._articles else None


class Magazine:
    all = []  

    def __init__(self, name, category):
        if len(name) < 2 or len(name) > 16:
            print("Error: Magazine name must be between 2 and 16 characters")
            return  
        if not isinstance(name, str):
            print("Error: Magazine name must be a string")
            return  
        if len(category) == 0:
            print("Error: Category cannot be empty")
            return  
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            print("Error: Name must be a string")
            return
        if len(value) < 2 or len(value) > 16:
            print("Error: Magazine name must be between 2 and 16 characters")
            return
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            print("Error: Category must be a string")
            return
        if value == "":
            print("Error: Category cannot be empty")
            return
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        if not self._articles:
            return None
        authors_count = {}
        for article in self._articles:
            authors_count[article.author] = authors_count.get(article.author, 0) + 1
        contributing_authors = [author for author, count in authors_count.items() if count > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine._articles), default=None)
