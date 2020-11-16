import os
import sys
import webbrowser
flag = 0

def start_nn():		#Start Name Node
	print("Starting...")
	os.system("hadoop-daemon.sh start namenode")
	print("Name Node services started.")
	



def conf_nn():		#configures Name Node
	
	
	print("\t\t\tCreating ur system as Name Node.....")
	dr_name = input("Enter name of directory to deploy file system : ")
	os.system("mkdir /{}".format(dr_name))
	ip = input("Enter IP address of Name Node(For public access enter 0.0.0.0) : ")
	
	
	#os.system("cd /etc/hadoop")
	#os.system("vim hdfs-site.xml")
	f = open("/etc/hadoop/hdfs-site.xml","w")
	f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{}</value>
</property>

</configuration>

""".format(dr_name))
	f.close()
	
	
	f = open("/etc/hadoop/core-site.xml","w")
	f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>

</configuration>
""".format(ip))
	f.close()
	os.system("""hadoop namenode -format
systemctl stop firewalld""")

def conf_dn():
	
	print("Configuring ur system as Data Node..")
	dr_name = input("Enter name of directory to contribute : ")
	os.system("mkdir /{}".format(dr_name))
	ip = input("Enter IP address of Name Node : ")
	
	
	#os.system("cd /etc/hadoop")
	#os.system("vim hdfs-site.xml")
	f = open("/etc/hadoop/hdfs-site.xml","w")
	f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{}</value>
</property>

</configuration>

""".format(dr_name))
	f.close()
	
	
	f = open("/etc/hadoop/core-site.xml","w")
	f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>

</configuration>
""".format(ip))
	f.close()

def chk():
	os.system("hadoop dfsadmin -report")

def start_dn():
	print("Starting...")
	os.system("hadoop-daemon.sh start datanode")
	print("Data Node services started.")

def conf_client():
	print("Configuring your system as Client.")
	
	ip = input("Enter IP address of Name Node : ")
	
		
	f = open("/etc/hadoop/core-site.xml","w")
	f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.data</name>
<value>hdfs://{}:9001</value>
</property>

</configuration>
""".format(ip))
	f.close()
	os.system("clear")
	print("Client services started")
	
	

def upblk(a, b):
	
	os.system("hadoop fs -Ddfs.block.size={} -put {} /".format(a, b))

def fsls():
	
	os.system("hadoop fs -ls /")

def delf(f):
	os.system("hadoop fs -rm  /{}".format(f))
def readf(f):
	os.system("hadoop fs -cat /{}".format(f))
def upf(f):
	os.system("hadoop fs -put {}  /")

	
		
	




	


	
def hadoop():	
	while True:
		os.system("tput setaf 5")
		print("\t\tWelcome to Hadoop Distributed Storage technology\n")
		print("\t___________________________________________________________")
		os.system("tput setaf 3")

		p = int(input("""\t\t\tPRESS 1 - To configure ur system
		\tPRESS 2 to Start Services
		\tPRESS 3 to Access Filesystem
		\tPRESS 4 to check which service is running
		\tPRESS 5 to check status
		\tPRESS 6 to open hadoop WebUI
		\tPRESS 0 to EXIT\nENTER here : """))
		os.system("tput setaf 7")

		if p==1:
			os.system("clear")
			a = int(input("""\t\t\tPRESS 1 - To configure your system as Namenode
		\tPress 2 - To configure your system as Datanode
		\tPress 3 - To configure your system as client\nEnter here : """))
			if a==1:
				conf_nn()
			elif a==2:
				conf_dn()
			elif a==3:
				conf_client()
				
		elif p==2:
			os.system("clear")
			b = int(input("""\t\t\tPRESS 1 - To Start Namenode services
		\tPRESS 2 - To Start Datanode services\nEnter here : """))
			if b==1:
				start_nn()
			elif b==2:
				start_dn()

		elif p==3:
			while True:
				os.system("clear")
				c = int(input("""\t\t\t\tPRESS 1 - To List the contents of File System
			\t\tPRESS 2 - To upload a file
			\t\tPRESS 3 - To read a file
			\t\tPRESS 4 - To delete file
			\nEnter here : """))
				if c==1:
					fsls()
				elif c==2:
					filen = input("Enter name of file with full path : ")
					blksz = int(input("Enter block size in bytes (by Default 64 MB) for default value Press Enter 0 : "))
					if blksz!=0:
						upblk(blksz, filen)
					else:
						upf(filen)
				elif c==3:
					filen = input("Enter name of file : ")
					readf(filen)
				elif c==4:
					filen = input("Enter name of file : ")
					delf(filen)
				flag = input("Press any key to continue\nPress 0 for previous menu\nEnter here : .")
				if flag=='0':
					break
				
		elif p==4:
			os.system("clear")
			os.system("jps")
		elif p==5:
			os.system("clear")
			chk()
		elif p==6:
			os.system("clear")
			sys.stdout.write("Enter IP address of Name Node : ")
			sys.stdout.flush()
			ip = sys.stdin.readline()
			webbrowser.open('http://{}:50070'.format(ip), new=2)
		i=input("Press 0 to Exit\nPress 1 to again run the menu\nEnter here : ")
		if i=='0':
			break
		os.system("clear")


def aws():
	def aws_instance():
		print('\t\t\tCreating a Key Pair...')

		key_name = input('\t\t\tEnter your key pair name that you want to give = ') 
		os.system("aws ec2 create-key-pair --key-name={}".format(key_name))

		
		

		print('\n\t\t\tCreating a Sec Group...')
		sec_name = input('\t\t\tEnter your security group name that you want to give = ') 
		os.system('aws ec2 create-security-group --description {} --group-name {}'.format(key_name, sec_name))
		
		

		auth = input('\n\t\t\tTo provide autorized security enter your GroupID here : ')
		os.system('aws ec2 authorize-security-group-ingress --group-id {} --protocol tcp --port 22 --cidr 0.0.0.0/0'.format(auth))


		print('\n\t\t\tCreaing an Instance On AWS Cloud...')
		img_id = input('\t\t\t provide the image ID which OS you want to launch : ')
		instance_type = input('\t\t\tEnter which type of OS you want to launch :')
		os.system('aws ec2 run-instances --image-id {} --instance-type {} --security-group-ids {} --key-name {}'.format(img_id, instance_type, auth, key_name))
		print('\n\t\t\tYour Instance is created you can verify it from Management Console')

	def start_instance():
		start_id = input('Enter Instance ID that you want to start : ')
		os.system('aws ec2 start-instances --instance-ids {}'.format(start_id))
		print('Your Instance started successfully.')

	def stop_instance():
		stop_id = input('Enter Instance ID that you want to stop : ')
		os.system('aws ec2 stop-instances --instance-ids {}'.format(stop_id))
		print('Your Instance stopped successfully.')
	    
	def cloudfront_service():
		print("\t\t\t\tFor giving origin in cloud front we have to use S3 bucket ....")
		choice_bucket = input("\t\t\t\tDo you want to create bucket or you want to use existing bucket..(type-create bucket/existing bucket)?")
		if(("create bucket" in choice_bucket)):
			bucket_name = input("\t\tEnter bucket name which you want to use for cloud front service:")
			region_name = input("\t\t\t\tEnter region name :")
			os.system("aws s3 mb s3://{} --region {}".format(bucket_name,region_name))
			print("\t\t\t\tbucket created....")
			print()
			print("\t\t\t\tUpload obect inside bucket...")
			object_name = input("\t\t\t\tEnter object which you want to upload:")
			print("Which type of permission you want to give to object..")
			print("\t\t\t\t(private)(public-read)(public-read-write)(authenticated-read)(aws-exec-read)(bucket-owner-read)(bucket-owner-full-control)(log-delivery-write)")
			object_permission = input("\t\t\t\tEnter permission for object:")
			os.system("aws s3 cp {} s3://{} --acl {}".format(object_name,bucket_name,object_permission))
			print()
			print("\t\t\t\tObject is uploaded successfully...")
			print("\t\t\t\tCreating cloud front distribution...")
			os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(bucket_name,object_name))
		if(("existing bucket" in choice_bucket)):
			bucket_name=input("\t\t\t\tEnter S3 bucket name:")
			object_name=input("\t\t\t\tEnter object name:")
			os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(bucket_name,object_name))
		
	def s3_service():
		bucket_name = input("\t\t\t\tEnter bucket name:")
		region_name = input("\t\t\t\tEnter region name :")
		os.system("aws s3 mb s3://{} --region {}".format(bucket_name,region_name))
		print("\t\t\t\tbucket created....")
		print()
		choice_upload = input("\t\t\t\tDo you want to upload obect inside bucket(Yes/No)...")
		if(("Yes" in choice_upload) or ("YES" in choice_upload) or ("yes" in choice_upload)):
			object_name = input("\t\t\t\tEnter object-path which you want to upload:")
			print("What type of permission you want to give to object..")
			print("\t\t\t\t(private)(public-read)(public-read-write)(authenticated-read)(aws-exec-read)(bucket-owner-read)(bucket-owner-full-control)(log-delivery-write)")
			object_permission = input("\t\t\t\tEnter permission for object:")
			os.system("aws s3 cp {} s3://{} --acl {}".format(object_name,bucket_name,object_permission))
			print()
			print("\t\t\t\tObject is uploaded successfully...")
		else:
			print("okay")
	#creating volume 

	def EBS_volume():
		def create_volume():
			print("To create volume ----------")
			volume_type=input("enter volume type :")
			volume_size=input("enter volume size :")
			avail_zone=input("enter EBS availability zone : ")
			print("\t\t\t\t--------------creating volume-------------------\n")
			os.system("aws ec2 create-volume --volume-type {}  --size {} --availability-zone {}".format(volume_type,volume_size,avail_zone)) 

	    #Attach volume
		def Attach_volume():
			print("To Attach volume ----------")
			instance_id=input("enter instance id to attach volume:")
			vol_id= input("enter volume id to attach :")
			device=input("enter device to attach as :") #ex:/dev/xvdf 
			print("\t\t\t\t--------------Attaching volume-------------------\n")
			os.system("aws ec2  attach-volume  --instance-id {}  --volume-id {} --device {} ".format(instance_id,vol_id,device))

	    #modify volume
		def modify_volume():
			print("To modify  volume ----------")
			volume_id=input("enter volume id to modify :")
			size=input("enter volume size to modify :")
			print("\t\t\t\t--------------Modifying  volume-------------------\n")
			os.system("aws ec2 modify-volume --volume-id {} --size {} ".format(volume_id,size))
			
	    #Automation code
		print("\t\t\t\t------------------EBS Automation--------------------\n")

		while(1):
			print("\t\t\t\t 1.Create volume \n \t\t\t\t 2.Attach volume \n \t\t\t\t 3.Modify volume \n \t\t\t\t 4.Detach volume \n \t\t\t\t 5.exit \n")
			choice=int(input("choose your Requirement :"))
			if(choice==1):
			    create_volume()
			if(choice==2):
			    Attach_volume()
			if(choice==3):
			    modify_volume()
			if(choice==4):
			    break
		    
	def IAM_user():
	    #creating User
		def create_user():
			print("\t\t\t\t-------------To create user--------------\n")
			name=input("enter user_name to create IAM User :")
			os.system("aws iam create-user --user-name {} ".format(name))

	    #creating group
		def create_group():
			print("\t\t\t\t-------------To create group--------------\n")
			group_name=input("enter group name to create IAM group :")
			os.system("aws iam create-group  --group-name {} ".format(group_name))
		
		
	    #get specific group details
		def get_group():
			group_name=input("enter group name to get details :")
			os.system("aws iam get-group --group-name {}".format(group_name))


	    #add user to group
		def  user_add_group():
			print("\t\t\t\t-------------To add user in group--------------\n")
			user_name=input("enter the user name to add in group :")
			group_name=input("enter the group name :")
			os.system(" aws iam add-user-to-group --user-name {} --group-name  {} ".format(user_name,group_name))
			


	    #create access key of user
		def create_access_key():
			print("\t\t\t\t-------------To create access key--------------\n")
			user=input("enter  user_name to create access key :")
			os.system("aws iam create-access-key --user-name {} ".format(user))

	    #list-users
		def list_users():
			os.system("aws iam list-users")
		
	    #list-groups
		def list_groups():
			os.system("aws iam list-groups")

	    #delete user
		def delete_user():
			print("\t\t\t\t-------------To delete user--------------\n")
			user_name=input("enter user name which you would like to delete :")
			os.system("aws iam delete-user --user-name {} ".format(user_name))
		
	    #delete group
		def delete_group():
			group_name=input("enter group name which you would like to delete :")
			os.system("aws iam delete-group --group-name {}".format(group_name))


	    #Automation code 

		while(1):
			print("\t\t\t\t ------------------IAM Creation-----------------\n")
			print("\t\t 1.create-user \n \t\t 2.create-group \n \t\t 3.get-group details \n \t\t 4.add-user-to-group \n \t\t 5.add-group-policy \n \t\t 6.group-details \n \t\t 7.create access key \n \t\t\t\t 8.list-users \n \t\t\t\t 9.list-grops \n  \t\t 10.delete-user \n \t\t 11.delete group \n \t\t 12.remove-user from group \n \t\t 13.delete user access key\n \t\t 14.exit \n")	
			choice=int(input("enter your requirement : "))
			if(choice==1):
			    create_user()
			if(choice==2):
			    create_group()
			if(choice==3):
			    get_group()
			if(choice==4):
			    user_add_group()
			if(choice==5):
			    create_access_key()
			if(choice==6):
			    list_users()
			if(choice==7): 
			    list_groups()
			if(choice==8):
			    delete_user()
			if(choice==9):
			    delete_group()
			if(choice==10):
			    del_group_user()
			if(choice==14):
			    break

			print("\t\t\t\tConfigure AWS to enter into AWS\n")
			os.system("aws configure")
	while(1):
		print('''\t\t\tSelect your requirement
			\t\t\t\t1: Create Aws instance.
			\t\t\t\t2: Start AWS Instance.
			\t\t\t\t3: Stop AWS Instance.
			\t\t\t\t4: Create a S3 bucket.
			\t\t\t\t5: Create a CloudFront service.
			\t\t\t\t6: EBS Volume
			\t\t\t\t7: IAM User
			\t\t\t\t8: exit
				''')
		select = input("\t\t\tselect from menu :")
		select = int(select)

		if(select==1):
			aws_instance()
		elif(select == 2):
			start_instance()
		elif(select == 3):
			stop_instance()
		elif(select==4):
			s3_service()
		elif(select==5):
			cloudfront_service()
		elif(select==6):
			EBS_volume()
		elif(select==7):
			IAM_user()  
		elif(select==8):
			exit() 	
		else:
			print("\n\t\tinvalid option!!!")
		print("\t\t\t\t________________________________________________________________________________________________________________________\n")


def docker():
	while True:
		print("""\n\n\t\t\twelcome to docker
		\t\t\t..................
	 	press 1: for container launch
	 	press 2: to see running instances
	 	press 3: to see available images
	 	press 4: to see all available containers
	 	press 5: to start container



		press 0: Previous Menu """)

		choice = int(input("Enter your choice"))
		
		if choice == 1:
			print("""select which image you want to use:
			press 1: ubuntu
			press 2: debian 
			press 3: centos""")
		  

			choice1 = int(input("enter your choice : "))
			if choice1 == 1:
				os.system("docker run -dit ubuntu:latest")
			elif choice1 == 2:
				os.system("docker run -dit debian:latest")
			elif choice1 == 3:
				os.system("docker run -dit centos:latest")
				
					
		elif choice == 2:
			os.system("docker ps")
		elif choice == 3:
			os.system("docker images")
		elif choice == 4:
			os.system("docker ps -a")
		elif choice == 5:
			os.system("docker ps")
			print("Enter os name:")
			name  =  input()
			os.system("docker attach "+name)
		else:
			break
		input("Press any key to run again\n")
				

while True:
	print("\t\t\t...Welcome to our Automation Program...")
	i = int(input("""\tPress 1 : For Hadoop
	Press 2 : For AWS
	Press 3 : For Docker
	Press 0 : To Exit\nEnter here : """))
	if i==1:
		hadoop()
	elif i==2:
		aws()
	elif i==3:
		docker()
	elif i==0:
		exit()
	else:
		continue
