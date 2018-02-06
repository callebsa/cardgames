from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/vandtia/img/<path:filename>')
def get_img(filename):
	    try:
      		w = int(request.args['w'])
        	h = int(request.args['h'])
	    except (KeyError, ValueError):
    	    return send_from_directory('.', filename)
 		try:
        	im = Image.open(filename)
        	#im.thumbnail((w, h), Image.ANTIALIAS)
       		io = StringIO.StringIO()
        	im.save(io, format='JPEG')
        return Response(io.getvalue(), mimetype='image/jpeg')
    except IOError:
        return "File :" + filename + "cannot be find";
        
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
