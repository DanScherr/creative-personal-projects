from sql_alchemy import db

class SensorModel(db.Model):


    '''
    TABLE SCHEMA
    '''
    __tablename__       = 'sensors'
    sensor_id           = db.Column(db.Integer, primary_key=True)
    sensor_name         = db.Column(db.String, nullable=False) # {sensor} {model/type} {What it does} {n*}
    sensor_password     = db.Column(db.String, nullable=False)

    '''
    CONSTRUCTOR
    '''
    def __init__(self) -> None:
        self.sensor_id = set

    
    '''
    SETTERs
    '''
    def set_sensor_id():
        return None


    '''
    WITHIN CLASS UNIVERSAL ESCOPE AND ACCESSABILITY
    '''
    @classmethod
    def find_sensor(cls, sensor_id):
        sensor = cls.query.filter_by(sensor_id=sensor_id).first()
        if sensor:
            return sensor
        else:
            return None

    '''
    WITHIN OBJECT ESPECIFIC ESCOPE AND ACCESSABILITY
    '''
    def save_sensor(self):
        db.session.add(self)
        db.session.commit()

    def delete_sensor(self):
        db.session.delete(self)
        db.session.commit()