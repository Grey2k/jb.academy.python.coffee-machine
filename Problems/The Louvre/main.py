class Painting:
    museum = 'Louvre'

    def __init__(self, title: str, artist: str, year: int) -> None:
        self.title = title
        self.artist = artist
        self.year = year

    def get_info(self) -> str:
        return f'"{self.title}" by {self.artist} ({self.year}) hangs in the {Painting.museum}.'


input_title = input().strip()
input_artist = input().strip()
input_year = int(input().strip())

picture = Painting(input_title, input_artist, input_year)
print(picture.get_info())
