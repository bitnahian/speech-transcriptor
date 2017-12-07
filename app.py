from flask import Flask, render_template, request, jsonify
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
            # [START speech_quickstart]
            # Set environment variable for GOOGLE_APPLICATION_CREDENTIALS
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{{ url_for('static',filename='credentials.json') }}"

            # Instantiates a client
            # [START migration_client]
            client = speech.SpeechClient()
            # [END migration_client]

            content = file.read()
            audio = types.RecognitionAudio(content=content)

            # Convert to base64
            def encode_audio(audio):
                audio_content = audio.read()
                return base64.b64encode(audio_content)

            audio = encode_audio(audio)

            config = types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code='en-US')

            # Detects speech in the audio file
            response = client.recognize(config, audio)

            for result in response.results:
                print('Transcript: {}'.format(result.alternatives[0].transcript))
            # [END speech_quickstart]
            return jsonify({"success" : "Works."})


if __name__ == '__main__':
    app.run(debug=True)
