from flask import Flask, render_template, request, send_from_directory, make_response
from pytube import YouTube
from werkzeug.utils import secure_filename
import os
import requests

app = Flask(__name__)

def get_video_info(video_url):
    try:
        embed_url = f'https://noembed.com/embed?url={video_url}'
        response = requests.get(embed_url)
        response.raise_for_status()
        data = response.json()
        if 'thumbnail_url' in data:
            return {'thumbnail_url': data['thumbnail_url']}
    except Exception as e:
        print(f'Error fetching video info: {e}')
    return None


@app.route('/', methods=['GET', 'POST'])
def download_video():
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_info = get_video_info(video_url)

        try:
            yt = YouTube(video_url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            if stream:
                filename = secure_filename(yt.title) + '.mp4'
                stream.download(output_path='downloads/', filename=filename)
                response = make_response(send_from_directory('downloads/', filename, as_attachment=True, mimetype='video/mp4'))
                response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
            else:
                return render_template('index.html', error_message='No MP4 video available for download.')
        except Exception as e:
            return render_template('index.html', error_message=f'Error: {str(e)}', video_info=video_info)

    return render_template('index.html', video_info=None)

if __name__ == '__main__':
    os.makedirs('downloads', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=int(5000))
