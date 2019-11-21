class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "root",
        "HOST":"localhost",
        "PORT":"3306",
        "Name": "MysqlHelloFlask"
    }
    def get_db_info(self):
        engine = self.dbinfo.get("ENGINE") or "sqlite"
        driver = self.dbinfo.get("DRIVER") or ""
        user = self.dbinfo.get("USER") or ""
        password = self.dbinfo.get("PASSWORD") or ""
        host = self.dbinfo.get("HOST") or ""
        port = self.dbinfo.get("PORT") or ""
        name = self.dbinfo.get("Name") or ""
        return engine

    SQLALCHEMY_DATABASE_URI = get_db_info();


class DevelopConfig(Config):
    DEBUG = True
    dbinfo={
        "ENGINE":"mysql2",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"root",
        "HOST": "localhost",
        "PORT": "3306",
        "Name":"MysqlHelloFlask"
    }