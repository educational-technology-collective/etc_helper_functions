class Config:
    '''
        base configuration class
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://proxy_ma_system:gZAMAyf2SEn96d@etc-db.cmb61qv9ob3s.us-east-1.rds.amazonaws.com/proxy_ma'
