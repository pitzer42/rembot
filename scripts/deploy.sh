heroku login -i

heroku create rembot-dev
heroku git:remote -a rembot-dev

git checkout main
git add --all
git commit -m 'heroku deploy'
git push heroku

heroku logs --tail


# Create Config Vars
# ex.: heroku config:set GITHUB_USERNAME=joesmith