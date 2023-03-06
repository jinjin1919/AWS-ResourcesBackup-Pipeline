{\normalsize }
The objective of this project is to assist users in minimizing the time and effort associated with the creation of daily, automated, and aggregated backup and cost reports based on tags, simplified observability of data protection activities to provide enriched daily data protection reporting to customers, and enable users to dive deeper into the usage patterns and cost trends as well as backup data protection activities. 

\emph{Goal of Project:}

Create 2-10 EC2 instances, 2-10 RDS databases and 2-10 S3 buckets.

Populate the RDS database and S3 buckets with some content.

Tag each resource with one of three environment tags ("dev", "staging", "prod") and another department tag from ("sales", "marketing", "HR").

Create backup plans with different backup schedules for each tag, e.g. "dev" backs up once every 6 hours, "staging" every 3 hours, "prod" every hour.

Make a Quicksight dashboard that allows a user to categorize backups from different tag groups as well as resource type (e.g. S3, RDS or EC2)