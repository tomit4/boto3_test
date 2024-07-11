# AWS S3 Python Boto Basics

This repository contains very basic source code and documentation on how to utilize the AWS S3 SDK via Amazon's Python boto3 package.

**TODO:**

- [ ] Research on how to secure the IAM User on AWS so they do not have access
      to anything other than reading/writing/deleting the specific S3 bucket.
- [ ] Integrate creation, adding to, and deleting of <em>folders</em> within the
      S3 Bucket
- [ ] Figure out how to error out of if a bucket is not found.
- [ ] Write Extensive Documentation on Getting Started With Amazon S3. This
      includes signing up for AWS, setting up MFA for root user, creating a new IAM
      user, creating MFA for the IAM user, creating a group for the IAM user, linking
      to the getting started tutorial for the S3 buckets, generating and getting csv
      file of new IAM user's credentials (i.e. the AWS_ACCESS_KEY_ID and
      AWS_SECRET_ACCESS_KEY for use with the Amazon S3 API via boto3).

**RESOURCES:**

- [AWS S3 Getting Started](https://aws.amazon.com/s3/getting-started/)
- [Quick Start Youtube Tutorial](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Boto's Official Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Stack Overflow On Creating S3 Folders](https://stackoverflow.com/questions/1939743/amazon-s3-boto-how-to-create-a-folder)

**QUICKNOTES:**

```sh
python3 -m venv env
```

Activate the the virtual environment:

```sh
source env/bin/activate
```

Install local environment requirements:

```sh
pip install -r requirements.txt
```

Copy env-sample to .env:

```sh
cp env-sample .env
```
