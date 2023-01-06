'============================================JWT - json web token============================================'
import time
import jwt

SECRET_KEY='lm_40kn3mivsy$w$#-#7j+u11b3ld9b2bg@y!e5bekho8@vgz6'
ALGO='HS256'
ACCESS_TOKEN_EXPIRE = 5  # секунды
REFRESH_TOKEN_EXPIRE = 30


def encodeJWT(data):
    payload_access = {
        'data':data,
        'expiry':time.time() + ACCESS_TOKEN_EXPIRE
    }
    
    payload_refresh = {
        'data':data,
        'expiry':time.time() + REFRESH_TOKEN_EXPIRE
    }

    access_token = jwt.encode(payload_access, SECRET_KEY, algorithm=ALGO)
    refresh_token = jwt.encode(payload_refresh, SECRET_KEY, algorithm=ALGO)
    return {'access':access_token, 'refresh':refresh_token}

def decodeJWT(token:str):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGO])
        if decoded['expiry'] >= time.time():
            return decoded
        return 'Срок действия истек'
    except:
        return {}


def refreshJWT(refresh:str):
    decoded = decodeJWT(refresh)
    if decoded:
        return encodeJWT(decoded['data'])
    return {}