
import fresh_tomatoes
import media

whiplash = media.Movie("Whiplash",
                        "It depicts the relationship between an ambitious jazz student and an abusive instructor", "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg", "https://www.youtube.com/watch?v=ZZY-Ytrw2co")

atonement = media.Movie("Atonement",
                        "Fledgling writer Briony Tallis, as a thirteen-year-old, irrevocably changes the course of several lives when she accuses her older sister's lover of a crime he did not commit.", "https://upload.wikimedia.org/wikipedia/en/e/e4/Atonement_UK_poster.jpg", "https://www.youtube.com/watch?v=zRlkHu-R7yI")

BlackPanther = media.Movie("Black Panther",
                            "T'Challa, the King of Wakanda, rises to the throne in the isolated, technologically advanced African nation, but his claim is challenged by a vengeful outsider who was a childhood victim of T'Challa's father's mistake.", "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg", "https://www.youtube.com/watch?v=xjDjIWPwcPU")

dangal = media.Movie("Dangal",
                    "Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle towards glory at the Commonwealth Games in the face of societal oppression.", "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg", "https://www.youtube.com/watch?v=x_7YlGv9u1g")

queen = media.Movie("Queen",
                    "A Delhi girl from a traditional family sets out on a solo honeymoon after her marriage gets cancelled.", "https://upload.wikimedia.org/wikipedia/en/4/45/QueenMoviePoster7thMarch.jpg", "https://www.youtube.com/watch?v=KGC6vl3lzf0")

idiots = media.Movie("3 idiots",
                    "Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them idiots.", "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg", "https://www.youtube.com/watch?v=K0eDlFX9GMc")


movies = [whiplash, atonement, BlackPanther, dangal, queen, idiots]
fresh_tomatoes.open_movies_page(movies)
