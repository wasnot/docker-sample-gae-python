FROM wasnot/chainer-appengine
#RUN virtualenv /env -p python

# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
#ENV VIRTUAL_ENV /env
#ENV PATH /env/bin:$PATH
ADD . /app/
CMD python app.py
