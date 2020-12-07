from websocket import create_connection
def decodews(hashstr):
    payload = hashstr[1] & 127
    print(payload)
    if payload == 127:
        extend_payload_len = hashstr[2:10]
        mask = hashstr[10:14]
        decoded = hashstr[14:]
    # 当位运算结果等于127时,则第3-10个字节为数据长度
    # 第11-14字节为mask 解密所需字符串
    # 则数据为第15字节至结尾

    if payload == 126:
        extend_payload_len = hashstr[2:4]
        mask = hashstr[4:8]
        decoded = hashstr[8:]
    # 当位运算结果等于126时,则第3-4个字节为数据长度
    # 第5-8字节为mask 解密所需字符串
    # 则数据为第9字节至结尾

    if payload <= 125:
        extend_payload_len = None
        mask = hashstr[2:6]
        decoded = hashstr[6:]

    # 当位运算结果小于等于125时,则这个数字就是数据的长度
    # 第3-6字节为mask 解密所需字符串
    # 则数据为第7字节至结尾

    str_byte = bytearray()
    # b'\x81 \x85s \x92a\x10\x1b \xf7\r|\x1c' <126
    for i in range(len(decoded)):  # 0  \xf7 ^ \x92a 1 \r ^ \x10 \x1c ^ \x1b
        byte = decoded[i] ^ mask[i % 4]
        str_byte.append(byte)
    print(str_byte)
    return str_byte

ws = create_connection("wss://wss.xsj052.com/", timeout=5)
fuck = ws.recv()


decodews(fuck)

print(fuck.decode("utf-16"))

