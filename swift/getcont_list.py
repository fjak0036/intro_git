from keystoneauth1 import session
from keystoneauth1.identity import v3
from swiftclient import client

auth = v3.Password(auth_url='http://192.168.1.26:35357/v3/',username='system',password='123456',project_name='da',user_domain_id='default',project_domain_id='default')

sess = session.Session(auth=auth)

swift_conn = client.Connection(session=sess)

try:
    resp_headers, containers = swift_conn.get_account()

except session.exceptions.Unauthorized:
    print ("The request you have made requires authentication.")

except client.ClientException:
    print ("Account GET failed")


print("\nHeaders=======================================================================")
for(k,v) in resp_headers.items():
	print("%s:%s" %(k,v))

print("\nconainters=====================================================================")
for c in containers:
	print("%s" % c)
 



#print(containers)
