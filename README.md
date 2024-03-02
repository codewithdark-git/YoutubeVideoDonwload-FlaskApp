# Flask YouTube Video Downloader

This is a simple Flask web application for downloading YouTube videos. It allows users to input a YouTube video URL, and the application will download the highest resolution video stream. The downloaded videos will be saved in the `static/Download` directory.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/flask-youtube-downloader.git
cd flask-youtube-downloader
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

The application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

## Usage

1. Open the application in your web browser.
2. Paste a valid YouTube video URL in the provided input field.
3. Click the "Download" button to initiate the download process.

Please note that downloading copyrighted material without permission may violate YouTube's terms of service.

## Dependencies

- Flask
- pytube

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - A lightweight WSGI web application framework in Python.
- [pytube](https://github.com/pytube/pytube) - A lightweight and dependency-free Python library for downloading YouTube videos.
