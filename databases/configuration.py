import os
from definitions import ROOT_DIR


DB_TYPE = 'sqlite'
DB_RELATIVE_PATH = 'databases/test_db.db'
DB_PATH = os.path.join(ROOT_DIR, DB_RELATIVE_PATH)
