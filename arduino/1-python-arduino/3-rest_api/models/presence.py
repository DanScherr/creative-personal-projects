from sql_alchemy import db
from datetime import datetime


class PresenceModel(db.Model):

    '''
    TABLE SCHEMA
    '''
    __tablename__       = 'presence' # table name
    presence_id         = db.Column(db.String(31), primary_key=True) 
    date_time_sent      = db.Column(db.String(26), nullable=False) # data-time of postted data
    date_time_received  = db.Column(db.String(26)) # data-time of received data
    sensor_id           = db.Column(db.String(5)) # a foreign key references in its parameters, table_title.column
    detection           = db.Column(db.Integer)
    
    '''
    CONSTRUCTOR
    '''
    def __init__(self, date_time_sent, sensor_id, detection) -> None:
        self.date_time_received = self.set_date_time_received()
        self.presence_id        = self.set_presence_id(sensor_id)
        self.date_time_sent     = self.set_date_time_sent(date_time_sent)
        self.sensor_id          = self.set_sensor_id(sensor_id)
        self.detection          = self.set_detection(detection)


    '''
    SETTERs
    '''
    def set_date_time_received(self):
        date_time_received = str(datetime.today())
        return date_time_received
    
    def set_presence_id(self, sensor_id):
        presence_id = self.date_time_received + sensor_id
        return presence_id
    
    def set_date_time_sent(self, date_time_sent):
        if (self.check_date_today(date_time_sent)):
            return date_time_sent
        else:
            return None
    
    def set_sensor_id(self, sensor_id):
        return sensor_id
    
    def set_detection(self, detection):
        return detection
    
    '''
    CHECKERs
    '''
    def check_date_today(self, date_time_sent):
        if_date = (self.date_time_received[0:10] == date_time_sent[0:10])
        if if_date:
            return True
        else:
            return False

    def check_year_today(self, date_time_sent):
        if_year = (self.date_time_received[:4] == date_time_sent[:4])
        if if_year:
            return True
        else:
            return False
        
    def check_month_today(self, date_time_sent):
        if_month = (self.date_time_received[5:7] == date_time_sent[5:7])
        if if_month:
            return True
        else:
            return False
        
    def check_day_today(self, date_time_sent):
        if_day = (self.date_time_received[8:10] == date_time_sent[8:10])
        if if_day:
            return True
        else:
            return False


    '''
    WITHIN CLASS UNIVERSAL ESCOPE AND ACCESSABILITY
    '''
    @classmethod
    def find_presence(cls, presence_id):
        presence = cls.query.filter_by(presence_id).first() # returns first found queried object
        if presence:
            return presence # return object
        else:
            return None

    '''
    WITHIN OBJECT ESPECIFIC ESCOPE AND ACCESSABILITY
    '''
    def json(self): # convert dict to json
        return {
            'presence_id'           : self.presence_id,
            'date_time_sent'        : self.date_time_sent,
            'date_time_received'    : self.date_time_received,
            'sensor_id'             : self.sensor_id,
            'detection'             : self.detection
        }
    
    def save_presence(self) -> None: # saving object instance, each object is a line
        db.session.add(self)
        db.session.commit()

    def delete_presence(self) -> None: # deleting object instance, each object is a line
        db.session.delete(self)
        db.session.commit()
    
