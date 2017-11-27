# Setup

- Fork this repo
- Clone your copy of the repo to /home/osirv/labs/last_name/osirv_labs/
- After cloning the repo, always make sure that git knows who you are.
If you are using this repo in the labs, each time run: 
```
git config user.name "YOUR_NAME_OR_NICK"
git config user.email "YOUR_EMAIL@ADDRESS.com"
```

# Setdown

- Commit and push everything to your repo
- Delete this directory with:
```
rm -rf /home/osirv/labs/lastname/osirv_labs
```

# Pulling the additional materials to your copy of the repo:

``` 
git remote add upstream https://gitlab.com/levara/osirv_labs
git fetch upstream master
git merge upstream/master
```

