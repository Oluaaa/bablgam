def print_file_content(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            print(file.read())
    except Exception as error:
        print(f'Файл не найден')

