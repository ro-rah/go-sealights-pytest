# go-sealights-pytest
Don't forget to include an sltoken.txt file in the root of the cloned repo

# build
docker build -t mypytestimage --progress=plain .

# Running the test
docker run --network="host" mypytestimage

#instpect container
docker run -it --network="host" --entrypoint sh mypytestimage