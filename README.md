# python_OpenCV
OpenCVを使った、特定の動画から一定の間隔でフレームを取得するものです。

## 環境
- os: macOS catalina 10.15.7
- python: 3.8.0
- OpenCV: 4.4.0

## def save_frame(video_path, per_sec=30)

- video_path: 対象となる動画ファイルのpath
- per_sec:　何秒ごとの画像がほしいか、秒数を選択。デフォルトは30秒

## 出力形式
- 出力されるファイルは、動画が保存してある場所と同じところが選択される。
- また、そのファイル名は、"{動画名}_result"という形で出力される。
- 画像名は、"{秒数}.jpg"の形式で出力される。
