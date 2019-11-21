def get_db_info(dbinfo):
	engine = dbinfo.get("ENGINE") or "sqlite"
	driver = dbinfo.get("DRIVER") or ""
	users = dbinfo.get("USER") or ""
	password = dbinfo.get("PASSWORD") or ""
	host = dbinfo.get("HOST") or ""
	port = dbinfo.get("PORT") or ""
	database = dbinfo.get("DATABASE") or ""
	return "{}+{}://{}:{}@{}:{}/{}".format(engine,driver,users,password,host,port,database)

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
        "DATABASE": "MysqlHelloFlask"
    }
    SQLALCHEMY_DATABASE_URI = get_db_info(dbinfo);


class DevelopConfig(Config):
    DEBUG = True
    dbinfo={
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"root",
        "HOST": "localhost",
        "PORT": "3306",
        "DATABASE":"MysqlHelloFlask"
    }
    SQLALCHEMY_DATABASE_URI = get_db_info(dbinfo);

envs={
	"develop":DevelopConfig,
	"orgin":Config
}
