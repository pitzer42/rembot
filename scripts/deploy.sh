heroku create rembot
heroku git:remote -a rembot

git checkout main
git add --all
git commit -m 'heroku deploy'
git push heroku


# Create Config Vars
# ex.: heroku config:set GITHUB_USERNAME=joesmith