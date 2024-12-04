#movie
#title,rating,run_time,director,genre
#ARM
#KGF

class Movie:

    title:str

    rating:int

    run_time:int

    director:str 
    
    genre: str


    def set_movie(self,title,rating,run_time,director,genre):

        self.title=title

        self.rating=rating

        self.run_time=run_time

        self.director=director

        self.genre=genre

    def display(self):

        print(self.title,self.rating,self.run_time,self.director,self.genre)

movie_instance1=Movie()

movie_instance2=Movie()

movie_instance1.set_movie("ARM",7.7,2.45,"Jithin Lal","ComedyDram")

movie_instance2.set_movie("KGF",8.8,2.50,"Prasanth Neel","ACTION")

movie_instance1.display()

movie_instance2.display()