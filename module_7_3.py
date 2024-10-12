import string

class WordsFinder:
    def __init__(self, *file_names):
        # сохраняем имена файлов
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        # Перебираем все файлы
        for file_name in self.file_names:
            try:
                # Открываем каждый файл с помощью with
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Читаем текст файла, преобразуем в нижний регистр
                    text = file.read().lower()
                    # Заменяем пунктуацию на пустые строки
                    for punct in string.punctuation:
                        text = text.replace(punct, "")
                    # Разделяем текст на слова по пробелам
                    words = text.split()
                    # Записываем слова в словарь, где ключ - название файла, а значение - список слов
                    all_words[file_name] = words
            except FileNotFoundError:
                # Если файл не найден, выводим сообщение
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        word = word.lower()  # игнорируем регистр
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                # Возвращаем позицию первого вхождения слова (нумерация с 1)
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()  # игнорируем регистр
        result = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            # Считаем количество вхождений слова
            result[file_name] = words.count(word)
        return result

# Пример использования:
finder = WordsFinder('test_file.txt')

# Выводим все слова из файла
print(finder.get_all_words())

# Находим позицию слова 'text'
print(finder.find('text'))

# Считаем количество вхождений слова 'text'
print(finder.count('text'))
