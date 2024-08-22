# Дополнительное практическое задание по модулю: "Классы и объекты."
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.

import time


def run_video(video):   # функция проигрывания видео по секунде
    for run in range(1, video.duration + 1):
        video.time_now = run
        print(video.time_now, end=' ')
        time.sleep(1)
    video.time_now = 0
    print("Конец видео")


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    # Перегружаем сравнение класса "User" на сравнение по именам
    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname

    # При обращении к строке возвращаем имя пользователя
    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    # Перегружаем сравнение класса "Video" на сравнение по имени видео
    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if (nickname, hash(password)) == (user.nickname, user.password):
                self.current_user = user

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user not in self.users:
            self.users.append(user)
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for vidio in args:
            if vidio not in self.videos:
                self.videos.append(vidio)

    def get_videos(self, find_key):
        get_list = []
        for vidio in self.videos:
            if find_key.upper() in vidio.title.upper():
                get_list.append(vidio.title)
        return get_list

    def watch_video(self, name_vidio):
        if self.current_user is not None:   # Проверка на авторизацию
            for video in self.videos:   # поиск видео
                if name_vidio == video.title:
                    if not video.adult_mode:    # Запуск видео и проверка на 18+
                        run_video(video)
                    if video.adult_mode and self.current_user.age >= 18:
                        run_video(video)
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
