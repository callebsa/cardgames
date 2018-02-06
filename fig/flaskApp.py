from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/vandtia/img/<path:filename>')
def get_img(filename):
  print filename
  w= int(request.args['w'])
  h= int(request.args['h'])
  print "h: " + str(h)
  try:
    im = Image.open(filename)
    print "x"
    im.thumbnail((w, h), Image.ANTIALIAS)
    print "y"
    io = StringIO.StringIO()
    print "Z"
    im.save(io, format='JPEG')
    print "willsend"
    return Response(io.getvalue(), mimetype='image/jpeg')
  except:
    return "File :" + filename + "cannot be find";

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
