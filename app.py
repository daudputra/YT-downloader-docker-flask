
# ! masih mendownload dengan program bukan dengan browser
# ! kadang masih tidak bisa menampilkan thumbnail meskipun di maxres dan hqdefault image nya ada
# TODO: buat pilihan resolusi

from flask import Flask, render_template, request, send_from_directory, make_response
from pytube import YouTube
from werkzeug.utils import secure_filename
import requests

app = Flask(__name__)

def get_thumbnail_video(video_id):
    maxres_url = f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
    hqdefault_url = f'https://img.youtube.com/vi/{video_id}/hqdefault.jpg'

    response = requests.head(maxres_url)
    if response.status_code == 200:
        return hqdefault_url
    else:
        return maxres_url


@app.route('/', methods=['GET', 'POST'])
def download_video():
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = video_url.split('/')[-1].split('?')[0]  
        

        try:
            yt = YouTube(video_url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution='360p').first()
            # stream = yt.streams.get_highest_resolution()
            if stream:
                download_path = 'C:/Users/ASUS Vivobook/Downloads'
                filename = secure_filename(yt.title) + '.mp4' if yt.title else video_id + '.mp4'
                stream.download(output_path=download_path, filename=filename)
                response = make_response(send_from_directory(download_path, filename, as_attachment=True, mimetype='video/mp4'))
                response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'
                img_url = get_thumbnail_video(video_id)
                
                return render_template('index.html', img_url=img_url, response=response, video_url=video_url)

            else:
                return render_template('index.html', error_message='No MP4 video available for download.')
        except Exception as e:
            return render_template('index.html', error_message=f'Error: {str(e)}')

    return render_template('index.html', video_info=None)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(5000))
