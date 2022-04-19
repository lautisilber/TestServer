# TestServer

Simple server that echoes whatever it is sent. Can be used to test http clients. Created with iot applications in mind.

This script uses the package ***Flask***. It can be installed via the command:

<pre><code>pip install Flask</code></pre>

Then you can run the server with:

<pre><code>python3 app.py</code></pre>


If you wanted to specify a host and/or port you can do so by adding the arguments <code>--host="\<your host\>"</code> and <code>--port="\<your port\>"</code>.
For example: <code>python app.py --host=192.168.4.1 --port=1234</code>
