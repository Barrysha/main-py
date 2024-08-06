class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and hash(user.password) == hash(password):
                self.current_user = user
                return True
            elif user.nickname == nickname and user.password != password:
            	print(f"Неверный пароль, попробуйте ещё раз, {nickname}.")
            	return False
        if user.nickname not in self.users:##########
            print("Такого пользователя не обнаружено. зарегестрируйтесь.")
        return False

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует.")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print("Вы успешно зарегистрировались.")

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result
        
    def watch_video(self, video_title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return
        for video in self.videos:
            if video.title == video_title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                    return
                else:
                    # Здесь должна быть логика воспроизведения видео,
                    # которую мы не затрагивали в темах.
                    # Если мне стоит её добавить, дайте знать как.
                    print(f"Конец видео '{video_title}'")
                    break
        else:
            print("Видео не найдено.")

print("_" * 50, "\n")
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
print("_" * 50, "\n")
ur.add(v1, v2)

# Проверка поиска
print("_" * 50, "\n")
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
print("_" * 50, "\n")
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
print("_" * 50, "\n")
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
#ur.log_out()
ur.log_in("Vasyqa", "1234trew")

# Попытка воспроизведения несуществующего видео
print("_" * 50, "\n")
ur.watch_video('Лучший язык программирования 2024 года!')
