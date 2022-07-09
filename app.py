from flask import Flask, render_template, request, redirect
import youtube_dl
import pytube
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')



@app.route('/download', methods=["POST", "GET"])


# def download():
#	url = request.form["url"]
#    url = pytube.YouTube(str(link.get()))
#    video = url.streams.first()
#    return video.download()



def download():
	url = request.form["url"]

	with youtube_dl.YoutubeDL() as ydl:
		url = ydl.extract_info(url, download=False)
		print(url)
		try:
			download_link = url["entries"][-1]["formats"][-1]["url"]
		except:
			download_link = url["formats"][-1]["url"]
		return redirect(download_link+"&dl=1")


if __name__ == '__main__':
	app.run(host = "0.0.0.0",port=5000)
