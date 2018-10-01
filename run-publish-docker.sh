
# echo ' - Docker image - '
# echo $PREFIX
# echo $IMAGE
# echo ' - Github - '
# echo $GH_NAME
# echo $GH_EMAIL
# echo $GH_TOKEN
# echo ' - Docker login - '
# echo $DC_USER
# echo $DC_PASS
# echo ' - - '

set -e

if [ -z "$PREFIX" ]; then
    echo 'PREFIX variable is not set'
    exit 1
fi

if [ -z "$IMAGE" ]; then
    echo 'IMAGE variable is not set'
    exit 1
fi

if [ -z "$GH_NAME" ]; then
    echo 'GH_NAME variable is not set'
    exit 1
fi

if [ -z "$GH_EMAIL" ]; then
    echo 'GH_EMAIL variable is not set'
    exit 1
fi

if [ -z "$GH_TOKEN" ]; then
    echo 'GH_TOKEN variable is not set'
    exit 1
fi

if [ -z "$DC_USER" ]; then
    echo 'DC_USER variable is not set'
    exit 1
fi

if [ -z "$DC_PASS" ]; then
    echo 'DC_PASS variable is not set'
    exit 1
fi

version=`cat VERSION`
echo "version: $version"

docker build -t $PREFIX/$IMAGE:latest -f production.Dockerfile .

# tag it
docker tag $PREFIX/$IMAGE:latest $PREFIX/$IMAGE:$version

# login docker hub
docker login -u $DC_USER -p $DC_PASS

# push it
echo "publishing latest: ${PREFIX}/${IMAGE}:latest"
docker push ${PREFIX}/${IMAGE}:latest
echo "publishing version: ${PREFIX}/${IMAGE}:${version}"
docker push ${PREFIX}/${IMAGE}:${version}



# echo "GH_NAME='${GH_NAME}'" >> .envtemp
# echo "GH_EMAIL=${GH_EMAIL}" >> .envtemp
# echo "GH_TOKEN=${GH_TOKEN}" >> .envtemp
# echo "version=${version}" >> .envtemp
# echo "origin=${origin}" >> .envtemp

# docker run --rm -v `pwd`:"/app" -w "/app" --env-file .envtemp python:3 bash -c "sh run-git-version-update.sh"
# rm -rf .envtemp