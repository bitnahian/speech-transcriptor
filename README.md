# speech-transcriptor 
Speech to Transcript script using Google Speech API. The following description is copied from the python-doc module for the Google Speech API. 

Authentication
++++++++++++++

This sample requires you to have authentication setup. Refer to the
`Authentication Getting Started Guide`_ for instructions on setting up
credentials for applications.

.. _Authentication Getting Started Guide:
    https://cloud.google.com/docs/authentication/getting-started

Install Dependencies
++++++++++++++++++++

#. Install `pip`_ and `virtualenv`_ if you do not already have them. You may want to refer to the `Python Development Environment Setup Guide`_ for Google Cloud Platform for instructions.

 .. _Python Development Environment Setup Guide:
     https://cloud.google.com/python/setup

#. Create a virtualenv. Samples are compatible with Python 2.7 and 3.4+.

    .. code-block:: bash

        $ virtualenv env
        $ source env/bin/activate

#. Install the dependencies needed to run the samples.

    .. code-block:: bash

        $ pip install -r requirements.txt

.. _pip: https://pip.pypa.io/
.. _virtualenv: https://virtualenv.pypa.io/

#. Install `ffmpeg`_ and `sox`_ dependencies for formatting the blob audios received from the JavaScript. The following snippet is compatible with Ubuntu 16.04 LTS for installing the dependencies. 

    .. code-block:: bash

        $ sudo apt-get install ffmpeg
        $ sudo apt-get install sox

.. _ffmpeg: https://ffmpeg.org/ffmpeg.html/
.. _sox: http://sox.sourceforge.net/

This is a good [conversation](https://groups.google.com/forum/#!topic/cloud-speech-discuss/tbQHoaTTNH8) to understand some of the audio requirements for the Google Speech API. 

#. Quite naturally, I also used python wrappers for both ffmpeg and sox called `ffmpy`_ and `pysox`_ respectively. Both are listed as requirements in the requirements.txt file.

.. _ffmpy: https://pypi.python.org/pypi/ffmpy
.. _pysox: https://github.com/rabitt/pysox

#. Web resources and JS scripts to record sound blob was shamelessly taken from the [mdn/web-dictaphone](https://github.com/mdn/web-dictaphone).
