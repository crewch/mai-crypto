from pygost import gost34112012256


print(gost34112012256.new(bytes("Крючков Артемий Владимирович", 'utf-8')).digest())

# b'\xef\xe0\xc6\x88m\x12\xc6\xdc\xc4[@\xbb\x11\xf1\xbd\xfcQ-m\x91\xab\xdb\x03\xce\x15\xa3`H\xe6\xba\x05\x18'
# Вариант 8
# 8 == JH
