#When versioning is enabled, a simple DELETE cannot permanently delete an object. Instead, Amazon S3
#inserts a delete marker in the bucket, and that marker becomes the current version of the object with a new ID.
#To permanently delete versioned objects, you must use DELETE Object versionId .




#Calling Library
import boto3


#Filtering out
a_string="qwert"
Bucket_list=[]
Bucket_del_list=[]

#Defining client and resources
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

#Creating a bucket list
for bucket in s3_resource.buckets.all():
    Bucket_list.append(bucket.name)
#Filtering bucket to delete
for i in Bucket_list:
    if (a_string in i):
        Bucket_del_list.append(i)
if len(Bucket_del_list) == 0:
    print("No Bucket for Deletion" )


for bucket_name in Bucket_del_list:
    bucket = s3_resource.Bucket( bucket_name )
    try:
        print("Deleting Bucket :"+str(bucket_name))
        resp1 = bucket.object_versions.delete()
        resp2 = s3_client.delete_bucket( Bucket=bucket_name )
        if resp1:
            print("Deleting Versions of object in Bucket")
        if resp2:
            print("Deleting the Bucket",bucket_name)
    except Exception as e:
        print("Error :" + str(e))
