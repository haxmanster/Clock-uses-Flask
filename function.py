

def normalizacja_kata():
  if suma_katow > 0:
    if suma_katow < 0:
      return suma_katow
    return suma_katow
  if suma_katow < -180:
    return suma_katow + 360
  if suma_katow >= 180:
    return suma_katow
  return -suma_katow
