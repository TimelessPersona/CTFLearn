def binary_file_to_bytes(input_file, output_file):
    # 바이너리 파일을 읽어옵니다.
    with open(input_file, 'r') as file:
        binary_string = file.read().strip()

    # 바이너리 문자열의 길이를 8의 배수로 맞춥니다.
    while len(binary_string) % 8 != 0:
        binary_string = '0' + binary_string

    # 8비트씩 끊어서 바이트로 변환합니다.
    bytes_list = []
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        bytes_list.append(int(byte, 2))

    # 바이트 리스트를 문자열로 변환하여 output.txt 파일에 저장합니다.
    with open(output_file, 'w') as file:
        file.write(' '.join(map(str, bytes_list)))

# 파일 경로 설정
input_file = 'bin'
output_file = 'output.txt'

# 함수 호출
binary_file_to_bytes(input_file, output_file)
