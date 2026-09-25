# Launch an Ubuntu EC2 Instance

Log in to the AWS Management Console and navigate to the EC2 Dashboard

Click the Launch instances button

Name your instance under the Name and tags section (e.g., Ubuntu-Web-Server)

*Choose an Operating System*: In the Application and OS Images (Amazon Machine Image) section, select Ubuntu. Ensure you pick a version marked as Free tier eligible (Such as Ubuntu 24.04 LTS or 22.04 LTS)

*Select Instance Type*: Choose t2.micro or t3.micro (depending on your region) to stay within the AWS Free Tier

*Configure Key Pair*: 
Under Key pair (login), click Create new key pair
Give it a name, select RSA as the type, and choose .pem format
Click Create key pair and save the downloaded file securely. Note: You cannot download this file again.

*Network Settings (Firewall)*:
Ensure the *Allow SSH traffic from* checkbox is checked.
For production, restrict this from Anywhere (0.0.0.0/0) to My IP to ensure only you can access it.

Click *Launch instances* at the bottom of the summary panel

# Get your Instance Details

Go back to the Instances view in your EC2 Dashboard

Wait until your instance state shifts to Running

Click on your instance and locate the Public IPv4 address or Public IPv4 DNS in the details panel below. Copy it

# SSH into the Instance

Open your local terminal and follow these commands:

1. Navigate to the folder where your .pem key file is saved:

cd ~/Downloads

2. Set key permissions: Your private key must not be publicly viewable, or SSH will reject it. Run:

chmod 400 your-key-name.pem

3. Connect via SSH: Run the command below, substituting your key name and your instance's copied Public IP address:

ssh -i "your-key-name.pem" ubuntu@your-instance-public-ip

4. Accept the Fingerprint: The first time you connect, your terminal will ask if you want to continue connecting. Type "yes" and press Enter


# AWS CLI Installation:

To install AWS CLI first you need to install unzip on Ubuntu, open your terminal and update your package lists, then run the installation command

# Run the following commands:

sudo apt update
sudo apt install unzip

# Then run this command:

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# AWS Configuration:

# Run the setup command in your terminal to configure AWS

aws configure

# Enter Access Key: Paste your unique alphanumeric AWS identifier

AWS Access Key ID [None]: ABCD1234

# Enter Secret Key: Input your hidden security key credentials

AWS Secret Access Key [None]: wkskdfer

# Set the default region: Specify your closest cloud data center identifier

Default region name [None]: us-east-1

# Set output format: Choose how your terminal displays server data responses

Default output format [None]: json


