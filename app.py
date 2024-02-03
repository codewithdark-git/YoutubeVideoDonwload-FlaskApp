from flask import Flask, render_template, jsonify, request, send_from_directory
import os
import uuid
import threading
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form.get('link')
        if link:
            download_thread = threading.Thread(target=download_video, args=(link,))
            download_thread.start()
    return render_template('index.html')



def download_video(link):
    with app.app_context():
        try:
            url = YouTube(link)
            video_stream = url.streams.get_highest_resolution()
            
            if video_stream:
                download_path = "static\\Download"
                filename = f"{str(uuid.uuid4())}.MKV"
                
                video_stream.download(output_path=download_path, filename=filename)
                response_data = {"status": "success", "message": "Download completed successfully."}
            else:
                response_data = {"status": "error", "message": "No suitable video stream found."}
        except Exception as e:
            response_data = {"status": "error", "message": f"Download failed: {str(e)}"}
            print(f"Download failed: {str(e)}")
        
        return jsonify(response_data)




if not os.path.exists("static"):
    os.makedirs("static")

if __name__ == '__main__':
    app.run(debug=True)
