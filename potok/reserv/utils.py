from datetime import datetime, time
import pytz
from decimal import Decimal, ROUND_HALF_UP


discount = Decimal('0.20')
procent_zp = Decimal('0.14')

def get_local_time():
    city = 'Asia/Yerevan'
    timezone = pytz.timezone(city)
    current_date_and_time = datetime.now(timezone)
    current_time = current_date_and_time.time()
    return current_time

def get_local_date():
    city = 'Asia/Yerevan'
    timezone = pytz.timezone(city)
    current_date_and_time = datetime.now(timezone)
    return current_date_and_time.date()

def check_time_discount():
    first_zone = [time(12, 0), time(18, 0)]
    last_zone = [time(0, 0), time(2, 0)]
    if first_zone[0] < get_local_time() < first_zone[1] or last_zone[0] < get_local_time() < last_zone[1]:
        return True
    else:
        return False

def check_price(kal_count):
    if kal_count == 1:
        price = Decimal('10000.00')
        return price
    elif kal_count == 2:
        price = Decimal('17000.00')
        return price
    elif kal_count == 3:
        price = Decimal('23000.00')
        return price
    elif kal_count == 4:
        price = Decimal('23000.00')
        return price
    else:
        print('error PIZDETS')

def make_discount(price):
    final_price = price - (price * discount)
    rounded_final_price = final_price.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    return rounded_final_price

def calculate_ZP(price, discount, kal_count):
    price = price / kal_count
    if discount:
        zp = (make_discount(price) * procent_zp) * kal_count
        rounded_zp = zp.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        return rounded_zp
    else:
        zp = (price * procent_zp) * kal_count
        rounded_zp = zp.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        return rounded_zp

