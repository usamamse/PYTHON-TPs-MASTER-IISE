import logging

def log_error(message):
    logger = logging.getLogger('mon_logger')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('error.log')
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.error(message)

def read_file(filename):
    fichier = None  
    try:
        fichier = open(f'{filename}.txt', 'r')  
        lignes = fichier.readlines()
        for ligne in lignes:
            print(ligne.strip())  
    except FileNotFoundError:
        log_error("Le fichier n'existe pas!")

    finally:
        if fichier is not None:  
            fichier.close()

read_file('testExercice3')