[//]: # (This is also a comment.)

### Purpose
Here are basic Linux command line installation instructions for installing [Fuseki v2](https://jena.apache.org/documentation/fuseki2/), the system that provides a REST-style SPARQL 1.1 HTTP API for the [Jena](https://jena.apache.org/) triplestore, on Ubuntu 14.04+.

### All steps
* Server prerequisites
    * Add the OpenJDK repo
    * Install Java 8
* Getting Fuseki
    * Download Fuseki with Jena, unzip it into /opt/fuseki
        * NOTE: update the Fuseki version number in file name to latest
        * assume user 'ubuntu'
* Configure Fuseki    
    * Make a Fuseki config file, place it in 'run' dir
    * Make run scripts executable
    * Create log file
    * Create shortcut start and stop scripts that use the config & log file
    * Set enviro vars
* Run it
    * Start Fuseki
* Extra access 
    * Allow non-localhost use of Fuseki admin UI

### Step by step, with code
#### Server prerequisites
* Add the OpenJDK repo
* Install Java 8 

```{.sh}
sudo add-apt-repository ppa:openjdk-r/ppa
sudo aptitude update
sudo aptitude install -y openjdk-8-jdk
```

#### Getting Fuseki
* Download Fuseki with Jena, unzip it into /opt/fuseki  
    * NOTE: update the Fuseki version number in file name to latest  
    * assume user 'ubuntu'
    
```{.sh}
wget http://apache.mirror.serversaustralia.com.au/jena/binaries/apache-jena-fuseki-2.5.0.tar.gz -O fuseki.tar.gz  
sudo mkdir -p /opt/fuseki  
sudo tar -C /opt/fuseki -xzf fuseki.tar.gz --strip 1  
rm fuseki.tar.gz  
sudo chown -R ubuntu:ubuntu /opt/fuseki  
```

#### Configure Fuseki
* Make a Fuseki config file, place it in 'run' dir  

```{.sql}
@prefix fuseki:  <http://jena.apache.org/fuseki#> .
@prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
@prefix tdb:     <http://jena.hpl.hp.com/2008/tdb#> .
@prefix ja:      <http://jena.hpl.hp.com/2005/11/Assembler#> .
@prefix :        <http://nick.com> .

[] a fuseki:Server ;
	fuseki:services [
	 	a fuseki:Service ;
		fuseki:name              "tdb" ;      # http://host:port/tdb
		fuseki:serviceQuery      "query" ;     # SPARQL query service
		fuseki:serviceUpdate     "update" ;	   # SPARQL query service
		fuseki:dataset           :dataset ;
	]
.

:dataset
	a tdb:DatasetTDB ;
	tdb:location "{DATASET_FOLDER_LOCATION}" ;  # no trailing slash
	tdb:unionDefaultGraph true ;
	ja:defaultGraph :model;
.

:model
	a ja:InfModel;
	ja:reasoner [
		ja:reasonerURL <http://jena.hpl.hp.com/2003/OWLFBRuleReasoner>
	];
.
```

```{.sh}
mv config.ttl /opt/fuseki/run/
```

* Make run scripts executable

```{.sh}
sudo chmod +x fuseki-server
```

* Create log file

```{.sh}
touch fuseki.log
```

* Create shortcut start and stop scripts that use the config & log file
```{.sh}
cat >/opt/fuseki/start.sh <<EOL  
./fuseki-server --config=config.ttl > fuseki.log &  
EOL  
sudo chmod u+x start.sh
```

```{.sh}
cat >/opt/fuseki/stop.sh <<EOL  
echo "kill -9 \`ps aux | grep fuseki | grep -v grep | awk '{print \$2}'\`" > stop.sh  
EOL  
sudo chmod u+x stop.sh
```

* Set enviro vars
```{.sh}
export PATH=$PATH:/opt/fuseki  
export FUSEKI_HOME=/opt/fuseki
```

#### Run it
* Start Fuseki
```{.sh}
./start.sh
```

The API is now oline at http://{SERVER_URI}:3030

#### Extra access
* Allow non-localhost use of Fuseki admin UI  

```{.sh}
# follow the config directions given in run/shiro.ini 
# to edit that file in order to enable non-localhost access
```