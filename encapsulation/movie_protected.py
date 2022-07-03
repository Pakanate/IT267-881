class Movie:
    def __init__(self) -> None:
        #ตัวแปร protected ขึ้นต้นด้วย underscore 1 ครั้ง
        self._title = None
        self._year = None
        self._genre = None
    
    #เมธอด protected ขึ้นต้นด้วย underscore 1 ครั้ง
    def _add_movie(self,title:str,year:int,genre:str):
        self._title = title
        self._year = year
        self._genre = genre
    
    def _getmovie_detail(self):
        print(f'Title: {self._title}')
        print(f'Year: {self._year}')
        print(f'Genre: {self._genre}')

#คลาส Movie, Documentary อยู่ในไฟล์เดียวกัน จึงไม่ต้อง import
class Documentary(Movie):
    def __init__(self) -> None:
        Movie.__init__(self) #super().__init__()
    
    def add_channel(self,ch:str):
        self.channel = ch
    
    def _getmovie_detail(self):
        #super()._getmovie_detail()
        Movie._getmovie_detail(self)
        print(f'Channel: {self.channel}')

#สร้าง object
if __name__ == '__main__':
    m1 = Documentary()
    m1._add_movie('My Octopus Teacher',2020,'Documentary')
    m1.add_channel('NetFlix')
    m1._getmovie_detail() #เรียกใช้ของ Documenatary (overriding method)

