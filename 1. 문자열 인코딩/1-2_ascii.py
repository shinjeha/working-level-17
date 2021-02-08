# 다음 코드를 실행하기 위해서는 별도 모듈이 필요하지 않습니다.

def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)

    hex_data_as_str = ' '.join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = ' '.join("{0}".format(int(c)) for c in byte_data)
    print('\'' + text + '\' 문자열 길이: {0}'.format(len(text)))
    print('\'' + text + '\' 전체 문자를 표현하는 데 사용한 바이트 수: {0} 바이트'.format(len(byte_data)))
    print('\'' + text + '\' 16진수 값: {0}'.format(hex_data_as_str))
    print('\'' + text + '\' 10진수 값: {0}'.format(int_data_as_str))


print_text('Hello', 'ascii')

"""
'Hello' 문자열 길이: 5
'Hello' 전체 문자를 표현하는 데 사용한 바이트 수: 5 바이트
'Hello' 16진수 값: 0x48 0x65 0x6c 0x6c 0x6f
'Hello' 10진수 값: 72 101 108 108 111
"""