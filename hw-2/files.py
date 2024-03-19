# В проекте мы работаем с медиа-файлами (аудио, видео, фото). Есть некоторый общий набор данных о файле,
# необходимый для реализации бизнес-логики (имя, размер, дата создания, владелец...).
# Для каждого типа медиа-фалов есть свой набор мета-данных
#
# Попробуйте написать классы для работы с медиа-файлами (они будут основой для пользовательского кода остальных команд).
# приведите примеры кода - как можно создать, обновить, удалить или провести какое-нибудь действие (конвертация, извлечение фич)
# над файлом (можно без реализации деталей)
#
# Суть задания - именно проектирование классовой иерархии, а не реализация самой логики.
# Поэтому достаточно, например, просто объявить метод .save(...)
# и в комментарии уточнить - что он должен делать, без конкретной реализации.
#
import datetime

# конфигурация Minio
MINIO_SERVER = 'http://localhost:8084'
MINIO_BUCKET_NAME = "test"
MINIO_ACCESS_KEY = "user"
MINIO_SECRET_KEY = "secret"


# Объявляем базовый класс, от которого будут наследоваться остальные
class BaseFile:

    def __init__(self, filename, user='admin'):
        self.filename = filename
        self.filesize = 0
        self.filetype = ''
        self.owner = user
        self.create_date = datetime.date.today()
        # далее по коду не используется, но выглядит полезным
        filename_parts = filename.split(filename)
        self._filename_without_extension = filename_parts[0]
        self._extension = filename_parts[1]

    def create(self):
        pass

    def open(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    # Попробуйте дописать классы для работы с файлами, расположенными не на локальном диске (облако, удаленный
    # сервер, s3-like storage)
    #
    # Кажется, что это плохой код и так делать нельзя и стоит написать отдельный класс для клиента minio,
    # но тогда это будет противоречить заданию
    def upload_file(self, MINIO_SERVER, MINIO_BUCKET_NAME, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, file_path):
        pass

    def get_file(MINIO_SERVER, MINIO_BUCKET_NAME, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, file_path):
        pass


# Объявили общий класс для медиа файлов и абстрактные методы, которые должны быть переопределены в потомках.
# В задании ничего нет про исключения, но если их нужно ловить, то я доделаю
class MediaFileClass(BaseFile):

    def play(self):
        raise NotImplementedError('Метод не поддерживается')

    def pause(self):
        raise NotImplementedError('Метод не поддерживается')

    def stop(self):
        raise NotImplementedError('Метод не поддерживается')

    def convert(self):
        raise NotImplementedError('Метод не поддерживается')


# Класс для работы с видео-файлами
class VideoFileClass(MediaFileClass):

    def __init__(self, filename):
        super().__init__(filename)
        self._filetype = 'Video'

    def play(self):
        print(f"Проигрываем видео-файл: {self.filename}")

    def pause(self):
        print(f"Приостановить проигрывания видео-файла: {self.filename}")

    def stop(self):
        print(f"Остановить проигрывания видео-файла: {self.filename}")

    def convert(self, media_format='avi'):
        print(f"Преобразовать видео-файл в другой формат: {self.filename}")


# Класс для работы с аудио-файлами
class AudioFileClass(MediaFileClass):

    def __init__(self, filename):
        super().__init__(filename)
        self._filetype = 'Audio'

    def play(self):
        print(f"Проигрываем аудио-файл: {self.filename}")

    def pause(self):
        print(f"Приостановить проигрывания аудио-файла: {self.filename}")

    def stop(self):
        print(f"Остановить проигрывания аудио-файла: {self.filename}")

    def convert(self, media_format='mp3'):
        print(f"Преобразовать аудио-файл в другой формат: {self.filename}")

# Класс для работы с изображениями/фото
class ImageFileClass(MediaFileClass):

    def __init__(self, filename):
        super().__init__(filename)
        self._filetype = 'Image'

    def play(self):
        print(f"Просматриваем изображение: {self.filename}")

    def convert(self, image_format='png'):
        print(f"Преобразовать изображение в другой формат: {self.filename}")


# примеры вызова методов классов
image = ImageFileClass('picture.jpg')
image.convert()

movie = VideoFileClass('movie.mp4')
movie.play()
movie.pause()
movie.stop()


# попробуйте ответить на вопросы: много ли кода придется дописать / переписать
# при добавлении новых типов файлов  и способов их хранения?
#
# Кажется, что не очень много, так как мы может наследоваться от базового класса
# и не дублировать общий код
class OfficeFileClass(BaseFile):

    def print(self):
        raise NotImplementedError('Метод не поддерживается')

    def edit(self):
        raise NotImplementedError('Метод не поддерживается')


class OfficeExcelFileClass(OfficeFileClass):

    def __init__(self, filename):
        super().__init__(filename)
        self._filetype = 'Excel'

    def print(self):
        print(f"Печать Excel-файла: {self.filename}")

    def edit(self):
        print(f"Редактирование Excel-файла: {self.filename}")


new_excel_file = OfficeExcelFileClass('new_excel_file.xlsx')
