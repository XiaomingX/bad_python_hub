import ffmpeg

def convert_mp4_to_webm(input_file, output_file):
    try:
        # 使用ffmpeg进行转换
        ffmpeg.input(input_file).output(output_file, vcodec='libvpx', acodec='libvorbis').run()
        print(f"成功将 {input_file} 转换为 {output_file}")
    except ffmpeg.Error as e:
        print(f"转换失败: {e.stderr.decode()}")  # 输出详细错误信息

# 示例调用
input_mp4 = 'video.mp4'  # 输入文件名
output_webm = 'output.webm'  # 输出文件名
convert_mp4_to_webm(input_mp4, output_webm)