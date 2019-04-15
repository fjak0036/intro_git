from keystoneauth1 import session
from keystoneauth1.identity import v3
from swiftclient import client

auth = v3.Password(auth_url='http://192.168.1.26:35357/v3/',username='system',password='123456',project_name='da',user_domain_id='default',project_domain_id='default')

sess = session.Session(auth=auth)

swift_conn = client.Connection(session=sess)

resp_headers, containers = swift_conn.get_account()
print(containers)


container = 'container_100'
with open('test.txt', 'r') as local:
    swift_conn.put_object(
        container=container,
        obj='test_object.txt',
        contents=local,
        content_type='text/plain'
    )
