import os

YOLO = "C:\\yolo-V8\\runs\\detect\\predict-10\\labels\\" #yolov8의 pretrained model로 추론 결과 txt 경로
DATASET = 'C:\\yolo-V8\\results\\' # person class만 추출해서 number 바꿔서 저장할 경로

yolo_file = os.listdir(YOLO)

cnt = 0
for file_name in yolo_file:
    if not file_name.endswith('.txt'):
        continue 

    file_path = YOLO + file_name
    with open(file_path, 'r') as f: 
        for line in f.readlines():
            if line.split()[0] == '0': # 클래스가 사람인 경우만
                line = list(line)
                line[0] = '2' # class number 0로 변경
                line = ''.join(line).strip()
                print(line)
                data_path = DATASET + file_name
                with open(data_path, "a") as fd:
                    fd.write(line+"\n")
                cnt += 1
print(f'{cnt}라인을 변경했습니다.')
