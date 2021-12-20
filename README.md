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


so here is what happens when deploying
at first cat ~/id_rsa.pub sth like this 
add this ssh to the azure resources

create a ubuntu vm in azure or aws
use the sam ssh key (its set as public ssh and you dont need to generate it like before)
now based on the ssh key you create the vm 
remember the name of the vm :
azureuser for this restApi project 

configure the deploy files 
run the command in the projects root (not in the virtual server vagrant)
change the debug true to the recent command
run chmod +x deploy/*.sh  
which runs the shell command and configurations and access controls or whatsoever
now to connect to the azure vm run the command :
ssh azureuser@publicIp 
and youre done

now run the following command 
where the link is the raw data view of setup.sh in your github/restApi/deploy/setup.sh 

curl -sL https://raw.githubusercontent.com/sunilthapa43/restApi/master/deploy/setup.sh | sudo bash -