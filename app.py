from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
# For decoding audio
from ffmpy import FFmpeg
import sox
import io
import os
# Imports the Google Cloud client library
# [START migration_import]
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
# [END migration_import]

import base64

app = Flask(__name__)

UPLOAD_FOLDER = './'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/transcribe', methods = ['POST'])
def transcribe():
     file = request.files['file']
     if file.filename == '':
            flash('No selected file')
            return jsonify({"error" : "No file."})
     if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # [START speech_quickstart]
            # Set environment variable for GOOGLE_APPLICATION_CREDENTIALS
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "static/credentials.json"

            # Instantiates a client
            # [START migration_client]
            client = speech.SpeechClient()
            # [END migration_client]

            # The name of the audio file to encode
            file_name = os.path.join(
                os.path.dirname(__file__),
                'audio.wav')

            # first use ffmpeg to convert to flac
            # can't convert directly to raw for some reason. This is hax
            ff = FFmpeg(
                inputs = {'audio.wav' : None},
                outputs = {'audio.flac' : "-y"}
            )
            ff.run()

            # then use sox to convert to raw
            # create transformer
            tfm = sox.Transformer()
            # set output format
            tfm.set_output_format(rate=16000,bits=16,channels=1)
            # create the output file
            tfm.build('audio.flac', 'audio.raw')

            file_name = os.path.join(
                os.path.dirname(__file__),
                'audio.raw')

            with io.open(file_name, 'rb') as audio_file:
                content = audio_file.read()
                audio = types.RecognitionAudio(content=content)

            config = types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code='en-US')

            # Detects speech in the audio file
            response = client.recognize(config, audio)
            rsp = ''
            for result in response.results:
                rsp += 'Transcript: {}'.format(result.alternatives[0].transcript)
            # [END speech_quickstart]
            return jsonify({"output" : rsp})


if __name__ == '__main__':
    app.run(debug=True)
