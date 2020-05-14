import mysql.connector
import redis
from contextlib import contextmanager


class Sqlservice(object):

  HOST = 'n-adx-tidb-2'
  PORT = '4000'
  USER = 'adx'
  PWD = 'A7mS9a6ZAw9pGYYL'
  DBNAME = 'ad_bi'

  def __init__(self, host=HOST, port=PORT, pwd=PWD, user=USER, dbname=DBNAME, logger=None):
    self.logger = logger
    self.host = host
    self.port = port
    self.user = user
    self.pwd = pwd
    self.dbname = dbname
    self.dbs = None
    self.ctr_cursor = None
    self.created = False

  def __enter__(self):
    '''start a mysql service'''
    self.create()
    return self

  def __exit__(self, type, value, traceback):
    '''close a my sql service'''
    self.close()

  def create(self):
    self.dbs = mysql.connector.connect(
        host=self.host,
        port=self.port,
        user=self.user,
        passwd=self.pwd,
        database=self.dbname
    )
    self.ctr_cursor = self.dbs.cursor()
    self.created = True

  def close(self):
    if self.created:
      self.ctr_cursor.close()
      self.dbs.close()
      self.created = False
    else:
      pass

    return

  def get_ad_counts(self,
                    day='20200327',
                    country_code='total',
                    slot_id='total',
                    publisher_id='total',
                    mid='total',
                    traffic_source='total',
                    impr_count=10000):
    data = (day, country_code, slot_id, publisher_id,
            mid, traffic_source, impr_count)
    sql = """
          select count(ad_id) 
          from (select 
                      day,
                      ad_id,
                      impr_count,
                      click_count,
                      ctr,
                      cvr from r_day_stat_ad_effect 
                      where 
                      day=%s and 
                      country_code=%s and 
                      slot_id=%s and 
                      publisher_id=%s and  
                      mid=%s  and 
                      traffic_source=%s and 
                      test =0 and 
                      ctr > 0.0 and 
                      impr_count > %s) 
          ad_db
          """
    self.ctr_cursor.execute(sql, data)
    for x in self.ctr_cursor:
      if x[0]:
        return int(x[0])
    return 0

  def get_avg_ctr(self,
                  day='20200327',
                  country_code='total',
                  slot_id='total',
                  publisher_id='total',
                  mid='total',
                  traffic_source='total',
                  impr_count=10000):
    data = (day, country_code, slot_id, publisher_id,
            mid, traffic_source, impr_count)
    # data=(self.day,self.country_code,self.slot_id,self.publisher_id,self.mid,self.traffic_source,self.impr_count)
    sql = """
          select avg(ctr) 
          from (select day,
                       ad_id,
                       impr_count,
                       click_count,
                       ctr,
                       cvr from r_day_stat_ad_effect 
                       where 
                       day=%s and 
                       country_code=%s and 
                       slot_id=%s and 
                       publisher_id=%s and  
                       mid=%s and 
                       traffic_source=%s and
                       test=0 and 
                       ctr > 0.0 and 
                       impr_count > %s) 
          ad_db
      """
    self.ctr_cursor.execute(sql, data)
    for x in self.ctr_cursor:
      if x[0]:
        return float(x[0])
    return 0.0

  def get_min_ctr(self,
                  day='20200327',
                  country_code='total',
                  slot_id='total',
                  publisher_id='total',
                  mid='total',
                  traffic_source='total',
                  impr_count=10000):
    data = (day, country_code, slot_id, publisher_id,
            mid, traffic_source, impr_count)
    # data=(self.day,self.country_code,self.slot_id,self.publisher_id,self.mid,self.traffic_source,self.impr_count)
    sql = """
          select min(ctr) 
          from (select day,
                       ad_id,
                       impr_count,
                       click_count,
                       ctr,
                       cvr from r_day_stat_ad_effect 
                       where 
                        day=%s and 
                        country_code=%s and 
                        slot_id=%s and 
                        publisher_id=%s and  
                        mid=%s  and 
                        traffic_source=%s and 
                        test =0 and 
                        ctr > 0.0 and 
                        impr_count > %s) 
          ad_db
          """
    self.ctr_cursor.execute(sql, data)
    for x in self.ctr_cursor:
      if x[0]:
        return float(x[0])
    return 0.0

  def get_ad_info(self,
                  ad_id,
                  day='20200327',
                  country_code='total',
                  slot_id='total',
                  publisher_id='total',
                  mid='total',
                  traffic_source='total'):
    data = (day, country_code, slot_id,
            publisher_id, mid, traffic_source, ad_id)
    sql = """
          select 
          ctr, 
          impr_count, 
          click_count 
          from (select day,
                      ad_id,
                      impr_count,
                      click_count,
                      ctr,
                      cvr 
                      from r_day_stat_ad_effect 
                      where 
                      day=%s and 
                      country_code=%s and 
                      slot_id=%s and 
                      publisher_id=%s and  
                      mid=%s  and 
                      traffic_source=%s and 
                      test=0 and 
                      ad_id=%s
                  ) ad_db
          """
    self.ctr_cursor.execute(sql, data)
    for x in self.ctr_cursor:
      if x[0]:
        return [float(x[0]), int(x[1]), int(x[2])]
    return [0, 0, 0]
  
  # define a decorator
  def __call__(self, func):
    '''
    wrapper function

    the function should be like:
    def fun(..., ..., mysql_service = None):
      pass

    Args:
      function wanted to be implemented.

    Raise:
      NameError if mysql_service not in function parameters.
    '''
    def service_wrapper(*args, **kwargs):
      self.create()
      res = func(*args, **kwargs, mysql_service = self)
      self.close()
      return res
    return service_wrapper

class A():
  def __init__(self, msg):
    self.msg = msg
  
  @Sqlservice()
  def toy(self, mysql_service = None):
    print(f"this is initial message from {self.msg}")
    # print(data)
    print(mysql_service.get_ad_counts())
    print(mysql_service.get_avg_ctr())
    print(mysql_service.get_min_ctr())
    print(mysql_service.get_ad_info(ad_id='a2477423964992', day='20200327'))
    print(mysql_service.get_ad_info(ad_id='a2477423964992', day='20200328'))
    print(mysql_service.get_ad_info(ad_id='a2477423964992', day='20200329'))
    print()

if __name__ == "__main__":
  with Sqlservice() as rm:
    # rm = mysql_data(ctr_cursor,'logger')
    print(rm.get_ad_counts())
    print(rm.get_avg_ctr())
    print(rm.get_min_ctr())
    print(rm.get_ad_info(ad_id='a2477423964992', day='20200327'))
    print(rm.get_ad_info(ad_id='a2477423964992', day='20200328'))
    print(rm.get_ad_info(ad_id='a2477423964992', day='20200329'))
    print()

  @Sqlservice()
  def toy(data, mysql_service = None):
    print(data)
    print(mysql_service.get_ad_counts())
    print(mysql_service.get_avg_ctr())
    print(mysql_service.get_min_ctr())
    print(mysql_service.get_ad_info(ad_id='a2477423964992', day='20200327'))
    print(mysql_service.get_ad_info(ad_id='a2477423964992', day='20200328'))
    print(mysql_service.get_ad_info(ad_id='a2477423964992', day='20200329'))
    print()
  
  toy("This is from decorator")

  a = A("your Father")
  # aa = a.toy("Fuck you up, you mothorfucker!!!!")
  aa = a.toy()
  print(f"the result of toy from your Father {aa}")
  # rQ=redis.Redis(host='172.17.30.186',port=6380)
  # print(rQ.get('ap:'+'a2477423964992'))
