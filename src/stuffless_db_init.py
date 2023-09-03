from stuffless_model import StufflessItem, stufflessDB
import logging


def init_db():
    """
    Inicializa o banco de dados
    """
    try:
        logging.info('Initializing database')
        with stufflessDB:
            stufflessDB.create_tables([StufflessItem])
        logging.info('Tables created')
    except Exception as e:
        logging.error(f'Error initializing database: {e}')
        raise e
