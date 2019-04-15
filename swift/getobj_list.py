from keystoneauth1 import session
from keystoneauth1.identity import v3
from swiftclient import client

auth = v3.Password(auth_url='http://192.168.1.26:35357/v3/',username='system',password='123456',project_name='da',user_domain_id='default',project_domain_id='default')

sess = session.Session(auth=auth)

swift_conn = client.Connection(session=sess)

resp_headers, object = swift_conn.get_container("container_000")


print("\nobjetc=======================================================================")
for o  in object:
#	print("%s" % o)
	print("%s\t%s\t%s" % (o['last_modified'], o['bytes'], o['name']))
#print("\nconainters=====================================================================")
#for c in containers:
#	print("%s" % c)
 



#print(object)
