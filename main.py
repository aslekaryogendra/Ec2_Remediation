# Required imports
import csv
import os 
import boto3

# code starts from here

# Check if the tags of the instance are defined as per requirement list
def validate_tags(lst_tags):
    lst_valid=['BillingIdentifier','Environment','ITSO','FSO']
    check= all(i in lst_valid for i in lst_tags)
    if check is True:
        return 'Tags are Defined'
    else:
        return 'Tags are not Defined' 

# Get the required details of an instance to include in report
def getDetails(instance):
    i_tags=instance.tags
    lst_tags=[tag['Key'] for tag in i_tags]

    final_op=[]
    final_op.append(instance.id)
    final_op.append(instance.instance_type)
    final_op.append(instance.state.get('Name'))
    final_op.append(validate_tags(lst_tags))
    return final_op

# All regions
lst_region=['ap-south-1', 'eu-north-1', 'eu-west-3', 'eu-west-2', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'ap-northeast-1', 'ca-central-1', 'sa-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']

print("Checking tags : ['BillingIdentifier','Environment','ITSO','FSO']")
ans=input("Do you want to export the data in csv? (y/n): ")
if ans == 'y' or ans=='Y':
    f=open('report.csv','w+',newline='')
    writer= csv.writer(f)
    writer.writerow(['Instance_ID','Instance_Type','Instance_State','Instance_Tags','Instance_Region'])
    for each_region in lst_region:
        ec2=boto3.resource('ec2',region_name=each_region)
        instances=ec2.instances.filter()
        for instance in instances:
            # print(instance.id,instance.instance_type, instance.state.get('Name'),instance.tags, each_region)
            lst_item=[item for item in getDetails(instance)]
            lst_item.append(each_region)
            writer.writerow(lst_item)
        
    f.close()
    print(f"Get your file from: %s"%(os.getcwd()))
else:
    print(['Instance_ID','Instance_Type','Instance_State','Instance_Tags','Instance_Region'])
    for each_region in lst_region:
        ec2=boto3.resource('ec2',region_name=each_region)
        instances=ec2.instances.filter()
        for instance in instances:
            #print(getDetails(instance)[0],getDetails(instance)[1],getDetails(instance)[2],getDetails(instance)[3])
            lst_item=[item for item in getDetails(instance)]
            lst_item.append(each_region)
            print(lst_item)