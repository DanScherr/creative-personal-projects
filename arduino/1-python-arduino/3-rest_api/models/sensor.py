from sql_alchemy import db

class SensorModel(db.Model):


    '''
    TABLE SCHEMA
    '''
    __tablename__       = 'sensor'
    sensor_id           = db.Column(db.String, primary_key=True)
    sensor_name         = db.Column(db.String, nullable=False) # {sensor} {model/type} {What it does} {n*}


    '''
    CONSTRUCTOR
    '''
    def __init__(self, sensor_id, sensor_name) -> None:
        self.sensor_id      = sensor_id
        self.sensor_name    = sensor_name

    
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
    def json(self): # convert dict to json
        return {
            'sensor_id'     : self.sensor_id,
            'sensor_name'   : self.sensor_name
        }
    
    def save_sensor(self):
        db.session.add(self)
        db.session.commit()

    def delete_sensor(self):
        db.session.delete(self)
        db.session.commit()