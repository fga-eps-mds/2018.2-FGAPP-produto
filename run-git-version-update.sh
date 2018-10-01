git config --global user.name "${GH_NAME}"
git config --global user.email "${GH_EMAIL}"
echo "machine github.com login ${GH_NAME} password ${GH_TOKEN}" > ~/.netrc

# tag it
git add -A
git commit -m "version $version"
git tag -a "$version" -m "version $version"
git push $origin master
git push $origin master --tags
