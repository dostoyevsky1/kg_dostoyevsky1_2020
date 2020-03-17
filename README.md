# kg_dostoyevsky1_2020

### Python script to test strings for one-to-one mapping (isomorphism)

##### Implementation method 1 (with Python installed) -- Clone repo to local machine >> cd into repo >> run script

Clone repo:
```
git clone https://github.com/dostoyevsky1/kg_dostoyevsky1_2020.git
```

Cd into repo:
```
cd kg_dostoyevsky1_2020/
```

Run script:
```
python3 main.py 123 321
```

##### Implementation method 2 (with Docker installed) -- Pull docker image to local machine >> run container >> run script
##### Docker image: https://hub.docker.com/repository/docker/dostoyevsky/isomorphism

Pull image:
```
docker pull -a dostoyevsky/isomorphism
```

Run container:
```
docker run -it dostoyevsky/isomorphism:1.0 /bin/bash
```

Run script:
```
python3 main.py 123 321
```

OR

Run container + script:
```
docker run -it dostoyevsky/isomorphism:1.0 python main.py 123 321
```


