# EC2 Remediation

Project is to find the untagged EC2 instances from the account.
It will create three lists,
1. tagged [if the instance is tagged with required tags]
2. untagged [If the instance is not tagged at all]
3. invalid [If the instance is tagged but does not contain the required tags]

required list of tags: ['BillingIdentifier','Environment','ITSO','FSO']

## Pre-requisites:
- Boto3
- AWS account
- Python
