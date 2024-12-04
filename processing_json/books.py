from json import load

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\data_sets\\books.json")

data=load(f)

# for book in data:

#     print(book)

# print all titles

all_title=[book.get("title") for book in data]

# print(all_title)

# print pages < 250

page_filter=[book.get("title")for book in data if book.get("pages")<250]

# print(page_filter)

# print all genres

all_genres=[book.get("genre")for book in data]

# print(set(all_genres))

# print geners count

genre_count={genre:all_genres.count(genre)for genre in all_genres}

# print(genre_count)

# print costly car

costly_book=max(data,key=lambda d:d.get("price"))

# print(costly_book)

# author with more than one book

author_book=[book.get("author")for book in data]

author_count={author:author_book.count(author)for author in author_book}

print([k for k,v in author_count.items() if v>1])