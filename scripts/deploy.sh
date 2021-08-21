#heroku create rembot-dev
#heroku git:remote -a rembot-dev

git checkout main
git add --all
git commit -m 'heroku deploy'
git push heroku

heroku ps:scale worker=1 --app rembot-dev

heroku logs --tail

# Create Config Vars
# ex.: heroku config:set GITHUB_USERNAME=joesmith