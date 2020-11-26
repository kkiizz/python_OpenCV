import cv2
import os
from os.path import dirname, basename, join

def save_frame(video_path, per_sec=30):
    folder_path = dirname(video_path)
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print('読み込み失敗')
        return

    file_name, _ = os.path.splitext(os.path.basename(video_path))
    result_file_name = join(
        folder_path,
        file_name + "_result"
    )


    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print('fps: {}'.format(fps))
    print('動画時間: {} sec'.format(frame_count//fps))

    os.makedirs(result_file_name, exist_ok=True)

    for _frame_num in range(0, frame_count, fps*per_sec):
        cap.set(cv2.CAP_PROP_POS_FRAMES, _frame_num)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(
                join(
                    result_file_name,
                    str(int(_frame_num)//fps)+".jpg"
                ),
                frame
            )

if __name__ == "__main__":    
    path = ""
    save_frame(path)