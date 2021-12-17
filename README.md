# DjangoProjects REST API

DjangoProjects restapi code.




vagrant ssh to start vagrant

#to create a venv in desired location

#p.s. we create the venv inside vagrant which is our development server
python -m venv ~/env    
#env is name of env
#to activate the venv run source ~/env/bin/activate
# to deactivate the venv run deactivate


# list the reqms in the reqms.txt then run (in vagrant) : pip install -r reqms.txt
# automatically fetches the requirements(r*) listed




"""  running virtual server after restart"""
vagrant ssh
cd /vagrant
to log into ubuntubionic/vagrant
source ~/env/bin/activate


found the error in the last project i.e devsearch learn that tags had an extra s like tagss
its because the django automatically defines the classes as plural and if you name the model as tags then when django creates databases it pluralizes it like tagss


APIView:  basic
allows to define function that matches standard http methods:
get
post
 put
  patch
   delete
VIEWSet:
provide control over logic
calling other apis and working with local files


wen to use:
personal preference
validating and returning result in same call
need full control over logic
processing files and rendering sync response
call other apis with same request::
list
create
retrieve
update
partial_update
destroy

perfect for standard database
fastest

preferneces when
api for crud
quick and simple apis
custom logic
standard database strcture
