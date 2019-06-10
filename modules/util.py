def check():
    try:
        with open('IMPORTANT.txt', 'r') as file:
            text = file.read()
            if 'ya malaletniy debil kstati' in text.lower():
                return True

            else:
                return False

    except FileExistsError:
        return False

    except FileNotFoundError:
        return False
