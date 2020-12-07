from flask import Flask

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s !</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> 
    <title> Image streaming from AWS S3 </title> 
    </head>\n<body>'''
instructions = '''
    <br>
    <p><h2>Introduction</h2> This is a web application, <b>image streaming from AWS S3</b>, which can show the image from my AWS S3 !</p>
    <br>
    <p> My Raspberry pi takes the image with 1280*720 resolution, and send it to S3 database every 10 minutes (If Rpi opens ~). </p>
    <p> Therefore, you can refresh the website every 10 minutes to see the image difference. </p>
    <br>
    <p><img src="http://d323w7ypbkc7zw.cloudfront.net/imgStream.png" width = "50%" alt="S3 Image" name = imgShow>'''

home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
