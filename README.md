# go-sealights-pytest

# build
docker build -t mypytestimage --progress=plain .

# Running the test
docker run --network="host" mypytestimage

#instpect container
docker run -it --network="host" --entrypoint sh mypytestimage