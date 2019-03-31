#Log Alnalysis
Part of Udacity nanodegree.use virual machine,python and postgresql

## 1. how to start
### 1. Setup: Configure VM & Database

**Step 1:** Download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org). 

**Step 2:** Download the VM configuration from the [downloads folder](downloads/) or clone from this [github repo](https://github.com/udacity/fullstack-nanodegree-vm). 

**Step 3:**  Download the database from the [link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

Then, copy the database dump `newsdata.sql` to the `vagrant/`.

**Step 4:**  Download (`loganalysis.py`) from the current folder. Then, copy them to the `vagrant/`.

**Step 5:** Open the terminal. Then, run the following commands:

```
# Install & Configure VM
cd /path/to/vagrant
vagrant up

# Log into machine
vagrant ssh

# Populate database using dump to shared folder 
cd /vagrant 
psql -d news -f newsdata.sql
```

### 2. Run

Open the terminal.

```
# Launch & Login to machine
cd /path/to/vagrant
vagrant up
vagrant ssh

cd /vagrant 

# Run
python loganalysis.py
```

## Rubric

|SECTION|CRITERIA|
|---|---|
| Functionality | this code will answer the three questions in log analysis project|
| Database | the database not change|
| Language | The code written in Python 2.|
| Well-formatted | out put will be in plain text.|
| quality | No errors |
| SQL code | the code use one query foreach question|
| pep 8 | the code use pep 8 style code|

## Output

Q1. What are the most popular three articles of all time?

Candidate is jerk, alleges rival -- 338647 views
Bears love berries, alleges bear -- 253801 views
Bad things gone, say good people -- 170098 views

Q2. Who are the most popular article authors of all time?

Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views

Q3. On which days did more than 1% of requests lead to errors?

July 17, 2016 -- 2.3% errors